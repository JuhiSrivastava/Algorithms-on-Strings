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
    text = newText
    order = SortCharacters(text)
    classes = ComputeCharClasses(text,order)
    L = 1
    while L < len(text):
        order = SortDouble(text,L,order,classes)
        classes = UpdateClasses(order,classes,L)
        L = 2*L
    result = order
    return result


def PreprocessBWT(bwt):
    lastCol = [(val, idx) for (idx, val) in enumerate(bwt)]
    firstCol = sorted(lastCol)
    starts = dict()
    occ_counts_before = dict()
    CA = 0
    CC = 0
    CG = 0
    CT = 0
    occ_counts_before['A'] = [0]*(len(firstCol)+1)
    occ_counts_before['C'] = [0]*(len(firstCol)+1)
    occ_counts_before['G'] = [0]*(len(firstCol)+1)
    occ_counts_before['T'] = [0]*(len(firstCol)+1)
    occ_counts_before['$'] = [0]*(len(firstCol)+1)
    for i in range(len(firstCol)):
        if firstCol[i][0] == 'A':
            if 'A' not in starts:
                starts['A'] = i
            CA += 1
            occ_counts_before['A'][firstCol[i][1] +1] = CA
        if firstCol[i][0] == 'C':
            if 'C' not in starts:
                starts['C'] = i
            CC += 1
            occ_counts_before['C'][firstCol[i][1] +1] = CC
        if firstCol[i][0] == 'G':
            if 'G' not in starts:
                starts['G'] = i
            CG += 1
            occ_counts_before['G'][firstCol[i][1] +1] = CG
        if firstCol[i][0] == 'T':
            if 'T' not in starts:
                starts['T'] = i
            CT += 1
            occ_counts_before['T'][firstCol[i][1] +1] = CT
        if firstCol[i][0] == '$':
            if '$' not in starts:
                starts['$'] = i
            occ_counts_before['$'][firstCol[i][1] +1] = 1
    for i in range(1,len(firstCol)+1):
        occ_counts_before['A'][i] = occ_counts_before['A'][i-1] if occ_counts_before['A'][i] == 0 else occ_counts_before['A'][i]
        occ_counts_before['C'][i] = occ_counts_before['C'][i-1] if occ_counts_before['C'][i] == 0 else occ_counts_before['C'][i]
        occ_counts_before['G'][i] = occ_counts_before['G'][i-1] if occ_counts_before['G'][i] == 0 else occ_counts_before['G'][i]
        occ_counts_before['T'][i] = occ_counts_before['T'][i-1] if occ_counts_before['T'][i] == 0 else occ_counts_before['T'][i]
        occ_counts_before['$'][i] = occ_counts_before['$'][i-1] if occ_counts_before['$'][i] == 0 else occ_counts_before['$'][i]
    return starts, occ_counts_before    


def CountOccurrences(pattern, bwt, starts, occ_counts_before,suffix_array):
    top = 0
    bottom = len(bwt) -1
    li = []
    while top <= bottom:
        if len(pattern) > 0:
            symbol = pattern[-1]
            pattern = pattern[:len(pattern) -1]
            if symbol in bwt[top:bottom+1]:
                top = starts[symbol] + occ_counts_before[symbol][top]
                bottom = starts[symbol] + occ_counts_before[symbol][bottom+1] -1
            else:
                return li
        else:
            for i in range(top,bottom+1):
                li.append(suffix_array[i])
            return li
    return li


def find_occurrences(ntext, patterns):
    suffix_array = build_suffix_array(ntext+'$')
    newText1 = BWT(ntext+'$',suffix_array)
    starts, occ_counts_before = PreprocessBWT(newText1)
    occurrence_counts = set()
    for pattern in patterns:
        occurrence_counts = occurrence_counts|set(CountOccurrences(pattern, newText1, starts, occ_counts_before,suffix_array))
    return occurrence_counts

def BWT(text,suffix_array):
    result = ""
    leng = len(suffix_array)
    for i in range(leng):
       result = result + text[suffix_array[i]-1]
    return result

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    pattern_count = int(sys.stdin.readline().strip())
    patterns = sys.stdin.readline().strip().split()
    occs = find_occurrences(text, patterns)
    print(" ".join(map(str, occs)))