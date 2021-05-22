# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wrfgui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
import sys
from datetime import datetime, timedelta as td
import stevedore
#from stevedore.sanity import is_sane
import os
import subprocess


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(861, 899)
        MainWindow.setDockNestingEnabled(True)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks|QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.runwrfbutton = QtWidgets.QPushButton(self.centralwidget)
        self.runwrfbutton.setGeometry(QtCore.QRect(400, 20, 81, 21))
        self.runwrfbutton.setObjectName("runwrfbutton")
        self.runwrfbutton.clicked.connect(self.runwrf)        # runwrf action
        self.ncviewbutton = QtWidgets.QPushButton(self.centralwidget)
        self.ncviewbutton.setGeometry(QtCore.QRect(400, 60, 80, 22))
        self.ncviewbutton.setObjectName("ncviewbutton")
        self.ncviewbutton.clicked.connect(self.ncview)        # ncviewbutton action
        self.wrfoptionsframe = QtWidgets.QFrame(self.centralwidget)
        self.wrfoptionsframe.setGeometry(QtCore.QRect(0, 0, 381, 191))
        self.wrfoptionsframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.wrfoptionsframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.wrfoptionsframe.setObjectName("wrfoptionsframe")
        self.formLayoutWidget = QtWidgets.QWidget(self.wrfoptionsframe)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 351, 201))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.startDate = QtWidgets.QDateTimeEdit(self.formLayoutWidget)
        self.startDate.setObjectName("startDate")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.startDate)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.endDate = QtWidgets.QDateTimeEdit(self.formLayoutWidget)
        self.endDate.setObjectName("endDate")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.endDate)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.length = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.length.setObjectName("length")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.length)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.latitude = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.latitude.setObjectName("latitude")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.latitude)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.longitude = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.longitude.setObjectName("longitude")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.longitude)
        self.physicsoptionsframe = QtWidgets.QFrame(self.centralwidget)
        self.physicsoptionsframe.setGeometry(QtCore.QRect(0, 200, 381, 621))
        self.physicsoptionsframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.physicsoptionsframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.physicsoptionsframe.setObjectName("physicsoptionsframe")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.physicsoptionsframe)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 361, 721))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_2)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.gridew = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.gridew.setObjectName("gridew")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.gridew)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.gridns = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.gridns.setPlaceholderText("")
        self.gridns.setObjectName("gridns")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.gridns)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.vertlevels = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.vertlevels.setObjectName("vertlevels")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.vertlevels)
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.domains = QtWidgets.QSpinBox(self.formLayoutWidget_2)
        self.domains.setObjectName("domains")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.domains)
        self.label_13 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.gridratio = QtWidgets.QDoubleSpinBox(self.formLayoutWidget_2)
        self.gridratio.setObjectName("gridratio")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.gridratio)
        self.label_14 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_14.setObjectName("label_14")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.gridspacing = QtWidgets.QDoubleSpinBox(self.formLayoutWidget_2)
        self.gridspacing.setObjectName("gridspacing")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.gridspacing)
        self.label_15 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_15.setObjectName("label_15")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.timestep = QtWidgets.QSpinBox(self.formLayoutWidget_2)
        self.timestep.setObjectName("timestep")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.timestep)
        self.label_16 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.wpsmapproj = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.wpsmapproj.setObjectName("wpsmapproj")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.wpsmapproj)
        self.label_17 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_17.setObjectName("label_17")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.label_18 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_18.setObjectName("label_18")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.label_19 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_19.setObjectName("label_19")
        self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.ncores = QtWidgets.QSpinBox(self.formLayoutWidget_2)
        self.ncores.setObjectName("ncores")
        self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.ncores)
        self.label_20 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_20.setObjectName("label_20")
        self.formLayout_2.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.history_interval = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.history_interval.setObjectName("history_interval")
        self.formLayout_2.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.history_interval)
        self.label_21 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_21.setObjectName("label_21")
        self.formLayout_2.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.phys_mp = QtWidgets.QSpinBox(self.formLayoutWidget_2)
        self.phys_mp.setObjectName("phys_mp")
        self.formLayout_2.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.phys_mp)
        self.label_22 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_22.setObjectName("label_22")
        self.formLayout_2.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.phys_rawl = QtWidgets.QSpinBox(self.formLayoutWidget_2)
        self.phys_rawl.setObjectName("phys_rawl")
        self.formLayout_2.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.phys_rawl)
        self.label_23 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_23.setObjectName("label_23")
        self.formLayout_2.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.label_23)
        self.phys_rasw = QtWidgets.QSpinBox(self.formLayoutWidget_2)
        self.phys_rasw.setObjectName("phys_rasw")
        self.formLayout_2.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.phys_rasw)
        self.label_24 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_24.setObjectName("label_24")
        self.formLayout_2.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.phys_cu = QtWidgets.QSpinBox(self.formLayoutWidget_2)
        self.phys_cu.setObjectName("phys_cu")
        self.formLayout_2.setWidget(16, QtWidgets.QFormLayout.FieldRole, self.phys_cu)
        self.label_25 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_25.setObjectName("label_25")
        self.formLayout_2.setWidget(17, QtWidgets.QFormLayout.LabelRole, self.label_25)
        self.phys_pbl = QtWidgets.QSpinBox(self.formLayoutWidget_2)
        self.phys_pbl.setObjectName("phys_pbl")
        self.formLayout_2.setWidget(17, QtWidgets.QFormLayout.FieldRole, self.phys_pbl)
        self.label_26 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_26.setObjectName("label_26")
        self.formLayout_2.setWidget(18, QtWidgets.QFormLayout.LabelRole, self.label_26)
        self.label_27 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_27.setObjectName("label_27")
        self.formLayout_2.setWidget(19, QtWidgets.QFormLayout.LabelRole, self.label_27)
        self.label_28 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_28.setObjectName("label_28")
        self.formLayout_2.setWidget(20, QtWidgets.QFormLayout.LabelRole, self.label_28)
        self.runshort = QtWidgets.QSpinBox(self.formLayoutWidget_2)
        self.runshort.setObjectName("runshort")
        self.formLayout_2.setWidget(20, QtWidgets.QFormLayout.FieldRole, self.runshort)
        self.phys_sfcc = QtWidgets.QSpinBox(self.formLayoutWidget_2)
        self.phys_sfcc.setObjectName("phys_sfcc")
        self.formLayout_2.setWidget(18, QtWidgets.QFormLayout.FieldRole, self.phys_sfcc)
        self.phys_urb = QtWidgets.QSpinBox(self.formLayoutWidget_2)
        self.phys_urb.setObjectName("phys_urb")
        self.formLayout_2.setWidget(19, QtWidgets.QFormLayout.FieldRole, self.phys_urb)
        self.sitefile_2 = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.sitefile_2.setObjectName("sitefile_2")
        self.sitefile_2.addItem("")
        self.sitefile_2.addItem("")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.sitefile_2)
        self.tslistfile_2 = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.tslistfile_2.setObjectName("tslistfile_2")
        self.tslistfile_2.addItem("")
        self.tslistfile_2.addItem("")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.tslistfile_2)
        self.moreoptionsframe = QtWidgets.QFrame(self.centralwidget)
        self.moreoptionsframe.setGeometry(QtCore.QRect(390, 470, 391, 351))
        self.moreoptionsframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.moreoptionsframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.moreoptionsframe.setObjectName("moreoptionsframe")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.moreoptionsframe)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 371, 28))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.moreoptionsframe)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(130, 40, 251, 22))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_33 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_3.addWidget(self.label_33)
        self.label_32 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_3.addWidget(self.label_32)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.moreoptionsframe)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(10, 70, 371, 22))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_40 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.label_40.setObjectName("label_40")
        self.horizontalLayout_7.addWidget(self.label_40)
        self.auxhist7true = QtWidgets.QRadioButton(self.horizontalLayoutWidget_7)
        self.auxhist7true.setText("")
        self.auxhist7true.setObjectName("auxhist7true")
        self.horizontalLayout_7.addWidget(self.auxhist7true)
        self.auxhist7false = QtWidgets.QRadioButton(self.horizontalLayoutWidget_7)
        self.auxhist7false.setText("")
        self.auxhist7false.setObjectName("auxhist7false")
        self.horizontalLayout_7.addWidget(self.auxhist7false)
        self.horizontalLayoutWidget_10 = QtWidgets.QWidget(self.moreoptionsframe)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(10, 90, 371, 22))
        self.horizontalLayoutWidget_10.setObjectName("horizontalLayoutWidget_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_41 = QtWidgets.QLabel(self.horizontalLayoutWidget_10)
        self.label_41.setObjectName("label_41")
        self.horizontalLayout_10.addWidget(self.label_41)
        self.auxhist2true = QtWidgets.QRadioButton(self.horizontalLayoutWidget_10)
        self.auxhist2true.setText("")
        self.auxhist2true.setObjectName("auxhist2true")
        self.horizontalLayout_10.addWidget(self.auxhist2true)
        self.auxhist2false = QtWidgets.QRadioButton(self.horizontalLayoutWidget_10)
        self.auxhist2false.setText("")
        self.auxhist2false.setObjectName("auxhist2false")
        self.horizontalLayout_10.addWidget(self.auxhist2false)
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.moreoptionsframe)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(10, 110, 371, 22))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_42 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        self.label_42.setObjectName("label_42")
        self.horizontalLayout_8.addWidget(self.label_42)
        self.feedbacktrue = QtWidgets.QRadioButton(self.horizontalLayoutWidget_8)
        self.feedbacktrue.setText("")
        self.feedbacktrue.setObjectName("feedbacktrue")
        self.horizontalLayout_8.addWidget(self.feedbacktrue)
        self.feedbackfalse = QtWidgets.QRadioButton(self.horizontalLayoutWidget_8)
        self.feedbackfalse.setText("")
        self.feedbackfalse.setObjectName("feedbackfalse")
        self.horizontalLayout_8.addWidget(self.feedbackfalse)
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.moreoptionsframe)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(10, 130, 371, 22))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_43 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.label_43.setObjectName("label_43")
        self.horizontalLayout_9.addWidget(self.label_43)
        self.nopreprocessingtrue = QtWidgets.QRadioButton(self.horizontalLayoutWidget_9)
        self.nopreprocessingtrue.setText("")
        self.nopreprocessingtrue.setObjectName("nopreprocessingtrue")
        self.horizontalLayout_9.addWidget(self.nopreprocessingtrue)
        self.nopreprocessingfalse = QtWidgets.QRadioButton(self.horizontalLayoutWidget_9)
        self.nopreprocessingfalse.setText("")
        self.nopreprocessingfalse.setObjectName("nopreprocessingfalse")
        self.horizontalLayout_9.addWidget(self.nopreprocessingfalse)
        self.horizontalLayoutWidget_11 = QtWidgets.QWidget(self.moreoptionsframe)
        self.horizontalLayoutWidget_11.setGeometry(QtCore.QRect(10, 150, 371, 22))
        self.horizontalLayoutWidget_11.setObjectName("horizontalLayoutWidget_11")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_11)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_44 = QtWidgets.QLabel(self.horizontalLayoutWidget_11)
        self.label_44.setObjectName("label_44")
        self.horizontalLayout_11.addWidget(self.label_44)
        self.norunwrftrue = QtWidgets.QRadioButton(self.horizontalLayoutWidget_11)
        self.norunwrftrue.setText("")
        self.norunwrftrue.setObjectName("norunwrftrue")
        self.horizontalLayout_11.addWidget(self.norunwrftrue)
        self.norunwrffalse = QtWidgets.QRadioButton(self.horizontalLayoutWidget_11)
        self.norunwrffalse.setText("")
        self.norunwrffalse.setObjectName("norunwrffalse")
        self.horizontalLayout_11.addWidget(self.norunwrffalse)
        self.horizontalLayoutWidget_12 = QtWidgets.QWidget(self.moreoptionsframe)
        self.horizontalLayoutWidget_12.setGeometry(QtCore.QRect(10, 170, 371, 22))
        self.horizontalLayoutWidget_12.setObjectName("horizontalLayoutWidget_12")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_12)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_45 = QtWidgets.QLabel(self.horizontalLayoutWidget_12)
        self.label_45.setObjectName("label_45")
        self.horizontalLayout_12.addWidget(self.label_45)
        self.isanalysistrue = QtWidgets.QRadioButton(self.horizontalLayoutWidget_12)
        self.isanalysistrue.setText("")
        self.isanalysistrue.setObjectName("isanalysistrue")
        self.horizontalLayout_12.addWidget(self.isanalysistrue)
        self.isanalysisfalse = QtWidgets.QRadioButton(self.horizontalLayoutWidget_12)
        self.isanalysisfalse.setText("")
        self.isanalysisfalse.setObjectName("isanalysisfalse")
        self.horizontalLayout_12.addWidget(self.isanalysisfalse)
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.moreoptionsframe)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 200, 371, 166))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_29 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_29.setObjectName("label_29")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_29)
        self.projectdir = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.projectdir.setObjectName("projectdir")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.projectdir)
        self.label_30 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_30.setObjectName("label_30")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_30)
        self.label_31 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_31.setObjectName("label_31")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_31)
        self.initialconditions = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.initialconditions.setObjectName("initialconditions")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.initialconditions)
        self.label_34 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_34.setObjectName("label_34")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_34)
        self.boundaryconditions = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.boundaryconditions.setObjectName("boundaryconditions")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.boundaryconditions)
        self.label_35 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_35.setObjectName("label_35")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_35)
        self.inputdata = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.inputdata.setObjectName("inputdata")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.inputdata)
        self.altftpserver = QtWidgets.QComboBox(self.formLayoutWidget_3)
        self.altftpserver.setObjectName("altftpserver")
        self.altftpserver.addItem("")
        self.altftpserver.addItem("")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.altftpserver)
        self.displayframe5 = QtWidgets.QFrame(self.centralwidget)
        self.displayframe5.setGeometry(QtCore.QRect(390, 100, 391, 351))
        self.displayframe5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.displayframe5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.displayframe5.setObjectName("displayframe5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 861, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.triggered.connect(self.openfile)          # open file
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        
        # Set Default values
        self.startDate.setDate(QDate(2017, 8, 12))
        self.endDate.setDate(QDate(2017, 8, 12))
        self.length.setValue(6)
        self.latitude.setText("29.434")
        self.longitude.setText("-98.499")
        self.gridew.setText("100")
        self.gridns.setText("100")
        self.vertlevels.setText("40")
        self.domains.setValue(3)
        self.gridratio.setValue(3)
        self.gridspacing.setValue(1.5)
        self.timestep.setValue(10)
        self.wpsmapproj.setText("lambert")
        self.ncores.setValue(2)
        self.history_interval.setText("40")
        self.phys_mp.setValue(17)
        self.phys_rawl.setValue(4)
        self.phys_rasw.setValue(4)
        self.phys_cu.setValue(0)
        self.phys_pbl.setValue(1)
        self.phys_sfcc.setValue(1)
        self.phys_urb.setValue(0)
        self.runshort.setValue(0)
        self.auxhist7false.setChecked(True)
        self.auxhist2false.setChecked(True)
        self.feedbackfalse.setChecked(True)
        self.nopreprocessingfalse.setChecked(True)
        self.norunwrffalse.setChecked(True)
        self.isanalysisfalse.setChecked(True)
        self.projectdir.setText("undefined")
        self.initialconditions.setText("GFS")
        self.boundaryconditions.setText("GFS")
        self.inputdata.setText("")


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.runwrfbutton.setText(_translate("MainWindow", "run WRF"))
        self.ncviewbutton.setText(_translate("MainWindow", "ncview"))
        self.label.setText(_translate("MainWindow", "WRF Options"))
        self.label_6.setText(_translate("MainWindow", "Start"))
        self.label_7.setText(_translate("MainWindow", "End"))
        self.label_8.setText(_translate("MainWindow", "Length"))
        self.label_9.setText(_translate("MainWindow", "Latitude"))
        self.label_11.setText(_translate("MainWindow", "Longitude"))
        self.label_2.setText(_translate("MainWindow", "Physics Options"))
        self.label_4.setText(_translate("MainWindow", "gridew"))
        self.label_5.setText(_translate("MainWindow", "gridns"))
        self.label_10.setText(_translate("MainWindow", "vertlevels"))
        self.label_12.setText(_translate("MainWindow", "domains"))
        self.label_13.setText(_translate("MainWindow", "gridratio"))
        self.label_14.setText(_translate("MainWindow", "gridspacing"))
        self.label_15.setText(_translate("MainWindow", "timestep"))
        self.label_16.setText(_translate("MainWindow", "wpsmapproj"))
        self.label_17.setText(_translate("MainWindow", "sitefile"))
        self.label_18.setText(_translate("MainWindow", "tslistfile"))
        self.label_19.setText(_translate("MainWindow", "ncores"))
        self.label_20.setText(_translate("MainWindow", "history_interval"))
        self.label_21.setText(_translate("MainWindow", "phys_mp"))
        self.label_22.setText(_translate("MainWindow", "phys_rawl"))
        self.label_23.setText(_translate("MainWindow", "phys_rasw"))
        self.label_24.setText(_translate("MainWindow", "phys_cu"))
        self.label_25.setText(_translate("MainWindow", "phys_pbl"))
        self.label_26.setText(_translate("MainWindow", "phys_sfcc"))
        self.label_27.setText(_translate("MainWindow", "phys_urb"))
        self.label_28.setText(_translate("MainWindow", "runshort"))
        self.sitefile_2.setItemText(0, _translate("MainWindow", "None"))
        self.sitefile_2.setItemText(1, _translate("MainWindow", "Something else"))
        self.tslistfile_2.setItemText(0, _translate("MainWindow", "None"))
        self.tslistfile_2.setItemText(1, _translate("MainWindow", "Something else"))
        self.label_3.setText(_translate("MainWindow", "More Options"))
        self.label_33.setText(_translate("MainWindow", "True"))
        self.label_32.setText(_translate("MainWindow", "False"))
        self.label_40.setText(_translate("MainWindow", "auxhist7"))
        self.label_41.setText(_translate("MainWindow", "auxhist2"))
        self.label_42.setText(_translate("MainWindow", "feedback"))
        self.label_43.setText(_translate("MainWindow", "nopreprocessing"))
        self.label_44.setText(_translate("MainWindow", "norunwrf"))
        self.label_45.setText(_translate("MainWindow", "is_analysis"))
        self.label_29.setText(_translate("MainWindow", "projectdir"))
        self.label_30.setText(_translate("MainWindow", "altftpserver"))
        self.label_31.setText(_translate("MainWindow", "initialConditions"))
        self.label_34.setText(_translate("MainWindow", "boundaryConditions"))
        self.label_35.setText(_translate("MainWindow", "InputData"))
        self.altftpserver.setItemText(0, _translate("MainWindow", "None"))
        self.altftpserver.setItemText(1, _translate("MainWindow", "Something else"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        
    # ncview button press
    def ncview(self):
        print('displaying ncview')
        # os.system('ncview /opt/deepthunder/data/sample.nc')
        subprocess.call('ncview /opt/deepthunder/data/sample.nc', shell=True)
        
    #run wrf button press
    def runwrf(self):
        print('running wrf')
        print(self.length.text())

        '''
        start="2017-08-12"
        end="2017-08-12"
        length=6
        lat=29.434
        long=-98.499
        
        ngridew=100
        ngridns=100
        nvertlevels=40
        ndomains=3
        gridratio=3
        gridspacinginner=1.5
        timestep=10
        wpsmapproj='lambert'
        sitefile=None
        tslistfile=None
        ncores=2
        history_interval=[60]
        phys_mp=17
        phys_ralw=4
        phys_rasw=4
        phys_cu=0
        phys_pbl=1
        phys_sfcc=1
        phys_sfc=2
        phys_urb=0
        runshort=0
        auxhist7=False
        auxhist2=False
        feedback=False
        adaptivets=False
        nopreprocess=False
        projectdir="undefined"
        norunwrf=False
        is_analysis=False
        altftpserver=None
        initialConditions=['GFS']
        boundaryConditions=['GFS']
        inputData=[]
        
        # create date objects
        hour_start = 0
        #get the start date expecting it to be in the format YYYY-MM-DD
        date_start = datetime.strptime(str(start)+':'+str(hour_start),'%Y-%m-%d:%H')
        #get the end date expecting it to be in the format YYYY-MM-DD
        date_end = datetime.strptime(end+':'+str(hour_start),'%Y-%m-%d:%H')
        #calculate the difference between the two dates.
        date_delta = date_end - date_start
        forecast_length = int(length)

        #Note print off what is going on to aid in debugging
        print("Running "+ str(date_delta.days+1) +" individual simulation each     being "\
             +str(forecast_length) +" hours in length. UTC start is "+ str(hour_start))

        # loop over days to create forecasts
        for i in range(date_delta.days + 1):
  
            # current date of loop
            date_i = date_start + td(days=i)
                
            stevedore_instance = stevedore.Stevedore(date_i,
                                        forecast_length, lat, long,
                                        ncores=int(ncores),
                                        ndomains=int(ndomains),
                                        timestep=int(timestep),
                                        gridratio=int(gridratio),
                                        gridspacinginner=float(gridspacinginner),
                                        ngridew=ngridew,
                                        ngridns=ngridns,
                                        nvertlevels=int(nvertlevels),
                                        phys_mp=int(phys_mp),
                                        phys_ralw=int(phys_ralw),
                                        phys_rasw=int(phys_rasw),
                                        phys_cu=phys_cu,
                                        phys_pbl=int(phys_pbl),
                                        phys_sfcc=int(phys_sfcc),
                                        phys_sfc=int(phys_sfc),
                                        phys_urb=int(phys_urb),
                                        wps_map_proj=wpsmapproj,
                                        runshort=int(runshort),
                                        auxhist7=auxhist7,
                                        auxhist2=auxhist2,
                                        feedback=feedback,
                                        adaptivets=adaptivets,
                                        projectdir=projectdir,
                                        norunwrf=norunwrf,
                                        is_analysis=is_analysis,
                                        altftpserver=altftpserver,
                                        initialConditions=initialConditions,
                                        boundaryConditions=boundaryConditions,
                                        inputData=inputData,
                                        tsfile=tslistfile,
                                        history_interval=history_interval)


        # run wrf
        stevedore_instance.run_WRF()
        '''
        
    # open button press
    #def openfile(self, event=None):
     #   self.filename = filedialog.askopenfilename(initialdir = "/opt/deepthunder/data", title = "Select File", filetypes = (('NetCDF4','*.nc'),('all files','*.*')))

    def openfile(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "/opt/deepthunder/data", "All Files (*)", "","")
        print('open')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
