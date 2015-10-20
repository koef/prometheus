# -*- coding: utf-8 -*-
__author__ = 'koef'


class Student(object):
    def __init__(self, name, conf=None):
        if not conf:
            conf = {
                'exam_max': 30,
                'lab_max': 7,
                'lab_num': 10,
                'k': 0.61,
            }
        self.name = name
        self.conf = conf
        self.grades = {}
        self.exam = 0

    def make_lab(self, grade, lab=-1):
        if lab == -1:
            for i in range(self.conf["lab_num"]):
                if self.grades.get(i, 0) == 0:
                    lab = i
                    break
        if grade <= self.conf["lab_max"]:
            self.grades[lab] = grade
        else:
            self.grades[lab] = self.conf["lab_max"]
        return self

    def make_exam(self, grade):
        if grade <= self.conf["exam_max"]:
            self.exam = grade
        else:
            self.exam = self.conf["exam_max"]
        return self

    def is_certified(self):
        total_score = 0
        is_pass = False
        for counter in range(self.conf["lab_num"]):
            cur_grade = self.grades.get(counter, 0)
            total_score += cur_grade

        total_score += self.exam
        if float(total_score) / (self.conf["exam_max"] + self.conf["lab_max"] * self.conf["lab_num"]) >= self.conf["k"]:
            is_pass = True
        return total_score, is_pass


conf1 = {'exam_max': 20, 'lab_max': 40, 'lab_num': 2, 'k': 0.75}

o3 = Student('Oleg', conf1)
o3.make_lab(10).make_lab(10).make_exam(15)
print o3.is_certified()

o3.make_lab(20,1).make_lab(20,0)
print o3.is_certified()

o3.make_lab(50,2)
print o3.is_certified()

o3.make_lab(40,1)
print o3.is_certified()


