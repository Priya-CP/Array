
import sys

scores = list(map(int, sys.argv[1:]))

n = len(scores)
total = sum(scores)
average = total / n
maximum = max(scores)
minimum = min(scores)

print("Scores:", scores)
print("Sum of scores:", total)
print("Average of scores:", average)
print("Maximum score:", maximum)
print("Minimum score:", minimum)
