myarray = [1721, 979, 366, 299, 675, 1456]

# Part 1
def sum2020(n):
    for i in range(len(n) - 1):
        for j in range(i + 1, len(n)):
            if n[i]+n[j] == 2020:
                return n[i]*n[j]

expenses = []
with open('day1.txt', 'r') as f:
    for line in f:
        expenses.append(int(line.strip()))

# print(sum2020(expenses))

# Part 2
def sum2020part2(n):
    for i in range(len(n) - 2):
        for j in range(i + 1, len(n) - 1):
            for k in range(j + 1, len(n)):
                if n[i] + n[j] + n[k] == 2020:
                    return n[i] * n[j] * n[k]

print(sum2020part2(expenses))
