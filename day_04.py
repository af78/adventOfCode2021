"""You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see any
sunlight. What you can see, however, is a giant squid that has attached itself to the outside of your submarine.

Maybe it wants to play bingo?

Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random,
and the chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.) If all
numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)

The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. It
automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). For
example:

7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7

After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no winners, but the boards are marked as
follows (shown here adjacent to each other to save space):

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are still no winners:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

Finally, 24 is drawn:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

At this point, the third board wins because it has at least one complete row or column of marked numbers (in this case, the entire top row is marked: 14 21 17 24 4).

The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board;
in this case, the sum is 188. Then, multiply that sum by the number that was just called when the board won, 24,
to get the final score, 188 * 24 = 4512.

To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if
you choose that board? """
import numpy as np

input_file =  "input_day_04.txt"
#input_file = "input_day_04_test.txt"

with open(input_file) as fp:
    sequence = fp.readline().split(',')
    fp.readline()

    count = 0
    boards = []
    board = []
    board_num = 0

    for line in fp:
        board = board + line.split()
        if count == 4:
            count = 0
            nparray = np.array(board).reshape((5, 5))
            boards.append([board_num, nparray])
            board = []
            fp.readline()
            board_num = board_num + 1
        else:
            count = count + 1

    print(boards)
    print(sequence)

    marks = [{"win" : False, "mask": np.zeros((5, 5))} for i in range(len(boards))]


    def calculate_score(board, mark, number):
        it = np.nditer(board, flags=['multi_index'])
        sum = 0
        for value in it:
            if mark[it.multi_index] == 0:
                sum = sum + int(value)
        score = sum * int(number)
        return (score)

    scores = []

    for draw in sequence:
        for board in boards:
            board_num    = board[0]
            board_values = board[1]
            if not(marks[board_num]["win"]):
                it = np.nditer(board_values, flags=['multi_index'])
                for value in it:
                    if value == draw:
                        marks[board_num]["mask"][it.multi_index[0]][it.multi_index[1]] = 1
                        if np.all(marks[board_num]["mask"][it.multi_index[0], :] == 1) or np.all(
                            marks[board_num]["mask"][:, it.multi_index[1]] == 1):
                            print("Bingo! {}".format(draw))
                            print("Board num: {}".format(board_num))
                            marks[board_num]["win"] = 1
                            scores.append([calculate_score(board_values, marks[board_num]["mask"], draw), board_num])


    print("score {}".format(scores))

    print("The last board to win is: {} with score {}".format(scores[-1][1] + 1, scores[-1][0]))
    # print(mark)
