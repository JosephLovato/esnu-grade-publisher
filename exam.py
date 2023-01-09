from re import S
from student import student, convert_score_to_esnu
import pandas as pd


class exam:
    def __init__(self, rosterfilename, first_name, last_name, final_name, *module_names):
        self.students = []
        file = open(rosterfilename)
        lines = file.readlines()
        for line in lines:
            data = line.split(',')
            self.students.append(student(data[1], data[0], data[2][:-1]))
        file.close()
        self.first_name = first_name
        self.last_name = last_name
        self.final_name = final_name
        self.module_names = list(module_names)

    def add_scores(self, filename):
        df = pd.read_csv(filename)
        for i, student in enumerate(self.students):
            result = df[(df[self.first_name] == student.first_name) &
                        (df[self.last_name] == student.last_name)]
            if result.empty:
                continue
            for m in self.module_names:
                self.students[i].module_scores[m] = result[m].values[0]
            # self.students[i].final_score = convert_score_to_esnu(
            #     result[self.final_name].values[0])
            self.students[i].final_score = result[self.final_name].values[0]
