import pandas as pd

df = pd.read_excel('roaddistance.xlsx')
row_cnt, col_cnt = df.shape[0], df.shape[1]

def parse_xlsx():
  for x in range(1, row_cnt):
    for y in range(1, col_cnt):
      u = df.iat[x, 0].lower()
      v = df.iat[0, y].lower()
      d = df.iat[x, y]
      s1 = f"dist({u}, {v}, {d})."
      s2 = f"dist({v}, {u}, {d})."
      print(s1)
      if (d != 0):
        print(s2)

def gen_h():
  pass

if __name__ == "__main__":
  parse_xlsx()
  gen_h()
