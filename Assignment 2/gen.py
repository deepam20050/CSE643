# To install dependecies run pip3 install -r requirements.txt
import pandas as pd

df = pd.read_excel('roaddistance.xlsx')
row_cnt, col_cnt = df.shape[0], df.shape[1]
delhiX, delhiY = -1, -1
output = set()

def parse_xlsx():
  global delhiY
  global delhiX
  for x in range(1, row_cnt):
    for y in range(1, col_cnt):
      u = df.iat[x, 0].lower()
      v = df.iat[0, y].lower()
      d = df.iat[x, y]
      if (u == "delhi" and delhiY == -1):
        delhiY = y
      if (u == "delhi" and delhiX == -1):
        delhiX = x
      s1 = f"dist({u}, {v}, {d})."
      s2 = f"dist({v}, {u}, {d})."
      output.add(s1)
      if (d != 0):
        output.add(s2)

def gen_h():
  for x in range(1, row_cnt):
    for y in range(1, col_cnt):
      u = df.iat[x, 0].lower()
      v = df.iat[0, y].lower()
      l1, l2 = df.iat[x, delhiY], df.iat[delhiX, y]
      l3 = (l1 + l2 + abs(l1 - l2)) // 2
      if (u == v):
        l3 = 0
      s1 = f"h({u}, {v}, {l3})."
      s2 = f"h({v}, {u}, {l3})."
      output.add(s1)
      output.add(s2)
  for x in range(1, row_cnt):
    for xNew in range(1, row_cnt):
      u = df.iat[x, 0].lower()
      v = df.iat[xNew, 0].lower()
      l1, l2 = df.iat[x, delhiY], df.iat[xNew, delhiY]
      l3 = (l1 + l2 + abs(l1 - l2)) // 2
      if (u == v):
        l3 = 0
      s1 = f"h({u}, {v}, {l3})."
      s2 = f"h({v}, {u}, {l3})."
      output.add(s1)
      output.add(s2)
  for y in range(1, col_cnt):
    for yNew in range(1, col_cnt):
      u = df.iat[0, y].lower()
      v = df.iat[0, yNew].lower()
      l1, l2 = df.iat[delhiX, y], df.iat[delhiX, yNew]
      l3 = (l1 + l2 + abs(l1 - l2)) // 2
      if (u == v):
        l3 = 0
      s1 = f"h({u}, {v}, {l3})."
      s2 = f"h({v}, {u}, {l3})."
      output.add(s1)
      output.add(s2)

def gen_db():
  o = list(output)
  o.sort()
  for s in o:
    print(s)

if __name__ == "__main__":
  parse_xlsx()
  gen_h()
  gen_db()