N = input()
generator = 0

for g in range(1, int(N)+1):
  digit_sum = g
  for i in str(g):
    digit_sum += int(i)
  if digit_sum == int(N):
    generator = g
    break

print(generator)