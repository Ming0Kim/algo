N = int(input())
words = set()

# 중복 제거
for _ in range(N):
    words.add(input())

words = list(words) 

# 사전 순서대로 정렬
words.sort()

# 글자 수 순서대로 정렬
words.sort(key=lambda x : len(x))
for i in words:
    print(i)