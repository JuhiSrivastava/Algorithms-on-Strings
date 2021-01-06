# python3
import sys

def BWT(text):
    result = ""
    li =[]
    leng = len(text)
    for i in range(leng):
       text = text[leng-1] + text
       text = text[:len(text) -1]
       li.append(text)
    li = sorted(li)
    for i in li:
       result = result + i[leng-1] 
    return result

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))