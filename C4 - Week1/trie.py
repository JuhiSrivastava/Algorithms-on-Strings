#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.

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


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
