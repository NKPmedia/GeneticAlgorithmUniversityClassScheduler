from PyQt5 import QtWidgets, QtGui
from components import Database as db, Timetable
from py_ui import section as Parent
import json


class Section:
    def __init__(self, id):
        self.id = id
        self.dialog = dialog = QtWidgets.QDialog()
        # From the qt_ui generated UI
        self.parent = parent = Parent.Ui_Dialog()
        parent.setupUi(dialog)
        if id:
            self.fillForm()
        else:
            # Create new instance of timetable
            self.table = Timetable.Timetable(parent.tableSchedule)
        self.setupSubjects()
        parent.btnFinish.clicked.connect(self.finish)
        parent.btnCancel.clicked.connect(self.dialog.close)
        dialog.exec_()

    def setupSubjects(self):
        # Setup subjects tree view
        self.tree = tree = self.parent.treeSubjects
        self.model = model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderLabels(['ID', 'Available', 'Subject Code', 'Subject Name'])
        tree.setModel(model)
        tree.setColumnHidden(0, True)
        tree.setColumnHidden(5, True)
        # Populate tree with values
        conn = db.getConnection()
        cursor = conn.cursor()
        # Get subjects for listing
        cursor.execute('SELECT id, name, code FROM subjects')
        subjects = cursor.fetchall()
        # Subjects that the current section have
        currentSubjects = []
        if self.id:
            cursor.execute('SELECT subjects FROM sections WHERE id = ?', [self.id])
            # Convert result into list of int
            currentSubjects = list(map(lambda id: int(id), json.loads(cursor.fetchall()[0][0])))
            # Get section names
            # {id: name}
            sectionNames = []
            cursor.execute('SELECT id, name FROM sections WHERE active = 1')
            sectionNames = dict(cursor.fetchall())
        conn.close()
        for subject in subjects:
            subjectId = QtGui.QStandardItem(str(subject[0]))
            subjectId.setEditable(False)
            availability = QtGui.QStandardItem()
            availability.setCheckable(True)
            availability.setEditable(False)
            availability.setCheckState(2 if subject[0] in currentSubjects else 0)
            code = QtGui.QStandardItem(subject[2])
            code.setEditable(False)
            name = QtGui.QStandardItem(subject[1])
            name.setEditable(False)
            model.appendRow([subjectId, availability, code, name])

    def fillForm(self):
        conn = db.getConnection()
        cursor = conn.cursor()
        cursor.execute('SELECT name, schedule FROM sections WHERE id = ?', [self.id])
        result = cursor.fetchone()
        conn.close()
        self.parent.lineEditName.setText(str(result[0]))
        self.table = Timetable.Timetable(self.parent.tableSchedule, json.loads(result[1]))

    def finish(self):
        if not self.parent.lineEditName.text():
            return False
        name = self.parent.lineEditName.text()
        schedule = json.dumps(self.table.getData())
        subjects = []
        for row in range(self.model.rowCount()):
            if self.model.item(row, 1).checkState() == 2:
                subjects.append(self.model.item(row, 0).text())
        subjects = json.dumps(subjects)
        conn = db.getConnection()
        cursor = conn.cursor()
        if self.id:
            cursor.execute('UPDATE sections SET name = ?, schedule = ?, subjects = ?WHERE id = ?',
                           [name, schedule, subjects, self.id])
        else:
            cursor.execute('INSERT INTO sections (name, schedule, subjects) VALUES (?, ?, ?, ?)',
                           [name, schedule, subjects])
        conn.commit()
        conn.close()
        self.dialog.close()


class Tree:
    def __init__(self, tree):
        self.tree = tree
        self.model = model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderLabels(['ID', 'Available', 'Name', 'Operation'])
        tree.setModel(model)
        tree.setColumnHidden(0, True)
        model.itemChanged.connect(lambda item: self.toggleAvailability(item))
        self.display()

    def toggleAvailability(self, item):
        id = self.model.data(self.model.index(item.row(), 0))
        newValue = 1 if item.checkState() == 2 else 0
        conn = db.getConnection()
        cursor = conn.cursor()
        cursor.execute('UPDATE sections SET active = ?  WHERE id = ?', [newValue, id])
        conn.commit()
        conn.close()

    def display(self):
        self.model.removeRows(0, self.model.rowCount())
        conn = db.getConnection()
        cursor = conn.cursor()
        cursor.execute('SELECT id, active, name FROM sections')
        result = cursor.fetchall()
        conn.close()
        for instr in result:
            id = QtGui.QStandardItem(str(instr[0]))
            id.setEditable(False)
            availability = QtGui.QStandardItem()
            availability.setCheckable(True)
            availability.setCheckState(2 if instr[1] == 1 else 0)
            availability.setEditable(False)
            name = QtGui.QStandardItem(instr[2])
            name.setEditable(False)
            edit = QtGui.QStandardItem()
            edit.setEditable(False)
            self.model.appendRow([id, availability, name, edit])
            frameEdit = QtWidgets.QFrame()
            btnEdit = QtWidgets.QPushButton('Edit', frameEdit)
            btnEdit.clicked.connect(lambda state, id=instr[0]: self.edit(id))
            btnDelete = QtWidgets.QPushButton('Delete', frameEdit)
            btnDelete.clicked.connect(lambda state, id=instr[0]: self.delete(id))
            frameLayout = QtWidgets.QHBoxLayout(frameEdit)
            frameLayout.setContentsMargins(0, 0, 0, 0)
            frameLayout.addWidget(btnEdit)
            frameLayout.addWidget(btnDelete)
            self.tree.setIndexWidget(edit.index(), frameEdit)

    def edit(self, id):
        Section(id)
        self.display()

    def delete(self, id):
        confirm = QtWidgets.QMessageBox()
        confirm.setIcon(QtWidgets.QMessageBox.Warning)
        confirm.setText('Are you sure you want to delete this entry?')
        confirm.setWindowTitle('Confirm Delete')
        confirm.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        result = confirm.exec_()
        if result == 16384:
            conn = db.getConnection()
            cursor = conn.cursor()
            cursor.execute('DELETE FROM sections WHERE id = ?', [id])
            conn.commit()
            conn.close()
            self.display()
