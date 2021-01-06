# python3
import sys

def SortCharacters(text):
    order = [0]*len(text)
    count = [0]*5
    for i in range(len(text)):
        count[text[i]] = count[text[i]] + 1
    for j in range(1,5):
        count[j] = count[j] + count[j-1]
    for i in range(len(text)-1,-1,-1):
        c = text[i]
        count[c] = count[c] -1
        order[count[c]] = i
    return order

def ComputeCharClasses(text,order):
    classes = [0]*len(text)
    classes[order[0]] = 0
    for i in range(1,len(text)):
        if text[order[i]] != text[order[i-1]]:
            classes[order[i]] = classes[order[i-1]] + 1
        else:
            classes[order[i]] = classes[order[i-1]]
    return classes

def SortDouble(text,L,order,classes):
    count = [0]*len(text)
    newOrder = [0]*len(text)
    for i in range(len(text)):
        count[classes[i]] = count[classes[i]] + 1
    for j in range(1,len(text)):
        count[j] = count[j] + count[j-1]
    for i in range(len(text)-1,-1,-1):
        start = (order[i]-L +len(text))%len(text)
        cl = classes[start]
        count[cl] = count[cl] -1
        newOrder[count[cl]] = start
    return newOrder

def UpdateClasses(newOrder,classes,L):
    n = len(newOrder)
    newClass = [0]*n
    newClass[newOrder[0]] = 0
    for i in range(1, n):
        cur = newOrder[i]
        prev = newOrder[i-1]
        mid = (cur + L)%n
        midprev = (prev + L)%n
        if classes[cur] != classes[prev] or classes[mid] != classes[midprev]:
            newClass[cur] = newClass[prev] + 1
        else:
            newClass[cur] = newClass[prev]
    return newClass


def build_suffix_array(text):
    order = SortCharacters(text)
    classes = ComputeCharClasses(text,order)
    L = 1
    while L < len(text):
        order = SortDouble(text,L,order,classes)
        classes = UpdateClasses(order,classes,L)
        L = 2*L
    result = order
    return result


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  newText = []
  for i in range(len(text)):
      if text[i] == '$':
          newText.append(0)
      elif text[i] == 'A':
          newText.append(1)
      elif text[i] == 'C':
          newText.append(2)
      elif text[i] == 'G':
          newText.append(3)
      elif text[i] == 'T':
          newText.append(4)
      
  print(" ".join(map(str, build_suffix_array(newText))))
