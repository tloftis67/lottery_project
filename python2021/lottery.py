import random

def lotto(start, end,numchoices):
    numlist = []
    while len(numlist) < numchoices:

        number = random.randint(start,end)
        if number not in numlist:
            numlist.append(number)
    numlist.sort()
    return numlist


lottonumbers = lotto(1,30,8)
quickpicks = lotto(1,30,8)

print(lottonumbers)
print(quickpicks)

matching = []
for num in quickpicks:
    if num in lottonumbers:
        matching.append(num)

print(len(matching))


