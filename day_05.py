'''You come across a field of hydrothermal vents on the ocean floor! These vents constantly produce large,
opaque clouds, so it would be best to avoid them if possible.

They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents (your puzzle input) for
you to review. For example:

0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2

Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end
the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends.
In other words:

    An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
    An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.

For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

So, the horizontal and vertical lines from the above list would produce the following diagram:

.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....

In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number
of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, comes from
2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.

To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. In
the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.

Consider only horizontal and vertical lines. At how many points do at least two lines overlap?
'''
import numpy as np

input_file = "input_day_05.txt"
X_SIZE = 1000
Y_SIZE = 1000

#input_file = "input_day_05_test.txt"
#X_SIZE = 10
#Y_SIZE = 10

with open(input_file) as fp:
    grid = np.zeros((X_SIZE, Y_SIZE))
    lines = [(line.split()[0].split(","), line.split()[2].split(",")) for line in fp]

    for line in lines:
        coord_a = (int(line[0][0]), int(line[0][1]))
        coord_b = (int(line[1][0]), int(line[1][1]))
        print("coord a: {} , coord b: {}".format(coord_a, coord_b))

        if coord_a[1] == coord_b[1]: # vertical
            segment = [(x, coord_a[1]) for x in range(min(coord_a[0], coord_b[0]), max(coord_a[0], coord_b[0]) + 1)]

        elif coord_a[0] == coord_b[0]: # horizontal
            segment = [(coord_a[0], y) for y in range(min(coord_a[1], coord_b[1]), max(coord_a[1], coord_b[1]) + 1)]

        else: # diagonal 45deg
            if coord_b[0] - coord_a[0] > 0:
                dx = 1
            else:
                dx = -1

            if coord_b[1] - coord_a[1] > 0:
                dy = 1
            else:
                dy = -1

            segment = []
            for inc in range(abs(coord_a[0] - coord_b[0])+1):
                segment.append([coord_a[0] + (dx * inc), coord_a[1] + (dy * inc)])

        print("segment {}".format(segment))
        for point in segment:
           grid[point[1], point[0]] = grid[point[1], point[0]] + 1

        print(grid)

    it = np.nditer(grid)

    sum = 0
    for i in it:
        if i > 1:
            sum = sum + 1

    print ("The sum is: {}".format(sum))