from puzzle import Puzzle


class MNPuzzle(Puzzle):
    """
    An nxm puzzle, like the 15-puzzle, which may be solved, unsolved,
    or even unsolvable.
    """

    def __init__(self, from_grid, to_grid):
        """
        MNPuzzle in state from_grid, working towards
        state to_grid

        @param MNPuzzle self: this MNPuzzle
        @param tuple[tuple[str]] from_grid: current configuration
        @param tuple[tuple[str]] to_grid: solution configuration
        @rtype: None
        """
        # represent grid symbols with letters or numerals
        # represent the empty space with a "*"
        assert len(from_grid) > 0
        assert all([len(r) == len(from_grid[0]) for r in from_grid])
        assert all([len(r) == len(to_grid[0]) for r in to_grid])
        # J: setting a variable for row and col
        self.n, self.m = len(from_grid), len(from_grid[0])
        self.from_grid, self.to_grid = from_grid, to_grid

    def __eq__(self, other):
        """
        Return whether MNPuzzle self is equivalent to other.

        @type self: MNPuzzle
        @type other: MNPuzzle | Any
        @rtype: bool

        >>> grid1 = (("1", "2", "3"), ("4", "5", "*"))
        >>> grid2 = (("*", "2", "3"), ("1", "4", "5"))
        >>> mn1 = MNPuzzle(grid1, grid2)
        >>> grid3 = (("1", "2", "3"), ("4", "5", "*"))
        >>> grid4 = (("*", "2", "3"), ("1", "4", "5"))
        >>> mn2 = MNPuzzle(grid3, grid4)
        >>> mn1 == mn2
        True
        >>> mn3 = MNPuzzle(grid3, grid1)
        >>> mn1 == mn3
        False
        """

        return ((type(self) == type(other)) and
                (self.from_grid == other.from_grid) and
                (self.to_grid == other.to_grid))

    def __str__(self):
        """
        Return a human-readable string representation of MNPuzzle self.

        >>> grid1 = (("1", "2", "3"), ("4", "5", "*"))
        >>> grid2 = (("*", "2", "3"), ("1", "4", "5"))
        >>> mn = MNPuzzle(grid1, grid2)
        >>> print(mn)
        123
        45*
        """

        mn = ""
        j = 0
        for row in self.from_grid:
            j += 1
            for i in range(len(row)):
                mn += row[i]
            # to remove the <BLANKLINE> at the end
            if j != len(self.from_grid):
                mn += "\n"
        return mn

    def extensions(self):
        """
        Return list of legal extensions of MNPuzzle self.

        @type self: MNPuzzle
        @rtype: list[MNPuzzle]
        """

        # convenient names
        from_grid, to_grid = self.from_grid, self.to_grid
        for j in range(len(from_grid)):
            if "*" in from_grid[j]:
                # position of first empty position
                i = from_grid[j].index("*")
            # J :need to check bounds and figure out how to switch the symbols
            allowed_symbols = (tuple(from_grid[j-1][i]), tuple(from_grid[j+1][i]),
                               tuple(from_grid[j][i+1]), tuple(from_grid[j][i-1]))
            return ([MNPuzzle(from_grid[:j][:i] + d + from_grid[:j][i + 1:], to_grid)
                 for d in allowed_symbols])

        # def find_space(self):
        #     """
        #     Returns the [row, col] of the space.
        #
        #     @type self: MNPuzzle
        #     @rype: list[int]
        #     """
        #
        #     j = 0
        #     for row in self.from_grid:
        #         j += 1
        #         for i in range(len(row)):
        #             if row[i] == "*":
        #                 return [j, i]
        #     return "Error: no space found"

        # lex = []
        # cur_grid = []
        # col = None
        # row = 0
        # while col != None and row < len(self.from_grid):
        #     if "*" in self.from_grid[row]:
        #         col = self.from_grid[row].index("*")
        #     row += 1
        #     cur_grid.append(list(row))

        #if changes not > len(self.m or self.n)
        #up , change from_grid [j+1, i] and add it to coor list
        #down, change from_grid [j-1, i] and add it to coor list
        #right, change from_grid [j, i-1] and add it to coor list
        #left, change from_grid [j, i+1] and add it to coor list

        #for each location in the coor list
        #change cur_grid, add it to lex

        # return lex

    def is_solved(self):
        """
        Return True iff MNPuzzle self is solved.

        @type self: MNPuzzle
        @rtype: bool

        >>> grid1 = (("1", "2", "3"), ("4", "5", "*"))
        >>> grid2 = (("*", "2", "3"), ("1", "4", "5"))
        >>> mn1 = MNPuzzle(grid1, grid2)
        >>> mn1.is_solved()
        False
        >>> grid3 = (("1", "2", "3"), ("4", "5", "*"))
        >>> mn3 = MNPuzzle(grid3, grid1)
        >>> mn3.is_solved()
        True

        """

        return self.from_grid == self.to_grid


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    target_grid = (("1", "2", "3"), ("4", "5", "*"))
    start_grid = (("*", "2", "3"), ("1", "4", "5"))
    m = MNPuzzle(start_grid, target_grid)
    m.extensions()
    # from puzzle_tools import breadth_first_solve, depth_first_solve
    # from time import time
    # start = time()
    # solution = breadth_first_solve(MNPuzzle(start_grid, target_grid))
    # end = time()
    # print("BFS solved: \n\n{} \n\nin {} seconds".format(
    #     solution, end - start))
    # start = time()
    # solution = depth_first_solve((MNPuzzle(start_grid, target_grid)))
    # end = time()
    # print("DFS solved: \n\n{} \n\nin {} seconds".format(
    #     solution, end - start))
