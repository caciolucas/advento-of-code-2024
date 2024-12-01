l1 = []
l2 = []

with open("input.txt", "r") as f:
    for l in f.readlines():
        n1, n2 = l.split("   ")
        l1.append(int(n1))
        l2.append(int(n2))

l1.sort()
l2.sort()

distance = 0

for i in range(len(l1)):
    distance += abs(l1[i] - l2[i])

print(distance)

checked_numbers = []
similarity = 0
for i in range(len(l2)):
    n = l2[i]
    if n in l1 and n not in checked_numbers:
        similarity += n * l2.count(n)
        checked_numbers.append(n)

print(similarity)
