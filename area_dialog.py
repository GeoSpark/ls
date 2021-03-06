# -*- coding: utf-8 -*-
"""
.. module:: area_dialog
    :platform: Linux, Windows
    :synopsis: GUI for area division

.. moduleauthor: Zoltan Siki <siki@agt.bme.hu>
"""
from __future__ import absolute_import
from builtins import str
from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtWidgets import QDialog
from qgis.core import Qgis
from qgis.utils import iface

from .area_div import Ui_AreaDivDialog
from .base_classes import tr


class AreaDialog(QDialog):
    """ Class for area division dialog
    """

    def __init__(self, total_area, div_area, rotate):
        """ Initialize dialog data and event handlers
        """
        super(AreaDialog, self).__init__(flags=Qt.Dialog)
        self.total_area = int(total_area + 0.5)
        self.div_area = int(div_area + 0.5)
        self.rotate = rotate
        self.ui = Ui_AreaDivDialog()
        self.ui.setupUi(self)
        self.ui.CancelButton.clicked.connect(self.onCancelButton)
        self.ui.DivideButton.clicked.connect(self.onDivideButton)

    def showEvent(self, event):
        """ Set up initial state of dialog widgets

            :param event: NOT USED
        """
        self.reset()

    def reset(self):
        """ Reset dialog to initial state
        """
        self.ui.AreaLineEdit.setText(str(self.div_area))
        self.ui.TotalLineEdit.setText(str(self.total_area))
        self.ui.TwoPointRadio.setChecked(True)
        if self.rotate:
            self.ui.OnePointRadio.setEnabled(True)
        else:
            self.ui.OnePointRadio.setEnabled(False)

    def onDivideButton(self):
        """ Check input and accept dialog
        """
        try:
            a = float(self.ui.AreaLineEdit.text())
        except ValueError:
            iface.messageBar().pushMessage(tr('Warning'), tr('Invalid area value'), level=Qgis.Warning)
            return
        if a <= 0:
            iface.messageBar().pushMessage(tr('Warning'), tr('Invalid area value'), level=Qgis.Warning)
            return
        if not self.ui.OnePointRadio.isChecked() and not self.ui.TwoPointRadio.isChecked():
            iface.messageBar().pushMessage(tr('Warning'), tr('Select division method'), level=Qgis.Warning)
            return
        self.accept()

    def onCancelButton(self):
        """ Reject dialog
        """
        self.reject()
