import pandas as pd
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt

from components import Settings, TableModel, Utilities
import json

from components.scenario import Section
from scripts.htest import MultiIndexHeaderView, HorizontalHeaderDataRole, VerticalHeaderDataRole


class ScheduleParser:
    # Section / Room View
    # Subject Name + Instructor
    # Instructor View
    # Subject Name + Instructor + Section

    # table = QTableView, data = []
    def __init__(self, scenario, table, data):
        self.scenario = scenario
        self.table = table
        self.settings = settings = Settings.getSettings()
        self.build_model()
        MultiIndexHeaderView(Qt.Horizontal, table)
        MultiIndexHeaderView(Qt.Vertical, table)
        table.horizontalHeader().setSectionsMovable(True)  # reorder DataFrame columns manually

        # Set data
        table.setModel(self.model)
        table.resizeColumnsToContents()
        table.resizeRowsToContents()
        table.setFocusPolicy(QtCore.Qt.NoFocus)
        table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.parseData(data)

    # data = [{'color': None, 'text': '', 'instances': [[day, startingTS, endingTS]]}]
    def parseData(self, data):
        view = self.table
        model = self.model
        for entry in data:
            entry['color'] = Utilities.colorGenerator()
            for instance in entry['instances']:
                index = model.index(instance[1], instance[0])
                view.setSpan(instance[1], instance[0], instance[2] - instance[1], 1)
                item = QtGui.QStandardItem(entry['text'])
                item.setBackground(QtGui.QBrush(QtGui.QColor(*entry['color'])))
                item.setForeground(QtGui.QBrush(QtGui.QColor(*Utilities.textColor(entry['color']))))
                model.setData(index, item)

    def subjectGenerator(self):
        print(self.settings['starting_time'])

    def build_model(self):
        days = ['Mo', 'Di', 'Mi', 'Do', 'Fr']
        with open('timeslots.json') as json_file:
            self.timeslots = timeslots = json.load(json_file)['timeslots']
        col_header = []
        total_timeslots = 0
        for day in days:
            for slot in timeslots[self.settings['starting_time']:self.settings['ending_time'] + 1]:
                col_header.append(f"{day}_{slot}")
                total_timeslots = total_timeslots + 1
        section: Section
        row_header = []
        temporaryData = []
        for id, section in self.scenario.sections.items():
            row_header.append(f"{section.name}")
            temp = ["" for i in range(total_timeslots)]
            temporaryData.append(temp)
        header = [col_header, row_header]
        self.model = ScheduleParserModel(header, temporaryData)


class ScheduleParserModel(TableModel.TableModel):
    def __init__(self, header, table_data):
        super().__init__(header, table_data)

    def setData(self, index, value, role=None):
        if not index.isValid():
            return False
        elif role is None:
            self.table_data[index.row()][index.column()] = value
        self.dataChanged.emit(index, index)
        return True

    def data(self, index, role):
        row, col = index.row(), index.column()
        if role == QtCore.Qt.TextAlignmentRole:
            return QtCore.Qt.AlignCenter
        elif role in (Qt.DisplayRole, Qt.ToolTipRole):
            return "Test" #QtCore.QVariant()
        elif role in (HorizontalHeaderDataRole, VerticalHeaderDataRole):
            hm = QtGui.QStandardItemModel()
            hm.appendRow(QtGui.QStandardItem("Test2"))
            return hm
        #return self.table_data[index.row()][index.column()].text()
