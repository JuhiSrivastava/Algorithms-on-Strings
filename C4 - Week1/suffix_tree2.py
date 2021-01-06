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
            print("loop", i,j,tree[currentNode][j].start,tree[currentNode][j].leng,tree[currentNode][j].NextNode)
            if i<tree[currentNode][j].start and text[i:i+tree[currentNode][j].leng] == text[tree[currentNode][j].start:tree[currentNode][j].start+tree[currentNode][j].leng]:
                i = i+tree[currentNode][j].leng
                currentNode = tree[currentNode][j].NextNode
                print("dfvhskdjf",currentNode)
                flag = False
                break
            else:
                flag = True
                #print(text[i] ,text[tree[currentNode][j].start])
                if text[i] == text[tree[currentNode][j].start]:
                    pos = j
                    break
    return pos,i,currentNode 

def findMatchPosition(i,text,tree, currentNode,maxNode):
    printT(tree)
    flg = False
    currentNode1 = currentNode
    #i1 = i
    j,i,currentNode = find(i,text,tree, currentNode)
    i1 = i
    print("jhgkjhgm",j,i,currentNode, currentNode1)
    for k in range(tree[currentNode][j].start,tree[currentNode][j].start+tree[currentNode][j].leng):
            if text[i] == text[k]:
                flg = True
            else:
                break
            i=i+1
    print(flg,k,tree[currentNode][j].start+tree[currentNode][j].leng,i,i1)
    if flg and k != tree[currentNode][j].start+tree[currentNode][j].leng:
        print("After1")
        printT(tree)
        newNode = tree[currentNode][j].NextNode
        maxNode = maxNode +1 
        tree[maxNode] = []
        tree[newNode].append(Node(k,tree[currentNode][j].leng-(i-i1),maxNode))
        maxNode = maxNode +1 
        tree[maxNode] = []
        tree[newNode].append(Node(i,len(text)-i,maxNode))
        tree[currentNode][j].start = i1
        tree[currentNode][j].leng = i-i1
        print("After2")
        printT(tree)
    else:
        tree[i] = []
        tree[currentNode].append(Node(i,len(text)-i,i))
    return tree,maxNode
    

def build_suffix_tree(text):
  result = []
  tree = dict()
  maxNode = len(text)
  print(maxNode)
  l = len(text)-1
  tree[maxNode] =[]
  tree[maxNode].append(Node(l,1,l))
  tree[l] = []
  l = l - 1
  print("Before")
  printT(tree)
  while l >= 0:
      currentNode = len(text)
      pattern = text[l:]
      print(currentNode)
      print(pattern,maxNode)
      tree,maxNode = findMatchPosition(l,text,tree, currentNode,maxNode)
      printT(tree)
      l = l-1
  return result

def printT(tree):
      print("====================")
      for p in tree.keys():
          print("Node",p)
          for t in tree[p]: 
            print(t.start, t.leng, t.NextNode )
if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  result = build_suffix_tree(text)
  print("\n".join(result))