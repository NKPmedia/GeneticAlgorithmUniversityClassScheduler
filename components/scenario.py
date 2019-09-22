
class Subject:
    def __init__(self, id, name, lesson_count, short_name, instructors, subject_type, withtest):
        self.id = id
        self.name = name
        self.lesson_count = lesson_count
        self.short_name = short_name
        self.instructors = instructors
        self.subject_type = subject_type
        self.withtest = withtest


class Section:
    def __init__(self, id, name, available, section_type):
        self.id = id
        self.name = name
        self.available = available
        self.section_type = section_type


class Instructor:
    def __init__(self, id, name, hours, schedule):
        self.id = id
        self.name = name
        self.hours = hours
        self.schedule = schedule


class InstructorLessonPossibility:
    def __init__(self, instructor: Instructor, co_ref, score):
        self.instructor = instructor
        self.co_ref = co_ref
        self.score = score


class Lesson(object):
    def __init__(self, instructors: Instructor, section: Section, subject: Subject):
        self.instructors = instructors
        self.section = section
        self.subject = subject

class Scenario():

    def __init__(self, data):
        self.instructors = data["instructors"]
        self.rooms = data["rooms"]
        self.sections = data["sections"]
        self.subjects = data["subjects"]

        # lesson_id x (instructors(list), section, subject_id)
        self.lessons = self.construct_lesson_array()

    def construct_lesson_array(self):
        lessons = []
        section: Section
        for sec_id, section in self.sections.items():
            subject: Subject
            for sub_id, subject in self.subjects.items():
                if subject.subject_type == section.section_type:
                    instructors = [InstructorLessonPossibility(self.instructors[int(id)], elem["co_ref"], elem["score"])
                                   for id, elem in subject.instructors.items()]
                    lessons.append(Lesson(instructors, section, subject))
        return lessons