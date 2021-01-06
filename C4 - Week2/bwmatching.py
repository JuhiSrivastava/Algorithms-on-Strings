# python3
import sys


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


def CountOccurrences(pattern, bwt, starts, occ_counts_before):
    top = 0
    bottom = len(bwt) -1
    while top <= bottom:
        if len(pattern) > 0:
            symbol = pattern[-1]
            pattern = pattern[:len(pattern) -1]
            if symbol in bwt[top:bottom+1]:
                top = starts[symbol] + occ_counts_before[symbol][top]
                bottom = starts[symbol] + occ_counts_before[symbol][bottom+1] -1
            else:
                return 0
        else:
            return bottom-top+1
    return 0



if __name__ == '__main__':
  bwt = sys.stdin.readline().strip()
  pattern_count = int(sys.stdin.readline().strip())
  patterns = sys.stdin.readline().strip().split()
  # Preprocess the BWT once to get starts and occ_count_before.
  # For each pattern, we will then use these precomputed values and
  # spend only O(|pattern|) to find all occurrences of the pattern
  # in the text instead of O(|pattern| + |text|).  
  starts, occ_counts_before = PreprocessBWT(bwt)
  occurrence_counts = []
  for pattern in patterns:
    occurrence_counts.append(CountOccurrences(pattern, bwt, starts, occ_counts_before))
  print(' '.join(map(str, occurrence_counts)))
