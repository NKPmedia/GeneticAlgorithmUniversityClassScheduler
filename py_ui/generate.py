# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'generate.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(835, 549)
        Dialog.setMaximumSize(QtCore.QSize(1500, 553))
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.cmbSection = QtWidgets.QComboBox(self.groupBox_3)
        self.cmbSection.setObjectName("cmbSection")
        self.cmbSection.addItem("")
        self.cmbSection.addItem("")
        self.cmbSection.addItem("")
        self.cmbSection.addItem("")
        self.cmbSection.addItem("")
        self.horizontalLayout_5.addWidget(self.cmbSection)
        self.chkPreview = QtWidgets.QCheckBox(self.groupBox_3)
        self.chkPreview.setObjectName("chkPreview")
        self.horizontalLayout_5.addWidget(self.chkPreview)
        self.horizontalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnPause = QtWidgets.QPushButton(self.groupBox_4)
        self.btnPause.setObjectName("btnPause")
        self.horizontalLayout_4.addWidget(self.btnPause)
        self.btnStop = QtWidgets.QPushButton(self.groupBox_4)
        self.btnStop.setObjectName("btnStop")
        self.horizontalLayout_4.addWidget(self.btnStop)
        self.horizontalLayout_2.addWidget(self.groupBox_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.boxGen = QtWidgets.QGroupBox(Dialog)
        self.boxGen.setObjectName("boxGen")
        self.gridLayout = QtWidgets.QGridLayout(self.boxGen)
        self.gridLayout.setObjectName("gridLayout")
        self.lblFitness = QtWidgets.QLabel(self.boxGen)
        self.lblFitness.setObjectName("lblFitness")
        self.gridLayout.addWidget(self.lblFitness, 2, 0, 1, 1)
        self.lblPreviousFitness = QtWidgets.QLabel(self.boxGen)
        self.lblPreviousFitness.setObjectName("lblPreviousFitness")
        self.gridLayout.addWidget(self.lblPreviousFitness, 2, 1, 1, 1)
        self.lblPopulation = QtWidgets.QLabel(self.boxGen)
        self.lblPopulation.setObjectName("lblPopulation")
        self.gridLayout.addWidget(self.lblPopulation, 1, 0, 1, 1)
        self.lblMutation = QtWidgets.QLabel(self.boxGen)
        self.lblMutation.setObjectName("lblMutation")
        self.gridLayout.addWidget(self.lblMutation, 1, 1, 1, 1)
        self.lblHighestFitness = QtWidgets.QLabel(self.boxGen)
        self.lblHighestFitness.setObjectName("lblHighestFitness")
        self.gridLayout.addWidget(self.lblHighestFitness, 3, 0, 1, 1)
        self.lblLowestFitness = QtWidgets.QLabel(self.boxGen)
        self.lblLowestFitness.setObjectName("lblLowestFitness")
        self.gridLayout.addWidget(self.lblLowestFitness, 3, 1, 1, 1)
        self.horizontalLayout.addWidget(self.boxGen)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lblCPU = QtWidgets.QLabel(self.groupBox)
        self.lblCPU.setObjectName("lblCPU")
        self.gridLayout_2.addWidget(self.lblCPU, 2, 0, 1, 1)
        self.lblTime = QtWidgets.QLabel(self.groupBox)
        self.lblTime.setObjectName("lblTime")
        self.gridLayout_2.addWidget(self.lblTime, 0, 0, 1, 2)
        self.lblMemory = QtWidgets.QLabel(self.groupBox)
        self.lblMemory.setObjectName("lblMemory")
        self.gridLayout_2.addWidget(self.lblMemory, 2, 1, 1, 1)
        self.lblStatus = QtWidgets.QLabel(self.groupBox)
        self.lblStatus.setObjectName("lblStatus")
        self.gridLayout_2.addWidget(self.lblStatus, 1, 0, 1, 2)
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.tableSchedule = QtWidgets.QTableView(Dialog)
        self.tableSchedule.setObjectName("tableSchedule")
        self.tableSchedule.horizontalHeader().setDefaultSectionSize(50)
        self.tableSchedule.horizontalHeader().setMinimumSectionSize(10)
        self.verticalLayout_5.addWidget(self.tableSchedule)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Generate"))
        self.groupBox_3.setTitle(_translate("Dialog", "Preview"))
        self.cmbSection.setItemText(0, _translate("Dialog", "Section 1"))
        self.cmbSection.setItemText(1, _translate("Dialog", "Section 2"))
        self.cmbSection.setItemText(2, _translate("Dialog", "Section 3"))
        self.cmbSection.setItemText(3, _translate("Dialog", "Section 4"))
        self.cmbSection.setItemText(4, _translate("Dialog", "Section 5"))
        self.chkPreview.setText(_translate("Dialog", "Disable Preview"))
        self.groupBox_4.setTitle(_translate("Dialog", "Operation"))
        self.btnPause.setText(_translate("Dialog", "Pause Generation"))
        self.btnStop.setText(_translate("Dialog", "Stop Generation"))
        self.boxGen.setTitle(_translate("Dialog", "Generation N"))
        self.lblFitness.setText(_translate("Dialog", "Average Fitness:"))
        self.lblPreviousFitness.setText(_translate("Dialog", "Previous Average Fitness:"))
        self.lblPopulation.setText(_translate("Dialog", "Population:"))
        self.lblMutation.setText(_translate("Dialog", "Mutation Rate:"))
        self.lblHighestFitness.setText(_translate("Dialog", "Highest Fitness:"))
        self.lblLowestFitness.setText(_translate("Dialog", "Lowest Fitness:"))
        self.groupBox.setTitle(_translate("Dialog", "System"))
        self.lblCPU.setText(_translate("Dialog", "CPU Usage:"))
        self.lblTime.setText(_translate("Dialog", "Elapsed Time:"))
        self.lblMemory.setText(_translate("Dialog", "Memory Usage:"))
        self.lblStatus.setText(_translate("Dialog", "Status:"))
