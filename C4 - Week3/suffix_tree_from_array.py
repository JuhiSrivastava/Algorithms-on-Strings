# python3
import sys

class SuffixTreeNode:
  def __init__(self, parent, children,stringDepth,edgeStart,edgeEnd):
    self.parent = parent
    self.children = children
    self.stringDepth = stringDepth
    self.edgeStart = edgeStart
    self.edgeEnd = edgeEnd
    
#class SuffixTreeNode:
    #SuffixTreeNode parent
    #Map<char, SuffixTreeNode> children
    #integer stringDepth
    #integer edgeStart
    #integer edgeEnd
    
def CreateNewLeaf(node, S, suffix):
    leaf = SuffixTreeNode(
            children = {}, 
            parent = node,
            stringDepth = len(S) - suffix,
            edgeStart = suffix + node.stringDepth,
            edgeEnd = len(S) - 1)
    node.children[S[leaf.edgeStart]] = leaf
    return leaf

def BreakEdge(node, S, start, offset):
    startChar  = S[start]
    midChar   =  S[start + offset]
    midNode  =  SuffixTreeNode(
            children = {}, 
            parent = node,
            stringDepth = node.stringDepth + offset,
            edgeStart = start,
            edgeEnd = start + offset - 1)
    midNode.children[midChar]  = node.children[startChar]
    node.children[startChar].parent  = midNode
    node.children[startChar].edgeStart += offset
    node.children[startChar] =  midNode
    return midNode


def suffix_array_to_suffix_tree(sa, lcp, text):
    root = SuffixTreeNode(
            children = {}, 
            parent = None,
            stringDepth = 0,
            edgeStart = -1,
            edgeEnd = -1)
    lcpPrev =  0
    curNode =  root
    for i in range(len(text)):
        suffix = sa[i]
    while curNode.stringDepth > lcpPrev:
        curNode = curNode.parent
    if curNode.stringDepth == lcpPrev:
        curNode = CreateNewLeaf(curNode, text, suffix)
    else:
        edgeStart  = sa[i-1] + curNode.stringDepth
        offset  = lcpPrev - curNode.stringDepth
        midNode =  BreakEdge(curNode, text, edgeStart, offset)
        curNode =  CreateNewLeaf(midNode, text, suffix)
    if i < len(text) -1:
        lcpPrev  = lcp[i]
    return root


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    sa = list(map(int, sys.stdin.readline().strip().split()))
    lcp = list(map(int, sys.stdin.readline().strip().split()))
    print(text)
    # Build the suffix tree and get a mapping from 
    # suffix tree node ID to the list of outgoing Edges.
    tree = suffix_array_to_suffix_tree(sa, lcp, text)
    """
    Output the edges of the suffix tree in the required order.
    Note that we use here the contract that the root of the tree
    will have node ID = 0 and that each vector of outgoing edges
    will be sorted by the first character of the corresponding edge label.
    
    The following code avoids recursion to avoid stack overflow issues.
    It uses two stacks to convert recursive function to a while loop.
    This code is an equivalent of 
    
        OutputEdges(tree, 0);
    
    for the following _recursive_ function OutputEdges:
    
    def OutputEdges(tree, node_id):
        edges = tree[node_id]
        for edge in edges:
            print("%d %d" % (edge[1], edge[2]))
            OutputEdges(tree, edge[0]);
    
    """
    stack = [(0, 0)]
    result_edges = []
    while len(stack) > 0:
      (node, edge_index) = stack[-1]
      stack.pop()
      if not node in tree:
        continue
      edges = tree[node]
      if edge_index + 1 < len(edges):
        stack.append((node, edge_index + 1))
      print("%d %d" % (edges[edge_index][1], edges[edge_index][2]))
      stack.append((edges[edge_index][0], 0))
