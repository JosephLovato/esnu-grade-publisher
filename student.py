#
# student.py
# store student data and associated exam grades
#

def convert_score_to_esnu(score):
    if score == 3:
        return 'E'
    elif score == 2:
        return 'S'
    elif score == 1:
        return 'N'
    elif score == 0:
        return 'U'
    else:
        return 'X'


class student:
    def __init__(self, first_name, last_name, id):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.module_scores = {}
        self.final_score = "U"

    def generate_comment(self):
        comment = ""
        for m in self.module_scores:
            comment += m + ": " + \
                self.module_scores[m] + "\n" + \
                convert_score_to_esnu(self.module_scores[m]) + "\n" #comment out this line if publishing final grades
        return comment
