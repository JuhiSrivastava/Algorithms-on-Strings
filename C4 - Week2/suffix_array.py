# python3
import sys


def build_suffix_array(text):
    li = []
    for i in range(len(text)-1,-1,-1):
        li.append((text[i:len(text)],i))
    li = sorted(li)
    result = []
    for (i,j) in li:
        result.append(j)
    return result


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, build_suffix_array(text))))
