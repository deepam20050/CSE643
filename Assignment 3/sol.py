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

'''
CGPA
>= 9 -> 0
>= 8 -> 1
>= 7 -> 2
'''

# {'cnt', 'cgpa', 'work'}
with ruleset('courses'):
  @when_all((m.cnt >= 3) & (m.cgpa >= 8) & (m.work == 0))
  def mlpath(c):
    c.assert_fact('interest', {'work': 'ml-engineer', 'cgpa': 1})

  @when_all((m.cnt >= 3) & (m.cgpa >= 7) & (m.work == 0))
  def sdepath(c):
    c.assert_fact('interest', {'work': 'sde', 'cgpa': 2})

  @when_all((m.cnt >= 5) & (m.cgpa >= 9) & (m.work == 1))
  def researchpath(c):
    c.assert_fact('interest', {'work': 'research', 'cgpa': 0})

  @when_all((m.cnt >= 3) & (m.cgpa >= 9) & (m.work == 2))
  def uipath(c):
    c.assert_fact('interest', {'work': 'ui', 'cgpa': 0})
  
  @when_all((m.cnt >= 3) & (m.cgpa >= 8) & (m.work == 2))
  def gamepath(c):
    c.assert_fact('interest', {'work': 'game', 'cgpa' : 1})
  
  @when_all((m.cnt >= 3) & (m.cgpa >= 7) & (m.work == 2))
  def graphpath(c):
    c.assert_fact('interest', {'work': 'ui', 'cgpa': 2})

  @when_all((m.cnt >= 3) & (m.cgpa >= 9) & (m.work == 3))
  def startuppath(c):
    c.assert_fact('interest', {'work': 'startup', 'cgpa': 0})
  
  @when_all((m.cnt >= 3) & (m.cgpa >= 7) & (m.work == 3))
  def startup_sde(c):
    c.assert_fact('interest', {'work': 'sde', 'cgpa': 1})

  @when_all(m.cgpa > 0)
  def generic(c):
    c.assert_fact('interest', {'work': 'intern', 'cgpa': -1})

'''
CGPA
>= 9 -> 0
>= 8 -> 1
>= 7 -> 2
'''

# {'work', 'cgpa'}
with ruleset('interest'):
  @when_all((m.work == 'ml-engineer') & (m.cgpa <= 1))
  def go_ml(c):
    c.assert_fact('career', {'option': 1})
  
  @when_all((m.work == 'ml-engineer') & (m.cgpa <= 2))
  def go_sde(c):
    c.assert_fact('career', {'option': 0})
  
  @when_all((m.work == 'research') & (m.cgpa == 0))
  def goresearch(c):
    c.assert_fact('career', {'option': 2})
  
  @when_all((m.work == 'research') & (m.cgpa <= 2))
  def go_research_ml(c):
    c.assert_fact('career', {'option': 1})

  @when_all((m.work == 'startup') & (m.cgpa == 0))
  def go_startup(c):
    c.assert_fact('career', {'option': 3})
  
  @when_all((m.work == 'startup') & (m.cgpa <= 1))
  def go_startup(c):
    c.assert_fact('career', {'option': 0})
  
  @when_all((m.work == 'ui') & (m.cgpa <= 1))
  def go_ui(c):
    c.assert_fact('career', {'option': 5})
  
  @when_all((m.work == 'ui') & (m.cgpa <= 2))
  def go_ui_graphic(c):
    c.assert_fact('career', {'option': 4})
  
  @when_all((m.work == 'game'))
  def go_game(c):
    c.assert_fact('career', {'option': 6})
  
  @when_all((m.cgpa < 0))
  def go_intern(c):
    c.assert_fact('career', {'option': 7})

# {'occ', 'cgpa'}
with ruleset('career'):
  @when_all(m.option == 0)
  def sde(c):
    c.assert_fact({'occ': 'Software Engineer'})
  
  @when_all(m.option == 1)
  def ml(c):
    c.assert_fact({'occ': 'ML Engineer'})
  
  @when_all(m.option == 2)
  def research(c):
    c.assert_fact({'occ': 'Research'})

  @when_all(m.option == 3)
  def startup(c):
    c.assert_fact({'occ': 'Entrepreneurship'})

  @when_all(m.option == 4)
  def graphic(c):
    c.assert_fact({'occ': 'Graphic Designer'})
  
  @when_all(m.option == 5)
  def ui(c):
    c.assert_fact({'occ': 'UI/UX Designer'})
  
  @when_all(m.option == 6)
  def game(c):
    c.assert_fact({'occ': 'Game Developer'})
  
  @when_all(m.option == 7)
  def intern(c):
    c.assert_fact({'occ': 'Internship'})
  
  @when_all(+m.occ)
  def output(c):
    print('Career suggested: {0}'.format(c.m.occ))

def get_common (listA, listB):
  return len(set(listA) & set(listB))

def start(x, cgpa, interest_idx):
  assert_fact('courses', {'cnt': x, 'cgpa': cgpa, 'work': interest_idx})

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
  if (interest_idx == 0):
    start(get_common(courses_done, career_sde), cgpa, interest_idx)
  elif (interest_idx == 1):
    start(get_common(courses_done, career_research), cgpa, interest_idx)
  elif (interest_idx == 2):
    start(get_common(courses_done, career_ui), cgpa, interest_idx)
    start(get_common(courses_done, career_game), cgpa, interest_idx)
  elif (interest_idx == 3):
    start(get_common(courses_done, career_startup), cgpa, interest_idx)