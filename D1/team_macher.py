import requests
import random
import sys


class Students:
    def __init__(self, list_name):
        self.list_name = list_name
        self.students = {}
        self.course_id = {}

    def get_from_hack(self):
        req_hack = requests.get("https://hackbulgaria.com/api/students/",
                                verify=False)
        self.students = req_hack.json()

    def list_coureses(self):
        courses = []
        for student in self.students:
            for course in student["courses"]:
                if course["name"] not in courses:
                    courses.append(course["name"])
        for index, course in enumerate(courses):
            self.course_id[index + 1] = course
        print(self.course_id)
        return courses

    def mach_teams(self, course_id, team_size, group_time):
        available_students = []
        count_student = 0
        for student in self.students:
            if student["available"] is True:
                for course in student["courses"]:
                    if (course["name"] == self.course_id[course_id]
                            and course["group"] == group_time):
                        available_students.append(student)
                        count_student += 1
        random.shuffle(available_students)
        index = 0
        while index < count_student:
            if count_student - index - 1 >= team_size:
                for i in range(team_size):
                    print(available_students[index + i]["name"])
            else:
                for i in range(count_student - index - 1):
                    print(available_students[index + i]["name"])
            print("=========================================================")
            index += team_size


def main():
    hack = Students("Hack BG")
    hack.get_from_hack()
    hack.list_coureses()
    course = sys.argv[1]
    team_size = sys.argv[2]
    group = sys.argv[3]
    print("%s, %s, %s" % (course, team_size, group))
    hack.mach_teams(int(course), int(team_size), int(group))
if __name__ == '__main__':
        main()
