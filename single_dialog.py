# -*- coding: utf-8 -*-
"""
.. module:: single_dialog
    :platform: Linux, Windows
    :synopsis: GUI for single point calculations

.. moduleauthor: Zoltan Siki <siki@agt.bme.hu>
"""
from __future__ import absolute_import

import platform
import webbrowser

from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtGui import QFont, QStandardItem
from qgis.PyQt.QtWidgets import QDialog, QListWidgetItem, QSizePolicy
from qgis.gui import QgsMessageBar

from .prettytable.prettytable import PrettyTable
from .calculation import Calculation
from .gama_interface import *
from .resultlog import *
from .single_calc import Ui_SingleCalcDialog


class SingleDialog(QDialog):
    """ Class for single point calculation dialog (intersection, resection, ...)
    """

    def __init__(self, log):
        """ Initialize dialog data and event handlers
        """
        super(SingleDialog, self).__init__(flags=Qt.Dialog)
        self.ui = Ui_SingleCalcDialog()
        self.ui.setupUi(self)
        self.ui.MessageBar = QgsMessageBar()
        self.ui.MessageBar.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.ui.verticalLayout_6.insertWidget(0, self.ui.MessageBar, 0)
        self.log = log

        # event handlers
        self.ui.OrientRadio.toggled.connect(self.radioClicked)
        self.ui.RadialRadio.toggled.connect(self.radioClicked)
        self.ui.IntersectRadio.toggled.connect(self.radioClicked)
        self.ui.ResectionRadio.toggled.connect(self.radioClicked)
        self.ui.FreeRadio.toggled.connect(self.radioClicked)
        self.ui.Station1Combo.currentIndexChanged.connect(self.stationComboChanged)
        self.ui.Station2Combo.currentIndexChanged.connect(self.stationComboChanged)
        self.ui.AddButton.clicked.connect(self.onAddButton)
        self.ui.AddAllButton.clicked.connect(self.onAddAllButton)
        self.ui.RemoveButton.clicked.connect(self.onRemoveButton)
        self.ui.RemoveAllButton.clicked.connect(self.onRemoveAllButton)
        self.ui.CalcButton.clicked.connect(self.onCalcButton)
        self.ui.ResetButton.clicked.connect(self.onResetButton)
        self.ui.CloseButton.clicked.connect(self.onCloseButton)
        self.ui.HelpButton.clicked.connect(self.onHelpButton)
        self.ui.SourceList.setSortingEnabled(True)

    def showEvent(self, event):
        """ Reset dialog when receives a show event.

            :param event: NOT USED
        """
        if platform.system() == 'Linux':
            # change font
            self.ui.ResultTextBrowser.setFont(QFont(config.fontname, int(config.fontsize)))
        self.log.set_log_path(config.log_path)
        self.reset()

    def reset(self):
        """ Reset dialog to initial state
        """
        # reset radio buttons
        self.ui.radioButtonGroup.setExclusive(False)
        self.ui.OrientRadio.setChecked(False)
        self.ui.RadialRadio.setChecked(False)
        self.ui.IntersectRadio.setChecked(False)
        self.ui.ResectionRadio.setChecked(False)
        self.ui.FreeRadio.setChecked(False)
        self.ui.radioButtonGroup.setExclusive(True)

        # disable widgets
        self.ui.Station1Combo.setEnabled(False)
        self.ui.Station2Combo.setEnabled(False)

        # clear widgets
        self.ui.Station1Combo.clear()
        self.ui.Station2Combo.clear()
        self.ui.SourceList.clear()
        self.ui.TargetList.clear()
        self.ui.ResultTextBrowser.clear()

    def fillStationCombos(self):
        """ Change dialog controls when an other calculation type selected.
        """
        # get selected stations
        oldStation1 = self.ui.Station1Combo.itemData(self.ui.Station1Combo.currentIndex())
        oldStation2 = self.ui.Station2Combo.itemData(self.ui.Station2Combo.currentIndex())
        # clear station combos
        self.ui.Station1Combo.clear()
        self.ui.Station2Combo.clear()
        self.ui.Station1Combo.setEnabled(False)
        self.ui.Station2Combo.setEnabled(False)

        # get combobox models
        combomodel1 = self.ui.Station1Combo.model()
        combomodel2 = self.ui.Station2Combo.model()

        # get stations
        known_stations = get_stations(True, False)
        all_stations = get_stations(False, False)
        oriented_stations = get_stations(True, True)
        # fill Station1Combo and Station2Combo
        stations1 = []
        stations2 = []
        if known_stations is not None and self.ui.OrientRadio.isChecked():
            for stn in known_stations:
                stations1.append([u"%s (%s:%s)" % (stn[0], stn[1], stn[2]), stn])
            self.ui.Station1Combo.setEnabled(True)
        elif oriented_stations is not None and (self.ui.RadialRadio.isChecked() or
                                                self.ui.IntersectRadio.isChecked()):
            for stn in oriented_stations:
                stations1.append([u"%s (%s:%s)" % (stn[0], stn[1], stn[2]), stn])
                if self.ui.IntersectRadio.isChecked():
                    stations2.append([u"%s (%s:%s)" % (stn[0], stn[1], stn[2]), stn])
            self.ui.Station1Combo.setEnabled(True)
            if self.ui.IntersectRadio.isChecked():
                self.ui.Station2Combo.setEnabled(True)
        elif all_stations is not None and (self.ui.ResectionRadio.isChecked() or
                                           self.ui.FreeRadio.isChecked()):
            self.ui.Station1Combo.setEnabled(True)
            for stn in all_stations:
                stations1.append([u"%s (%s:%s)" % (stn[0], stn[1], stn[2]), stn])

        known_points = get_known()
        if stations1 is not None:
            for station in stations1:
                item = QStandardItem(station[0])
                item.setData(station[1], Qt.UserRole)
                if known_points is not None and station[1][0] in known_points:
                    itemfont = item.font()
                    itemfont.setWeight(QFont.Bold)
                    item.setFont(itemfont)
                combomodel1.appendRow(item)
        if self.ui.IntersectRadio.isChecked() and stations2 is not None:
            for station in stations2:
                item = QStandardItem(station[0])
                item.setData(station[1], Qt.UserRole)
                if known_points is not None and station[1][0] in known_points:
                    itemfont = item.font()
                    itemfont.setWeight(QFont.Bold)
                    item.setFont(itemfont)
                combomodel2.appendRow(item)

        # select previously selected stations if present in the list
        self.ui.Station1Combo.setCurrentIndex(self.ui.Station1Combo.findData(oldStation1))
        self.ui.Station2Combo.setCurrentIndex(self.ui.Station2Combo.findData(oldStation2))

    def fillSourceList(self):
        """ Change dialog controls when an other calculation type selected.
        """
        # get the selected stations
        stn1 = self.ui.Station1Combo.itemData(self.ui.Station1Combo.currentIndex())
        stn2 = self.ui.Station2Combo.itemData(self.ui.Station2Combo.currentIndex())
        # clear source and target list
        self.ui.SourceList.clear()
        self.ui.TargetList.clear()
        # get target points according to the stations
        targets = []
        if stn1 is not None and (self.ui.OrientRadio.isChecked() or
                                 self.ui.ResectionRadio.isChecked() or self.ui.FreeRadio.isChecked()):
            targets = get_targets(stn1[0], stn1[1], stn1[2], True)
        elif stn1 is not None and self.ui.RadialRadio.isChecked():
            targets = get_targets(stn1[0], stn1[1], stn1[2], False, True)
        elif stn1 is not None and stn2 is not None and \
                self.ui.IntersectRadio.isChecked():
            # fill source list for intersection (common points)
            targets_stn1 = get_targets(stn1[0], stn1[1], stn1[2], False)
            targets_stn2 = get_targets(stn2[0], stn2[1], stn2[2], False)
            for t1 in targets_stn1:
                for t2 in targets_stn2:
                    if t1[0] == t2[0]:
                        if not t1[0] in targets:
                            targets.append([t1, t2])
                        break

        # fill source list widget
        known_list = get_known()
        if targets is not None:
            for target in targets:
                if self.ui.IntersectRadio.isChecked():
                    item = QListWidgetItem(target[0][0])
                    item.setData(Qt.UserRole, target)
                    if known_list is not None and target[0][0] in known_list:
                        itemfont = item.font()
                        itemfont.setWeight(QFont.Bold)
                        item.setFont(itemfont)
                else:
                    item = QListWidgetItem(u"%s (id:%s)" % (target[0], target[2]))
                    item.setData(Qt.UserRole, target)
                    if known_list is not None and target[0] in known_list:
                        itemfont = item.font()
                        itemfont.setWeight(QFont.Bold)
                        item.setFont(itemfont)
                self.ui.SourceList.addItem(item)

    def radioClicked(self):
        """ Change dialog controls when an other calculation type selected.
        """
        self.fillStationCombos()
        self.fillSourceList()

    def stationComboChanged(self):
        """ Init source and target list when one of two station combobox changed.
        """
        self.fillSourceList()

    def onAddButton(self):
        """ Add selected target points to used points list.
        """
        selected = self.ui.SourceList.selectedItems()
        for item in selected:
            self.ui.TargetList.addItem(self.ui.SourceList.takeItem(self.ui.SourceList.row(item)))

    def onAddAllButton(self):
        """ Add all target points to used points list.
        """
        while self.ui.SourceList.count():
            self.ui.TargetList.addItem(self.ui.SourceList.takeItem(0))

    def onRemoveButton(self):
        """ Remove selected used points and add to target points list.
        """
        selected = self.ui.TargetList.selectedItems()
        for item in selected:
            self.ui.SourceList.addItem(self.ui.TargetList.takeItem(self.ui.TargetList.row(item)))

    def onRemoveAllButton(self):
        """ Remove all used points and add to target points list.
        """
        while self.ui.TargetList.count():
            self.ui.SourceList.addItem(self.ui.TargetList.takeItem(0))

    def onCalcButton(self):
        """ Start a calculation when the Calculate button pushed.
        """
        # TODO: Disable the calculate button until we have a valid set up.
        if self.ui.radioButtonGroup.checkedId() == -1:
            self.ui.MessageBar.pushMessage(tr('SurveyingCalculation'), tr('Select the type of calculation'),
                                           level=Qgis.Critical)
            return

        # get the selected stations
        stn1 = self.ui.Station1Combo.itemData(self.ui.Station1Combo.currentIndex())
        if stn1 is None:
            self.ui.MessageBar.pushMessage(tr('SurveyingCalculation'), tr('Select station point 1'),
                                           level=Qgis.Critical)
            self.ui.Station1Combo.setFocus()
            return
        stn2 = self.ui.Station2Combo.itemData(self.ui.Station2Combo.currentIndex())
        if stn2 is None and self.ui.IntersectRadio.isChecked():
            self.ui.MessageBar.pushMessage(tr('SurveyingCalculation'), tr('Select station point 2'),
                                           level=Qgis.Critical)
            self.ui.Station2Combo.setFocus()
            return
        if self.ui.TargetList.count() == 0:
            self.ui.MessageBar.pushMessage(tr('SurveyingCalculation'), tr('Add points to Used Points list'),
                                           level=Qgis.Critical)
            self.ui.TargetList.setFocus()
            return

        if self.ui.OrientRadio.isChecked():
            # orientation
            s = get_station(stn1[0], stn1[1], stn1[2])
            ref_list = []
            for i in range(self.ui.TargetList.count()):
                targetp = self.ui.TargetList.item(i).data(Qt.UserRole)
                to = get_target(targetp[0], targetp[1], targetp[2])
                tp = ScPoint(targetp[0])
                ref_list.append([tp, to])

            try:
                z, rows = Calculation.orientation(s, ref_list)
            except (ValueError, TypeError, AttributeError) as e:
                self.ui.MessageBar.pushMessage(tr('SurveyingCalculation'), str(e), level=Qgis.Critical)
                return

            ang_err_label = 'Ang err'

            if ANGLE_UNITS_DISP[config.angle_displayed] in ('DEG', 'DMS'):
                ang_err_label += ' (")'
            elif ANGLE_UNITS_DISP[config.angle_displayed] == 'GON':
                ang_err_label += ' (cc)'
            elif ANGLE_UNITS_DISP[config.angle_displayed] == 'RAD':
                ang_err_label += ' (r)'

            x = PrettyTable()
            x.field_names = ['Point num', 'Code', 'Direction', 'Bearing', 'Orient ang', 'Distance', ang_err_label,
                             'Dist err']
            x.align['Point num'] = 'l'
            x.align['Code'] = 'l'
            x.align['Direction'] = 'r'
            x.align['Bearing'] = 'r'
            x.align['Orient ang'] = 'r'
            x.align['Distance'] = 'r'
            x.align[ang_err_label] = 'r'
            x.align['Dist err'] = 'r'
            x.float_format = '0.3'

            for r in rows:
                x.add_row(r)

            set_orientationangle(stn1[0], stn1[1], stn1[2], z.get_angle(ANGLE_UNITS_STORE[config.angle_stored]))

            res = "\n" + tr('Orientation') + ' - %s\n' % s.p.id
            res += x.get_string()
            res += u"\n%-48s %s\n" % \
                   (tr('Average orientation angle'), z.get_angle(ANGLE_UNITS_DISP[config.angle_displayed]))
            self.ui.ResultTextBrowser.append(res)
            self.log.write()
            self.log.write(res)

        elif self.ui.RadialRadio.isChecked():
            # radial surveys (polar point)
            s = get_station(stn1[0], stn1[1], stn1[2])
            x = PrettyTable()
            x.field_names = ['Point num', 'Code', 'E', 'N', 'Z', 'Bearing', 'H. Distance']
            x.align['Point num'] = 'l'
            x.align['Code'] = 'l'
            x.align['E'] = 'r'
            x.align['N'] = 'r'
            x.align['Z'] = 'r'
            x.align['Bearing'] = 'r'
            x.align['H. Distance'] = 'r'
            x.float_format = '0.3'

            x.add_row((s.p.id, (s.p.pc if s.p.pc is not None else "-"), s.p.e, s.p.n,
                       (s.p.z if s.p.z is not None else ""), '<station>', ''))

            for i in range(self.ui.TargetList.count()):
                targetp = self.ui.TargetList.item(i).data(Qt.UserRole)
                to = get_target(targetp[0], targetp[1], targetp[2])
                pp, row = Calculation.polarpoint(s, to)

                if pp is not None:
                    tp = ScPoint(pp)
                    x.add_row(row)

                    if pp.z is None:
                        # no z calculated
                        tp.store_coord(2)
                    else:
                        tp.store_coord(3)
                else:
                    self.ui.MessageBar.pushMessage(tr('SurveyingCalculation'),
                                                   tr('Radial survey on %s cannot be calculated!') % targetp[0],
                                                   level=Qgis.Critical)

            res = "\n" + tr("Radial Survey") + '\n'
            res += x.get_string()
            self.ui.ResultTextBrowser.append(res)
            self.log.write()
            self.log.write_log(res)

        elif self.ui.IntersectRadio.isChecked():
            # intersection
            s1 = get_station(stn1[0], stn1[1], stn1[2])
            s2 = get_station(stn2[0], stn2[1], stn2[2])
            if stn1 == stn2:
                self.ui.MessageBar.pushMessage(tr('SurveyingCalculation'), tr('Station 1 and station 2 are the same!'),
                                               level=Qgis.Critical)
                self.ui.Station1Combo.setFocus()
                return

            x = PrettyTable()
            x.field_names = ['Point num', 'Code', 'E', 'N', 'Bearing 1', 'Bearing 2']
            x.align['Point num'] = 'l'
            x.align['Code'] = 'l'
            x.align['E'] = 'r'
            x.align['N'] = 'r'
            x.align['Bearing 1'] = 'r'
            x.align['Bearing 2'] = 'r'
            x.float_format = '0.3'

            x.add_row((s1.p.id, (s1.p.pc if s1.p.pc is not None else "-"), s1.p.e, s1.p.n, '<station>', ''))
            x.add_row((s2.p.id, (s2.p.pc if s2.p.pc is not None else "-"), s2.p.e, s2.p.n, '<station>', ''))

            for i in range(self.ui.TargetList.count()):
                itemdata = self.ui.TargetList.item(i).data(Qt.UserRole)
                targetp1 = itemdata[0]
                targetp2 = itemdata[1]
                to1 = get_target(targetp1[0], targetp1[1], targetp1[2])
                tp1 = ScPoint(targetp1[0])
                to2 = get_target(targetp2[0], targetp2[1], targetp2[2])
                # tp2 = ScPoint(targetp2[0])
                ip, row = Calculation.intersection(s1, to1, s2, to2)
                if ip is not None:
                    tp1.set_coord(ip)
                    tp1.store_coord(2)
                    x.add_row(row)
                else:
                    self.ui.MessageBar.pushMessage(tr('SurveyingCalculation'),
                                                   tr('Intersecion on %s cannot be calculated!') % targetp1[0],
                                                   level=Qgis.Critical)

            res = "\n" + tr("Intersection") + '\n'
            res += x.get_string()
            self.ui.ResultTextBrowser.append(res)
            self.log.write()
            self.log.write_log(res)

        elif self.ui.ResectionRadio.isChecked():
            # resection
            s = get_station(stn1[0], stn1[1], stn1[2])
            if self.ui.TargetList.count() != 3:
                self.ui.MessageBar.pushMessage(tr('SurveyingCalculation'),
                                               tr('Select exactly 3 used points for resection!'), level=Qgis.Critical)
                self.ui.TargetList.setFocus()
                return
            targetp1 = self.ui.TargetList.item(0).data(Qt.UserRole)
            targetp2 = self.ui.TargetList.item(1).data(Qt.UserRole)
            targetp3 = self.ui.TargetList.item(2).data(Qt.UserRole)
            to1 = get_target(targetp1[0], targetp1[1], targetp1[2])
            to2 = get_target(targetp2[0], targetp2[1], targetp2[2])
            to3 = get_target(targetp3[0], targetp3[1], targetp3[2])
            tp1 = ScPoint(targetp1[0])
            tp2 = ScPoint(targetp2[0])
            tp3 = ScPoint(targetp3[0])
            rp, rows = Calculation.resection(s, tp1, tp2, tp3, to1, to2, to3)
            ScPoint(rp).store_coord(2)
            # result log
            x = PrettyTable()
            x.field_names = ['Point num', 'Code', 'E', 'N', 'Direction', 'Angle']
            x.align['Point num'] = 'l'
            x.align['Code'] = 'l'
            x.align['E'] = 'r'
            x.align['N'] = 'r'
            x.align['Direction'] = 'r'
            x.align['Angle'] = 'r'
            x.float_format = '0.3'

            for row in rows:
                x.add_row(row)

            res = "\n" + tr("Resection") + '\n'
            res += x.get_string()
            self.ui.ResultTextBrowser.append(res)
            self.log.write()
            self.log.write_log(res)

        elif self.ui.FreeRadio.isChecked():
            # free station
            g = GamaInterface()  # default standard deviations are used!
            s = get_station(stn1[0], stn1[1], stn1[2])
            g.add_point(s.p, 'ADJ')
            g.add_observation(s.o)
            for i in range(self.ui.TargetList.count()):
                targetp = self.ui.TargetList.item(i).data(Qt.UserRole)
                fp = get_coord(targetp[0])
                g.add_point(fp, 'FIX')
                to = get_target(targetp[0], targetp[1], targetp[2])
                g.add_observation(to)
            t = g.adjust()
            if t is None:
                # adjustment failed
                self.ui.ResultTextBrowser.append(tr('gama-local not installed or other runtime error'))
            else:
                self.ui.ResultTextBrowser.append(t.decode('utf-8'))

    def onResetButton(self):
        """ Reset dialog when the Reset button pushed.
        """
        self.reset()

    def onCloseButton(self):
        """ Close the dialog when the Close button pushed.
        """
        self.accept()

    def onHelpButton(self):
        """ Open user's guide at Single Point Calculations in the default web browser.
        """
        webbrowser.open("http://www.digikom.hu/SurveyingCalculation/usersguide.html#single-point-calculations")
