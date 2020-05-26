#!/usr/bin/python3
"""N queens
    """


from sys import argv


class chezz_table:
    """N queens
        """

    def __init__(self, N):
        chezz_tab = []
        for i in range(N):
            row = []
            for j in range(N):
                row.append(0)
            chezz_tab.append(row)
        self.N = N
        self.table = chezz_tab
        self.end = 0
        self.num_queens = 0

    def add_first_queen(self, x, y):
        self.table[x][y] = 1
        self.num_queens += 1
        self.add_block_spaces(x, y)

    def add_queen(self):
        for i in range(self.N):
            for j in range(self.N):
                if self.table[i][j] == 0:
                    self.table[i][j] = 1
                    self.num_queens += 1
                    self.add_block_spaces(i, j)
                    return
        self.end = 1

    def add_block_spaces(self, ii, jj):
        for i in range(self.N):
            for j in range(self.N):
                if bool(i == ii) != bool(j == jj):
                    self.table[i][j] = 2
                if abs(ii - i) == abs(jj - j) and ii != i:
                    self.table[i][j] = 2


if len(argv) != 2:
    print("Usage: nqueens N")
    exit(1)

N = argv[1]
if not N.isdigit():
    print("N must be a number")
    exit(1)

N = int(N)
if N < 4:
    print("N must be at least 4")
    exit(1)

solutions = []
cont = 0
for x in range(N):
    for y in range(N):
        solutions.append(chezz_table(N))
        solutions[cont].add_first_queen(x, y)
        while solutions[cont].end == 0:
            solutions[cont].add_queen()
        # print(solutions[cont].table)
        cont += 1

max = 0
for i in range(cont):
    if solutions[i].num_queens > max:
        max = solutions[i].num_queens
print(max)
for i in range(cont):
    if solutions[i].num_queens == max:
        print(solutions[i].table)
