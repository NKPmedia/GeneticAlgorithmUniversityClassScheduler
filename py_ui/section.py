# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'section.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(716, 553)
        Dialog.setMinimumSize(QtCore.QSize(716, 553))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 712, 549))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(-1, 9, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEditName = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditName.setObjectName("lineEditName")
        self.gridLayout.addWidget(self.lineEditName, 1, 1, 1, 1)
        self.lblName = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lblName.setObjectName("lblName")
        self.gridLayout.addWidget(self.lblName, 1, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.treeSubjects = QtWidgets.QTreeView(self.scrollAreaWidgetContents)
        self.treeSubjects.setMinimumSize(QtCore.QSize(0, 200))
        self.treeSubjects.setHeaderHidden(False)
        self.treeSubjects.setObjectName("treeSubjects")
        self.verticalLayout.addWidget(self.treeSubjects)
        self.tableSchedule = QtWidgets.QTableView(self.scrollAreaWidgetContents)
        self.tableSchedule.setMinimumSize(QtCore.QSize(0, 180))
        self.tableSchedule.setObjectName("tableSchedule")
        self.verticalLayout.addWidget(self.tableSchedule)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnFinish = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btnFinish.setObjectName("btnFinish")
        self.horizontalLayout_2.addWidget(self.btnFinish)
        self.btnCancel = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout_2.addWidget(self.btnCancel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lblName.setText(_translate("Dialog", "Name"))
        self.comboBox.setItemText(0, _translate("Dialog", "A"))
        self.comboBox.setItemText(1, _translate("Dialog", "B"))
        self.comboBox.setItemText(2, _translate("Dialog", "C"))
        self.label.setText(_translate("Dialog", "Kursart"))
        self.btnFinish.setText(_translate("Dialog", "Finish"))
        self.btnCancel.setText(_translate("Dialog", "Cancel"))
