from components import Database as db
import json

from components.scenario import Scenario, Subject, Section, Instructor


class ScenarioComposer:
    def __init__(self):
        self.conn = db.getConnection()
        self.cursor = self.conn.cursor()

    def getInstructors(self):
        self.cursor.execute('SELECT id, name, hours, schedule FROM instructors WHERE active = 1')
        instructors = {}
        for idx, col in enumerate(self.cursor.fetchall()):
            instructors[col[0]] = Instructor(col[0], col[1], col[2], col[3])
        return instructors

    def getRooms(self):
        self.cursor.execute('SELECT id, name, type, schedule FROM rooms WHERE active = 1')
        instructors = {}
        for idx, col in enumerate(self.cursor.fetchall()):
            instructors[col[0]] = col
        return instructors

    def getSubjects(self):
        self.cursor.execute('SELECT id, name, hours, code, description, instructors, subject_type, withTest FROM subjects')
        subjects = {}
        for idx, col in enumerate(self.cursor.fetchall()):
            subjects[col[0]] = Subject(col[0], col[1], col[2], col[3], json.loads(col[5]), col[6], col[7])
        return subjects

    def getSections(self):
        self.cursor.execute('SELECT id, name, schedule, section_type FROM sections WHERE active = 1')
        sections = {}
        for idx, col in enumerate(self.cursor.fetchall()):
            sections[col[0]] = Section(col[0], col[1], col[1], col[3])
        return sections

    def listToDictionary(self, toDict):
        return {entry[0]: list(entry[1:]) for entry in toDict}

    def jsonToList(self, dictionary, index):
        for key, value in dictionary.items():
            dictionary[key][index] = json.loads(value[index])
        return dictionary

    def stringToInt(self, dictionary, index):
        for key, value in dictionary.items():
            dictionary[key][index] = list(map(int, value[index]))
        return dictionary

    def closeConnection(self):
        self.conn.commit()
        self.conn.close()

    def getScenarioData(self):
        data = {
            'instructors': self.getInstructors(),
            'sections': self.getSections(),
            'subjects': self.getSubjects(),
            'rooms': self.getRooms()
        }
        scenario = Scenario(data)
        self.closeConnection()
        return scenario
