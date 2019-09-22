import random

import numpy as np
from components import Settings
from components.scenario import Lesson


class Chromosome:
    #data: day x hour x room = lesson_id

    def __init__(self, scenario):
        self.scenario = scenario
        self.settings = Settings.getSettings()
        self.init_empty_data()
        self.genrate_random_timetable()

    @classmethod
    def create(cls, scenario):
        return cls(scenario)


    def init_empty_data(self):
        self.days = 5
        self.hours = 7
        self.rooms = 3
        self.data = np.full((self.days, self.hours, self.rooms), -1, dtype=np.int16)
        pass

    def genrate_random_timetable(self):
        for id, lesson in enumerate(self.scenario.lessons):
            placed = False
            while not placed:
                r_day = random.randint(0, self.days - 1)
                r_hour = random.randint(0, self.hours - 1)
                r_room = random.randint(0, self.rooms - 1)

                if self.data[r_day, r_hour, r_room] == -1:
                    self.data[r_day, r_hour, r_room] = id
                    placed = True

    def get_placed_subject_list(self):
        subject = {}
        for day in range(self.days):
            for hour in range(self.hours):
                for room in range(self.rooms):
                    lesson_id = self.data[day, hour, room]
                    if lesson_id != -1:
                        lesson: Lesson = self.scenario.lessons[lesson_id]
                        subject_id = lesson.subject.id
                        if lesson.subject.id not in subject:
                            subject[subject_id] = {}
                            subject[subject_id]["places"] = []
                            subject[subject_id]["name"] = subject
                        subject[subject_id]["places"].append([day, hour, room])