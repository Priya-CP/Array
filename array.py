
scores = []

n = int(input("Enter number of scores: "))

for i in range(n):
    score = float(input("Enter score: "))
    scores.append(score)

total = sum(scores)
average = total / n

print("Scores:", scores)
print("Sum of scores:", total)
print("Average of scores:", average)
