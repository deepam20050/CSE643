'''
Deepam Sarmah
2020050
deepam20050@iiitd.ac.in
'''
from durable.lang import *

Courses = ["Data Structures & Algorithms", "Computer Networks", "Operating Systems", "Machine Learning", "Artificial Intelligence", "Computer Graphics", "Human Computer Interaction", "Introduction to Animation and Graphics", "Game Design and Development", "Valuation and Portfolio Management", "Money and Banking"]
Interests = ["Software Job", "Research", "Graphic/Designer Job", "Startups"]

career_ml = [0, 1, 2, 3, 4]
career_sde = [0, 1, 2, 3]
career_startup = [0, 1, 2, 3, 9, 10]
career_research = [0, 1, 2, 3, 4, 5]
career_ui = [0, 2, 7, 8]
career_game = [0, 1, 2, 3, 4, 7, 8]

'''
  ruleset('courses')
  ruleset('interest')
  ruleset('career')
'''

# {'count', 'cgpa', 'work'}
with ruleset('courses'):
  @when_all((m.count >= 3) & (m.cgpa >= 8) & (m.work == 0))
  def mlpath(c):
    c.assert_fact('interest', {'work': 'ml-engineer', 'cgpa': m.cgpa})

  @when_all((m.count >= 3) & (m.cgpa >= 7) & (m.work == 0))
  def sdepath(c):
    c.assert_fact('interest', {'work': 'sde', 'cgpa': m.cgpa})

  @when_all((m.count >= 5) & (m.cgpa >= 9) & (m.work == 1))
  def researchpath(c):
    c.assert_fact('interest', {'work': 'research', 'cgpa': m.cgpa})

  @when_all((m.count >= ))

# {'work', 'cgpa'}
with ruleset('interest'):
  pass

# {'cgpa'}
with ruleset('career'):
  pass

if __name__ == "__main__":
  cgpa = int(input("Enter CGPA: "))
  print("Choose course indices of the courses you've done from the following courses")
  for i in range(len(Courses)):
    print(i, ": ", Courses[i])
  courses_done = []
  num_courses = int(input("Enter number of courses done: "))
  for i in range(num_courses):
    x = int(input("Enter course index: "))
    courses_done.append(x)
  print("Choose interest from the following interest options")
  for i in range(len(Interests)):
    print(i, ": ", Interests[i])
  interest_idx = int(input("Enter interest index: "))
