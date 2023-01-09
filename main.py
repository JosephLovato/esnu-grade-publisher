#
# main.py
#

from exam import exam

from canvasapi import Canvas

# Canvas API URL
API_URL = "https://elearning.mines.edu"
# Canvas API key (generate from https://elearning.mines.edu/profile/settings > + New Access Token)
API_KEY = "9802~GdDE4yv0soEtR9NuvEUSstoWFXbZb7sugttdFKKrsnUh7ruC9ycqhAR8mqr2zpwT"
# Course to work on (get id from canvas URL)
COURSE = "42642"
# Assignment (get id from canvas URL)
ASSIGNMENT = "316730"

canvas = Canvas(API_URL, API_KEY)
course = canvas.get_course(COURSE)
assignment = course.get_assignment(ASSIGNMENT)


csci220 = exam("roster.csv", "first_name", "last_name",
               "Final", "Analysis", "Programming", "Comprehension")
csci220.add_scores("final_grades.csv")

# Print grades to check them
for s in csci220.students:
    print(s.first_name, s.last_name, s.final_score)
    print(s.generate_comment())

# Test one student
# submission = assignment.get_submission(csci220.students[0].id)
# submission.edit(submission={"posted_grade": csci220.students[0].final_score}, comment={
#                 "text_comment": csci220.students[0].generate_comment()})


# Submit all students
# for s in csci220.students:
#     print(s.last_name)
#     submission = assignment.get_submission(s.id)
#     submission.edit(submission={"posted_grade": s.final_score}, comment={
#                     "text_comment": s.generate_comment()})

print("...done.")
