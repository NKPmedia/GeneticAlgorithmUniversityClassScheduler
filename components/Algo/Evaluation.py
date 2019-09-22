import copy
import itertools


class Evaluation():
    # Evaluation weight depends on settings
    @staticmethod
    def evaluateAll(self, chromosome):
        subjectPlacement = self.evaluateSubjectPlacements(chromosome)
        lunchBreak = self.evaluateLunchBreak(chromosome) if self.settings['lunchbreak'] else 100
        studentRest = self.evaluateStudentRest(chromosome)
        instructorRest = self.evaluateInstructorRest(chromosome)
        idleTime = self.evaluateStudentIdleTime(chromosome)
        meetingPattern = self.evaluateMeetingPattern(chromosome)
        instructorLoad = self.evaluateInstructorLoad(chromosome)
        chromosome.fitnessDetails = copy.deepcopy([subjectPlacement, lunchBreak, studentRest, instructorRest, idleTime,
                                                   meetingPattern, instructorLoad])
        matrix = self.settings['evaluation_matrix']
        return round(
            (subjectPlacement * matrix['subject_placement'] / 100) +
            (lunchBreak * matrix['lunch_break'] / 100) +
            (studentRest * matrix['student_rest'] / 100) +
            (instructorRest * matrix['instructor_rest'] / 100) +
            (idleTime * matrix['idle_time'] / 100) +
            (meetingPattern * matrix['meeting_pattern'] / 100) +
            (instructorLoad * matrix['instructor_load'] / 100),
            2
        )

    # = ((subjects - unplacedSubjects) / subjects) * 100
    @staticmethod
    def evaluateSubjectPlacements(self, chromosome):
        sections = copy.deepcopy({key: value[2] for key, value in self.data['sections'].items()})
        sharings = self.data['sharings']
        chromosomeUnplacedData = chromosome.data['unplaced']
        # Number of subjects that are in sharing
        sharingSubjects = 0
        # Remove section subjects that are shared
        for sharing in sharings.values():
            # Sharing subjects is increased based on number of sections sharing the subject
            sharingSubjects += len(sharing[1])
            for section in sharing[1]:
                sections[section].remove(sharing[0])
        # Combined list of section subjects
        sectionSubjects = len(list(itertools.chain.from_iterable(sections.values())))
        # Combined list of subjects
        totalSubjects = sectionSubjects + sharingSubjects
        # Number of shared subjects that are not placed
        unplacedSharingSubjects = 0
        for sharing in chromosomeUnplacedData['sharings']:
            # Sharing subjects is increased based on number of sections sharing the subject
            unplacedSharingSubjects += len(sharings[sharing][1])
        # Length of unplaced section subjects
        unplacedSectionSubjects = len(list(itertools.chain.from_iterable(chromosomeUnplacedData['sections'].values())))
        totalUnplacedSubjects = unplacedSharingSubjects + unplacedSectionSubjects
        return round(((totalSubjects - totalUnplacedSubjects) / totalSubjects) * 100, 2)

    # = ((instructorTeachingDays - noRestDays) / instructorTeachingDays) * 100
    @staticmethod
    def evaluateInstructorRest(self, chromosome):
        instructorTeachingDays = 0
        noRestDays = 0
        for instructor in chromosome.data['instructors'].values():
            # Instructor week
            week = {day: [] for day in range(6)}
            for timeslot, timeslotRow in enumerate(instructor):
                for day, value in enumerate(timeslotRow):
                    # Add timeslot to instructor week if teaching
                    if value:
                        week[day].append(timeslot)
            for day in week.values():
                if not len(day):
                    continue
                instructorTeachingDays += 1
                if len(day) < 6:
                    continue
                hasViolated = False
                # Steps of how many three hours per day a section has (Increments of 30 minutes)
                for threeHours in range(6, len(day) + 1):
                    if hasViolated:
                        continue
                    # Compare consecutive timeslot to section's day timeslot
                    if [timeslot for timeslot in range(day[threeHours - 6], day[threeHours - 6] + 6)] == day[
                                                                                                         threeHours - 6: threeHours]:
                        hasViolated = True
                        noRestDays += 1
        if not instructorTeachingDays:
            return 100.00
        return round(((instructorTeachingDays - noRestDays) / instructorTeachingDays) * 100, 2)

    # = ((placedSubjects - badPattern) / placedSubjects) * 100
    @staticmethod
    def evaluateMeetingPattern(self, chromosome):
        placedSubjects = 0
        badPattern = 0
        for section in chromosome.data['sections'].values():
            for subject in section['details'].values():
                if not len(subject) or len(subject[2]) == 1:
                    continue
                placedSubjects += 1
                # Check if subject has unusual pattern
                if subject[2] not in [[0, 2, 4], [1, 3]]:
                    badPattern += 1
        return round(((placedSubjects - badPattern) / placedSubjects) * 100, 2)

    @staticmethod
    def evaluateInstructorLoad(self, chromosome):
        activeInstructors = {}
        activeSubjects = []
        # Get list of active subjects
        for section in self.data['sections'].values():
            activeSubjects += section[2]
        subjects = self.data['subjects']
        sharings = self.data['sharings']
        # Get list of active instructors and their potential load
        for subject in activeSubjects:
            # Exclude subjects that have less than 1 candidate instructor
            if len(subjects[subject][4]) <= 1:
                continue
            for instructor in subjects[subject][4]:
                if instructor not in activeInstructors.keys():
                    activeInstructors[instructor] = [0, 0]
                activeInstructors[instructor][0] += int(subjects[subject][1] / .5)
        # Remove load from instructors that is duplicated due to sharing
        for sharing in sharings.values():
            subject = subjects[sharing[0]]
            if len(subject[4]) <= 1:
                continue
            for instructor in subject[4]:
                activeInstructors[instructor][0] -= int(subject[1] / .5) * (len(sharing[1]) - 1)
        # Fill up active instructors with actual load
        for instructor, details in chromosome.data['instructors'].items():
            for timeslotRow in details:
                for day in timeslotRow:
                    if day and instructor in activeInstructors.keys():
                        activeInstructors[instructor][1] += 1
        instructorLoadAverage = 0
        # Calculate the average instructor load. Closer to 50% means equal distribution which is better
        for instructor in activeInstructors.values():
            instructorLoadAverage += (instructor[1] / instructor[0]) * 100
        if not len(activeInstructors):
            return 100.00
        instructorLoadAverage = round(instructorLoadAverage / len(activeInstructors), 2)
        return instructorLoadAverage