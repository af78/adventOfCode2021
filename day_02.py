fp = open("input_02.txt")

x = 0  # horizontal position
d = 0  # depth

for line in fp:
    command = line.split()[0]
    if command == 'forward':
        x = x + int(line.split()[1])
    elif command == 'down':
        d = d + int(line.split()[1])
    elif command == 'up':
        d = d - int(line.split()[1])

print (x, d)
print (x*d)

fp.close()

# part 2
fp = open("input_02.txt")

x = 0  # horizontal position
d = 0  # depth
aim = 0 # aim

for line in fp:
    command = line.split()[0]
    amount = int(line.split()[1])

    if command == 'forward':
        x = x + amount
        d = d + amount * aim
    elif command == 'down':
        aim = aim + amount
    elif command == 'up':
        aim = aim - amount

print (x, d)
print (x*d)
