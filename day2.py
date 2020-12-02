mylist = ['1-3 a: abcde', '1-3 c: cdefg', '2-9 c: ccccccccc']


# Part 1
# count = 0
# with open('day2.txt', 'r') as f:
#     for line in f:
#         chop = line.split()
#         minmax = chop[0].split('-')
#         lower = int(minmax[0])
#         upper = int(minmax[1])
#         char = chop[1].strip(':')
#         password = chop[2]
#         if lower <= password.count(char) <= upper:
#             count += 1

# Part 2
count = 0
with open('day2.txt', 'r') as f:
    for line in f:
        chop = line.split()
        minmax = chop[0].split('-')
        pos1 = int(minmax[0])
        pos2 = int(minmax[1])
        char = chop[1].strip(':')
        password = chop[2]
        if (password[pos1-1] == char) ^ (password[pos2-1] == char):
            count += 1

print(count)


