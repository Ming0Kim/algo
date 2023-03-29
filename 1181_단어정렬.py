import sys
input = sys.stdin.readline

N = int(input().split())

s = set()

for _ in range(N):
  word = input()
  print(word.split())

