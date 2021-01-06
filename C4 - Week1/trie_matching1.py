# python3
import sys

def trie_matching(text,tree):
    currentNode = 0
    for j in range(len(text)):
        if currentNode in tree.keys():
            if text[j] in tree[currentNode].keys():
                currentNode = tree[currentNode][text[j]]
            else:
                return False
        if j == len(text) -1 and currentNode in tree.keys():
            return False
    return True    
            

def build_trie(patterns):
    tree = dict()
    maxNode = 0
    for i in patterns:
        currentNode = 0
        for j in range(len(i)):
            if currentNode not in tree.keys():
                tree[currentNode] = dict()
                maxNode = maxNode + 1
                tree[currentNode][i[j]] = maxNode
            else:
                if i[j] not in tree[currentNode].keys():
                    maxNode = maxNode + 1
                    tree[currentNode][i[j]] = maxNode
            currentNode = tree[currentNode][i[j]]
    return tree

def solve (text, n, patterns):
    tree = build_trie(patterns)
    result = []
    i = 0
    while len(text) > 0:
        if trie_matching(text,tree):
            result.append(i)
        i = i+1
        text = text[1:]
    return result

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
