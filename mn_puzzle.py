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

        >>> from_grid = (("1", "2", "3"), ("4", "5", "*"))
        >>> to_grid = (("*", "2", "3"), ("1", "4", "5"))
        >>> mn1 = MNPuzzle(from_grid, to_grid)
        >>> extensions = mn1.extensions()
        >>> from_grid = (("1", "2", "*"), ("4", "5", "3"))
        >>> mn2 = MNPuzzle(from_grid, to_grid)
        >>> from_grid = (("1", "2", "3"), ("4", "*", "5"))
        >>> mn3 = MNPuzzle(from_grid, to_grid)
        >>> comparisons = [mn2, mn3]
        >>> len(extensions) == len(comparisons)
        True
        >>> all([puzzle in extensions for puzzle in comparisons])
        True
        >>> all([puzzle in comparisons for puzzle in extensions])
        True
        """
        # Convenient names.
        from_grid, to_grid = self.from_grid, self.to_grid
        if all(["*" not in row for row in from_grid]):
            # Return an empty list.
            return [_ for _ in []]
        else:
            legal_slides = []
            for row in range(len(self.n)):
                # If the given marker is the empty block, check for swaps.
                if "*" in from_grid[row]:
                    col = from_grid[row].index("*")
                    # If this empty block has a block above it, swap the blocks.
                    if (row - 1) >= 0:
                        above_block = from_grid[row - 1][col]
                        copy = [list(r) for r in from_grid]
                        copy[row - 1][col] = "*"
                        copy[row][col] = above_block
                        tuples = [tuple(x) for x in copy]
                        legal_slides.append(tuples)
                    # Do the same as above, but with below the given block.
                    if (row + 1) < len(from_grid):
                        below_block = from_grid[row + 1][col]
                        swap_down_grid = [row.copy() for row in from_grid]
                        swap_down_grid[row][col] = "."
                        swap_down_grid[row + 1][col] = "."
                        swap_down_grid[row + 2][col] = "*"
                        legal_slides.append(swap_down_grid)
                    # Swap if this empty block has a block to its left.
                    if (col - 1) >= 0:
                        left_block = from_grid[row][col - 1]
                        swap_left_grid = [[peg for peg in row] for row in from_grid]
                        swap_left_grid[row][col] = "."
                        swap_left_grid[row][col - 1] = "."
                        swap_left_grid[row][col - 2] = "*"
                        legal_slides.append(swap_left_grid)
                    # Do the same as above, but with the right.
                    if (col + 1) < len(from_grid[row]):
                        right_block = from_grid[row][col + 1]

                        swap_right_grid = [[peg for peg in row] for row in from_grid]
                        swap_right_grid[row][col] = "."
                        swap_right_grid[row][col + 1] = "."
                        swap_right_grid[row][col + 2] = "*"
                        legal_slides.append(swap_right_grid)
        return [MNPuzzle(new_grid, to_grid) for new_grid in legal_slides]
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
