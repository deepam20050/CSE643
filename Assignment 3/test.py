'''
Deepam Sarmah
2020050
deepam20050@iiitd.ac.in
'''
from durable.lang import *

ml_engineer = [0, 1, 2, 3, 4]

with ruleset('courses'):
  @when_all((m.type >= 4))
  def mlpath(c):
    c.assert_fact({'subject': 'ML Engineer'})
  
  @when_all((m.type < 4))
  def noml(c):
    c.assert_fact({'subject' : 'NIKAL'})

  @when_all(+m.subject)
  def output(c):
    print('{0}'.format(c.m.subject))

if __name__ == "__main__":
  listA = []
  n = int(input())
  for i in range(n):
    x = int(input())
    listA.append(x)
  x = len(set(listA) & set(ml_engineer))
  assert_fact('courses', {'type' : x})