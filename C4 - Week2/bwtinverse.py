# python3
import sys

def InverseBWT(bwt):
    result = ""
    lastCol = [(val, idx) for (idx, val) in enumerate(bwt)]
    firstCol = sorted(lastCol)
    index = {val: idx for (idx, val) in zip(firstCol, lastCol)}
    nextCol = firstCol[0]
    for j in range(len(bwt)):
        result += nextCol[0]
        nextCol = index[nextCol]
    return result[1:] + '$'

if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))