'''
Deepam Sarmah
2020050
deepam20050@iiitd.ac.in
'''
import string
import nltk

l = []
courses = ["automata", "algos", "datascience", "cp", "coding", "oop", "security", "business"]

def init():
  nltk.download('omw-1.4')
  nltk.download('stopwords')
  nltk.download('punkt')
  nltk.download('wordnet')

def parse():
  stops = set(nltk.corpus.stopwords.words('english'))
  lemmatized = nltk.WordNetLemmatizer()
  data = input("What do you like in CS?\n")
  data = data.lower()
  for x in string.punctuation:
    data = data.replace(x, " ")
  data = lemmatized.lemmatize(data)
  tokenized = nltk.word_tokenize(data)
  for x in tokenized:
    if x not in stops:
      l.append(x)

def solve():
  file = open("facts.txt", "w")
  for x in courses:
    if x in l:
      file.write(f"yes('{x}').\n")
    else:
      file.write(f"no('{x}').\n")
  x1 = input("Do you want to pursue research? ")
  file.write(f"res({x1}).\n")
  x2 = input("Do you want a career in ML? ")
  file.write(f"ml({x2}).\n")
  x3 = input("Do you want a career as a SDE? ")
  file.write(f"sde({x3}).\n")
  x4 = input("Do you want to pursue a career in cyber security? ")
  file.write(f"cyber({x4}).\n")
  x5 = input("Do you want to build your own startup? ")
  file.write(f"biz({x5}).\n")
  file.close()

if __name__ == "__main__":
  init()
  parse()
  solve()