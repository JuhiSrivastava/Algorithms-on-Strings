# python3
import sys


class Node:
    def __init__(self, a, b, c):
        self.start = a
        self.leng = b
        self.NextNode = c

def find(i,text,tree, currentNode):
    flag = False
    pos = -1
    while not flag:
        for j in range(len(tree[currentNode])):
            if i<tree[currentNode][j].start and text[i:i+tree[currentNode][j].leng] == text[tree[currentNode][j].start:tree[currentNode][j].start+tree[currentNode][j].leng]:
                i = i+tree[currentNode][j].leng
                currentNode = tree[currentNode][j].NextNode
                flag = False
                break
            else:
                flag = True
                if text[i] == text[tree[currentNode][j].start]:
                    pos = j
                    break
    return pos,i,currentNode 

def findMatchPosition(i,text,tree, currentNode,maxNode):
    flg = False
    currentNode1 = currentNode
    j,i,currentNode = find(i,text,tree, currentNode)
    i1 = i
    for k in range(tree[currentNode][j].start,tree[currentNode][j].start+tree[currentNode][j].leng):
            if text[i] == text[k]:
                flg = True
            else:
                break
            i=i+1
    if flg and k != tree[currentNode][j].start+tree[currentNode][j].leng:
        newNode = tree[currentNode][j].NextNode
        maxNode = maxNode +1 
        tree[maxNode] = []
        tree[newNode].append(Node(k,tree[currentNode][j].leng-(i-i1),maxNode))
        maxNode = maxNode +1 
        tree[maxNode] = []
        tree[newNode].append(Node(i,len(text)-i,maxNode))
        tree[currentNode][j].start = i1
        tree[currentNode][j].leng = i-i1
    else:
        tree[i] = []
        tree[currentNode].append(Node(i,len(text)-i,i))
    return tree,maxNode
    

def build_suffix_tree(text):
  
  tree = dict()
  maxNode = len(text)
  l = len(text)-1
  tree[maxNode] =[]
  tree[maxNode].append(Node(l,1,l))
  tree[l] = []
  l = l - 1
  while l >= 0:
      currentNode = len(text)
      pattern = text[l:]
      tree,maxNode = findMatchPosition(l,text,tree, currentNode,maxNode)
      l = l-1
  result = fillResult(tree,text)
  return result

def fillResult(tree,text):
    result = []
    for p in tree.keys():
        for t in tree[p]:
            result.append(text[t.start:t.start+t.leng])
    return result
    
if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  result = build_suffix_tree(text)
  print("\n".join(result))