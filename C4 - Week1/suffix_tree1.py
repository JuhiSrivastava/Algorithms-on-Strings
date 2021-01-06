# python3
import sys

def build_suffix_tree(text):
  result = []
  tree = dict()
  maxNode = 1
  i = 0
  tree[0] = dict()
  tree[0]['$'] = 1
  while i < len(text):
      currentNode = 0
      pattern = text[i:]
      for j in range(len(pattern)):
          if currentNode not in tree.keys():
                tree[currentNode] = dict()
                maxNode = maxNode + 1
                if j == len(pattern)-1 and pattern[j] == '$':
                    tree[currentNode][pattern[j] + str(i)] = maxNode
                else:
                    tree[currentNode][pattern[j]] = maxNode
          else:
                if pattern[j] not in tree[currentNode].keys():
                    maxNode = maxNode + 1
                    if j == len(pattern)-1 and pattern[j] == '$': 
                        tree[currentNode][pattern[j] + str(i)] = maxNode
                    else:
                        tree[currentNode][pattern[j]] = maxNode
          if j != len(pattern)-1:
              currentNode = tree[currentNode][pattern[j]]
      i = i+1
  for k in range(1):
    i = 0
    while i <= max(list(tree.keys())):
        j = 0
        flag = True
        while i in tree.keys() and j != len(tree[i]):
          li = list(tree[i].keys())
          if tree[i][li[j]] in tree.keys() and len(tree[tree[i][li[j]]]) == 1:
              key =list(tree[tree[i][li[j]]].keys())[0]
              tree[i][li[j]+key] = tree[tree[i][li[j]]][key]
              node = tree[i][li[j]]
              del tree[i][li[j]]
              del tree[node]
              flag = False
          else:
              j = j+1
        if flag:
            i = i + 1
  for i in tree.keys():
      for j in tree[i].keys():
          if '$' in j and len(j) > 1:
              data = j.split("$")
              result.append(data[0] + '$')
          else:
              result.append(j)
  return result


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  result = build_suffix_tree(text)
  print("\n".join(result))