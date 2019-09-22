import copy

from components import Settings


class Chromosome:
    # data = {
    #     sections: {
    #         id: {
    #             details: {
    #                 subject: [roomId,
    #                   instructorId,
    #                   [day / s],
    #                   startingTS,
    #                   length
    #                 ]
    #             },
    #             schedule: [days]
    #         }
    #     },
    #     instructors && rooms: {
    #         id: [
    #             [days] // Timeslots
    #             [1, None, 1, None, 1, False] // Example
    #             // None = Vacant, False = Unavailable
    #         ]
    #     },
    #     unplaced: {
    #         'sections': {
    #             id: [] // Section ID and unplaced subjects
    #         }
    #     }
    # }

    def __init__(self, data):
        self.fitness = 0
        self.fitnessDetails = []
        self.data = {
            'sections': {},
            'instructors': {},
            'rooms': {},
            'unplaced': {
                'sections': {}
            }
        }
        self.rawData = data
        self.settings = Settings.getSettings()
        self.buildChromosome()

    def buildChromosome(self):
        rawData = self.rawData
        # {id: {details: [subject: []], schedule: [days]}}
        sections = rawData['sections']
        for section in sections:
            self.data['sections'][section] = {'details': {}, 'schedule': []}
            self.data['sections'][section]['details'] = {key: [] for key in sections[section][2]}
            sectionTimetable = []
            for timeslotRow in sections[section][1]:
                sectionTimetable.append([None if day == 'Available' else False for day in timeslotRow])
            self.data['sections'][section]['schedule'] = sectionTimetable
            self.data['unplaced']['sections'][section] = []
        # {id: [days]}
        instructors = rawData['instructors']
        for instructor in instructors:
            instructorTimetable = []
            for timeslotRow in instructors[instructor][2]:
                instructorTimetable.append([None if day == 'Available' else False for day in timeslotRow])
            self.data['instructors'][instructor] = instructorTimetable
        # {id: [days]}
        rooms = rawData['rooms']
        for room in rooms:
            roomTimetable = []
            for timeslotRow in rooms[room][2]:
                roomTimetable.append([None if day == 'Available' else False for day in timeslotRow])
            self.data['rooms'][room] = roomTimetable

    # [roomId, [sectionId], subjectId, instructorID, [day/s], startingTS, length(, sharingId)]
    def insertSchedule(self, schedule):
        # Validate schedule details
        isValid = self.validateSchedule(copy.deepcopy(schedule))
        if isValid is not True:
            return isValid
        data = self.data
        # [roomId, instructorId, [day/s], startingTS, length]
        subjectDetails = [schedule[0], schedule[3], schedule[4], schedule[5], schedule[6]]
        # Check if schedule is for sharing
        if len(schedule) > 7:
            data['sharings'][schedule[-1]] = subjectDetails
        # Insert details into section data
        for section in schedule[1]:
            data['sections'][section]['details'][schedule[2]] = subjectDetails
        # Update instructor and room timetable
        for timeslot in range(schedule[5], schedule[5] + schedule[6]):
            for day in schedule[4]:
                if schedule[3]:
                    data['instructors'][schedule[3]][timeslot][day] = schedule[1]
                data['rooms'][schedule[0]][timeslot][day] = schedule[1]
        # False signifies no error in insertion
        return False

    def validateSchedule(self, schedule):
        if not self.isRoomTimeslotAvailable(schedule):
            return 1
        if not self.isInstructorTimeslotAvailable(schedule):
            return 2
        if not self.isSectionTimeslotAvailable(schedule):
            return 3
        return True

    def isRoomTimeslotAvailable(self, schedule):
        room = self.data['rooms'][schedule[0]]
        for timeslotRow in range(schedule[5], schedule[5] + schedule[6]):
            for day in schedule[4]:
                if room[timeslotRow][day] is not None:
                    return False
        return True

    def isSectionTimeslotAvailable(self, schedule):
        rooms = self.data['rooms']
        sections = self.data['sections']
        # Check for each room if on the given subject range, the section has class
        for room in rooms:
            for timeslotRow in range(schedule[5], schedule[5] + schedule[6]):
                for day in schedule[4]:
                    roomDayTimeslot = rooms[room][timeslotRow][day]
                    # Check if timeslot is blank
                    if roomDayTimeslot is None:
                        continue
                    # Check if section is in timeslot
                    for section in schedule[1]:
                        if section in roomDayTimeslot:
                            return False
        # Check for section unavailable times
        for section in schedule[1]:
            for timeslotRow in range(schedule[5], schedule[5] + schedule[6]):
                for day in schedule[4]:
                    if sections[section]['schedule'][timeslotRow][day] is not None:
                        return False
        return True

    def isInstructorTimeslotAvailable(self, schedule):
        # Pass if no instructor is set
        if not schedule[3]:
            return True
        instructor = self.data['instructors'][schedule[3]]
        for timeslotRow in range(schedule[5], schedule[5] + schedule[6]):
            for day in schedule[4]:
                if instructor[timeslotRow][day] is not None:
                    return False
        # Check if instructor can still teach
        maxLoad = self.rawData['instructors'][schedule[3]][1] * 2
        for timeslotRow in instructor:
            for day in timeslotRow:
                if day:
                    maxLoad -= 1
        if maxLoad < 0:
            return False
        return True