fp = open("input.txt")

num_increments = 0
last_measure = fp.readline()

for current_measure in fp:
    if int(current_measure) > int(last_measure):
        num_increments = num_increments + 1

    last_measure = current_measure

print(num_increments)
fp.close()

# part 2
fp = open("input.txt")

shreg = [0, 0, 0]

num_increments = 0

for i in range(0, 3):
    shreg[i] = int(fp.readline())

for measure in fp:
    if (shreg[1] + shreg[2] + int(measure)) > (shreg[0] + shreg[1] + shreg[2]):
        num_increments = num_increments + 1
    shreg[0:2] = shreg[1:3]
    shreg[2] = int(measure)


print(num_increments)