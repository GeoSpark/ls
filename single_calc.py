# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'single_calc.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SingleCalcDialog(object):
    def setupUi(self, SingleCalcDialog):
        SingleCalcDialog.setObjectName("SingleCalcDialog")
        SingleCalcDialog.resize(898, 536)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SingleCalcDialog.sizePolicy().hasHeightForWidth())
        SingleCalcDialog.setSizePolicy(sizePolicy)
        SingleCalcDialog.setMinimumSize(QtCore.QSize(720, 463))
        SingleCalcDialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        SingleCalcDialog.setSizeGripEnabled(False)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(SingleCalcDialog)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.MessageBar = QtWidgets.QWidget(SingleCalcDialog)
        self.MessageBar.setObjectName("MessageBar")
        self.verticalLayout_6.addWidget(self.MessageBar)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.RadioGroup = QtWidgets.QGroupBox(SingleCalcDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RadioGroup.sizePolicy().hasHeightForWidth())
        self.RadioGroup.setSizePolicy(sizePolicy)
        self.RadioGroup.setFlat(False)
        self.RadioGroup.setCheckable(False)
        self.RadioGroup.setObjectName("RadioGroup")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.RadioGroup)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.OrientRadio = QtWidgets.QRadioButton(self.RadioGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OrientRadio.sizePolicy().hasHeightForWidth())
        self.OrientRadio.setSizePolicy(sizePolicy)
        self.OrientRadio.setObjectName("OrientRadio")
        self.radioButtonGroup = QtWidgets.QButtonGroup(SingleCalcDialog)
        self.radioButtonGroup.setObjectName("radioButtonGroup")
        self.radioButtonGroup.addButton(self.OrientRadio)
        self.verticalLayout_5.addWidget(self.OrientRadio)
        self.RadialRadio = QtWidgets.QRadioButton(self.RadioGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RadialRadio.sizePolicy().hasHeightForWidth())
        self.RadialRadio.setSizePolicy(sizePolicy)
        self.RadialRadio.setObjectName("RadialRadio")
        self.radioButtonGroup.addButton(self.RadialRadio)
        self.verticalLayout_5.addWidget(self.RadialRadio)
        self.IntersectRadio = QtWidgets.QRadioButton(self.RadioGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IntersectRadio.sizePolicy().hasHeightForWidth())
        self.IntersectRadio.setSizePolicy(sizePolicy)
        self.IntersectRadio.setObjectName("IntersectRadio")
        self.radioButtonGroup.addButton(self.IntersectRadio)
        self.verticalLayout_5.addWidget(self.IntersectRadio)
        self.ResectionRadio = QtWidgets.QRadioButton(self.RadioGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ResectionRadio.sizePolicy().hasHeightForWidth())
        self.ResectionRadio.setSizePolicy(sizePolicy)
        self.ResectionRadio.setObjectName("ResectionRadio")
        self.radioButtonGroup.addButton(self.ResectionRadio)
        self.verticalLayout_5.addWidget(self.ResectionRadio)
        self.FreeRadio = QtWidgets.QRadioButton(self.RadioGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FreeRadio.sizePolicy().hasHeightForWidth())
        self.FreeRadio.setSizePolicy(sizePolicy)
        self.FreeRadio.setObjectName("FreeRadio")
        self.radioButtonGroup.addButton(self.FreeRadio)
        self.verticalLayout_5.addWidget(self.FreeRadio)
        spacerItem = QtWidgets.QSpacerItem(20, 49, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.horizontalLayout_3.addWidget(self.RadioGroup)
        self.StationGroup = QtWidgets.QGroupBox(SingleCalcDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StationGroup.sizePolicy().hasHeightForWidth())
        self.StationGroup.setSizePolicy(sizePolicy)
        self.StationGroup.setObjectName("StationGroup")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.StationGroup)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Station1Label = QtWidgets.QLabel(self.StationGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Station1Label.sizePolicy().hasHeightForWidth())
        self.Station1Label.setSizePolicy(sizePolicy)
        self.Station1Label.setObjectName("Station1Label")
        self.verticalLayout_4.addWidget(self.Station1Label)
        self.Station1Combo = QtWidgets.QComboBox(self.StationGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Station1Combo.sizePolicy().hasHeightForWidth())
        self.Station1Combo.setSizePolicy(sizePolicy)
        self.Station1Combo.setMinimumSize(QtCore.QSize(150, 0))
        self.Station1Combo.setObjectName("Station1Combo")
        self.verticalLayout_4.addWidget(self.Station1Combo)
        self.Station2Label = QtWidgets.QLabel(self.StationGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Station2Label.sizePolicy().hasHeightForWidth())
        self.Station2Label.setSizePolicy(sizePolicy)
        self.Station2Label.setObjectName("Station2Label")
        self.verticalLayout_4.addWidget(self.Station2Label)
        self.Station2Combo = QtWidgets.QComboBox(self.StationGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Station2Combo.sizePolicy().hasHeightForWidth())
        self.Station2Combo.setSizePolicy(sizePolicy)
        self.Station2Combo.setMinimumSize(QtCore.QSize(150, 0))
        self.Station2Combo.setObjectName("Station2Combo")
        self.verticalLayout_4.addWidget(self.Station2Combo)
        spacerItem1 = QtWidgets.QSpacerItem(20, 86, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_3.addWidget(self.StationGroup)
        self.PointsGroup = QtWidgets.QGroupBox(SingleCalcDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PointsGroup.sizePolicy().hasHeightForWidth())
        self.PointsGroup.setSizePolicy(sizePolicy)
        self.PointsGroup.setObjectName("PointsGroup")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.PointsGroup)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.TargetPointsLabel = QtWidgets.QLabel(self.PointsGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TargetPointsLabel.sizePolicy().hasHeightForWidth())
        self.TargetPointsLabel.setSizePolicy(sizePolicy)
        self.TargetPointsLabel.setObjectName("TargetPointsLabel")
        self.verticalLayout_2.addWidget(self.TargetPointsLabel)
        self.SourceList = QtWidgets.QListWidget(self.PointsGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SourceList.sizePolicy().hasHeightForWidth())
        self.SourceList.setSizePolicy(sizePolicy)
        self.SourceList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.SourceList.setObjectName("SourceList")
        self.verticalLayout_2.addWidget(self.SourceList)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.AddButton = QtWidgets.QPushButton(self.PointsGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddButton.sizePolicy().hasHeightForWidth())
        self.AddButton.setSizePolicy(sizePolicy)
        self.AddButton.setObjectName("AddButton")
        self.verticalLayout.addWidget(self.AddButton)
        self.AddAllButton = QtWidgets.QPushButton(self.PointsGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddAllButton.sizePolicy().hasHeightForWidth())
        self.AddAllButton.setSizePolicy(sizePolicy)
        self.AddAllButton.setObjectName("AddAllButton")
        self.verticalLayout.addWidget(self.AddAllButton)
        self.RemoveButton = QtWidgets.QPushButton(self.PointsGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RemoveButton.sizePolicy().hasHeightForWidth())
        self.RemoveButton.setSizePolicy(sizePolicy)
        self.RemoveButton.setObjectName("RemoveButton")
        self.verticalLayout.addWidget(self.RemoveButton)
        self.RemoveAllButton = QtWidgets.QPushButton(self.PointsGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RemoveAllButton.sizePolicy().hasHeightForWidth())
        self.RemoveAllButton.setSizePolicy(sizePolicy)
        self.RemoveAllButton.setObjectName("RemoveAllButton")
        self.verticalLayout.addWidget(self.RemoveAllButton)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.UsedPointsLabel = QtWidgets.QLabel(self.PointsGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UsedPointsLabel.sizePolicy().hasHeightForWidth())
        self.UsedPointsLabel.setSizePolicy(sizePolicy)
        self.UsedPointsLabel.setObjectName("UsedPointsLabel")
        self.verticalLayout_3.addWidget(self.UsedPointsLabel)
        self.TargetList = QtWidgets.QListWidget(self.PointsGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TargetList.sizePolicy().hasHeightForWidth())
        self.TargetList.setSizePolicy(sizePolicy)
        self.TargetList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.TargetList.setObjectName("TargetList")
        self.verticalLayout_3.addWidget(self.TargetList)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_3.addWidget(self.PointsGroup)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.ResultGroup = QtWidgets.QGroupBox(SingleCalcDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.ResultGroup.sizePolicy().hasHeightForWidth())
        self.ResultGroup.setSizePolicy(sizePolicy)
        self.ResultGroup.setObjectName("ResultGroup")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.ResultGroup)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.ResultTextBrowser = QtWidgets.QTextBrowser(self.ResultGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ResultTextBrowser.sizePolicy().hasHeightForWidth())
        self.ResultTextBrowser.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.ResultTextBrowser.setFont(font)
        self.ResultTextBrowser.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.ResultTextBrowser.setObjectName("ResultTextBrowser")
        self.horizontalLayout_5.addWidget(self.ResultTextBrowser)
        self.verticalLayout_6.addWidget(self.ResultGroup)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.HelpButton = QtWidgets.QPushButton(SingleCalcDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HelpButton.sizePolicy().hasHeightForWidth())
        self.HelpButton.setSizePolicy(sizePolicy)
        self.HelpButton.setObjectName("HelpButton")
        self.horizontalLayout_2.addWidget(self.HelpButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.CalcButton = QtWidgets.QPushButton(SingleCalcDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CalcButton.sizePolicy().hasHeightForWidth())
        self.CalcButton.setSizePolicy(sizePolicy)
        self.CalcButton.setObjectName("CalcButton")
        self.horizontalLayout_2.addWidget(self.CalcButton)
        self.ResetButton = QtWidgets.QPushButton(SingleCalcDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ResetButton.sizePolicy().hasHeightForWidth())
        self.ResetButton.setSizePolicy(sizePolicy)
        self.ResetButton.setObjectName("ResetButton")
        self.horizontalLayout_2.addWidget(self.ResetButton)
        self.CloseButton = QtWidgets.QPushButton(SingleCalcDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CloseButton.sizePolicy().hasHeightForWidth())
        self.CloseButton.setSizePolicy(sizePolicy)
        self.CloseButton.setObjectName("CloseButton")
        self.horizontalLayout_2.addWidget(self.CloseButton)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.retranslateUi(SingleCalcDialog)
        QtCore.QMetaObject.connectSlotsByName(SingleCalcDialog)
        SingleCalcDialog.setTabOrder(self.OrientRadio, self.RadialRadio)
        SingleCalcDialog.setTabOrder(self.RadialRadio, self.IntersectRadio)
        SingleCalcDialog.setTabOrder(self.IntersectRadio, self.ResectionRadio)
        SingleCalcDialog.setTabOrder(self.ResectionRadio, self.FreeRadio)
        SingleCalcDialog.setTabOrder(self.FreeRadio, self.Station1Combo)
        SingleCalcDialog.setTabOrder(self.Station1Combo, self.Station2Combo)
        SingleCalcDialog.setTabOrder(self.Station2Combo, self.AddButton)
        SingleCalcDialog.setTabOrder(self.AddButton, self.AddAllButton)
        SingleCalcDialog.setTabOrder(self.AddAllButton, self.RemoveButton)
        SingleCalcDialog.setTabOrder(self.RemoveButton, self.RemoveAllButton)
        SingleCalcDialog.setTabOrder(self.RemoveAllButton, self.HelpButton)
        SingleCalcDialog.setTabOrder(self.HelpButton, self.CalcButton)
        SingleCalcDialog.setTabOrder(self.CalcButton, self.ResetButton)
        SingleCalcDialog.setTabOrder(self.ResetButton, self.CloseButton)

    def retranslateUi(self, SingleCalcDialog):
        _translate = QtCore.QCoreApplication.translate
        SingleCalcDialog.setWindowTitle(_translate("SingleCalcDialog", "Single Point Calculations"))
        self.RadioGroup.setTitle(_translate("SingleCalcDialog", "Calculation"))
        self.OrientRadio.setToolTip(_translate("SingleCalcDialog", "Calculate orientation angle  on stations"))
        self.OrientRadio.setText(_translate("SingleCalcDialog", "Orientation"))
        self.RadialRadio.setText(_translate("SingleCalcDialog", "Radial Survey"))
        self.IntersectRadio.setText(_translate("SingleCalcDialog", "Intersection"))
        self.ResectionRadio.setText(_translate("SingleCalcDialog", "Resection"))
        self.FreeRadio.setText(_translate("SingleCalcDialog", "Free Station"))
        self.StationGroup.setTitle(_translate("SingleCalcDialog", "Station"))
        self.Station1Label.setText(_translate("SingleCalcDialog", "Station 1"))
        self.Station2Label.setText(_translate("SingleCalcDialog", "Station 2"))
        self.PointsGroup.setTitle(_translate("SingleCalcDialog", "Points"))
        self.TargetPointsLabel.setText(_translate("SingleCalcDialog", "Target Points"))
        self.AddButton.setText(_translate("SingleCalcDialog", "Add >"))
        self.AddAllButton.setText(_translate("SingleCalcDialog", "Add all"))
        self.RemoveButton.setText(_translate("SingleCalcDialog", "< Remove"))
        self.RemoveAllButton.setText(_translate("SingleCalcDialog", "Remove all"))
        self.UsedPointsLabel.setText(_translate("SingleCalcDialog", "Used Points"))
        self.ResultGroup.setTitle(_translate("SingleCalcDialog", "Result of Calculations"))
        self.HelpButton.setText(_translate("SingleCalcDialog", "Help"))
        self.CalcButton.setText(_translate("SingleCalcDialog", "Calculate"))
        self.ResetButton.setText(_translate("SingleCalcDialog", "Reset"))
        self.CloseButton.setText(_translate("SingleCalcDialog", "Close"))
