name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]


miss = dict(zip(name, yearning))

answer = []
for i in photo:
    score = 0
    for j in i:
        tmp = miss.get(j)
        if tmp:
            score += tmp
    answer.append(score)
print(answer)