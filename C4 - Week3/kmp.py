# python3
import sys


def ComputePrefixFunction(P):
    S = [0]*len(P)
    border = 0
    for i in range(1,len(P)):
        while border > 0 and P[i] != P[border]:
            border = S[border -1]
        if P[i] == P[border]:
            border = border +1 
        else:
            border = 0
        S[i] = border
    return S

def find_pattern(pattern, text):
  P = pattern + '$' + text
  S = ComputePrefixFunction(P)
  result = []
  leng = len(pattern)
  for i in range(leng+1,len(S)): 
      if S[i] == leng:
          result.append(i-leng-leng)
  return result


if __name__ == '__main__':
  pattern = sys.stdin.readline().strip()
  text = sys.stdin.readline().strip()
  result = find_pattern(pattern, text)
  print(" ".join(map(str, result)))

