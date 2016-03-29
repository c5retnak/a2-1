from puzzle import Puzzle


class GridPegSolitairePuzzle(Puzzle):
    """
    Snapshot of peg solitaire on a rectangular grid. May be solved,
    unsolved, or even unsolvable.
    """

    def __init__(self, marker, marker_set):
        """
        Create a new GridPegSolitairePuzzle self with
        marker indicating pegs, spaces, and unused
        and marker_set indicating allowed markers.

        @type marker: list[list[str]]
        @type marker_set: set[str]
                          "#" for unused, "*" for peg, "." for empty
        """
        assert isinstance(marker, list)
        # J: making sure it't not an empty board
        assert len(marker) > 0
        # J: making sure all the rows are the same
        assert all([len(x) == len(marker[0]) for x in marker[1:]])
        # J: making sure all the pieces are valid
        assert all([all(x in marker_set for x in row) for row in marker])
        # J: making sure the market set is valid
        assert all([x == "*" or x == "." or x == "#" for x in marker_set])
        self._marker, self._marker_set = marker, marker_set

    def __eq__(self, other):
        """
        Return whether GridPegSolitairePuzzle self is equivalent to other.

        @type self: GridPegSolitairePuzzle
        @type other: GridPegSolitairePuzzle | Any
        @rtype: bool

        >>> grid1 = []
        >>> grid1.append(["*", "*", ".", "*", "*"])
        >>> grid1.append(["*", "*", "*", "*", "*"])
        >>> gpsp1 = GridPegSolitairePuzzle(grid1, {"*", ".", "#"})
        >>> grid2 = []
        >>> grid2.append(["*", "*", ".", "*", "*"])
        >>> grid2.append(["*", "*", "*", "*", "*"])
        >>> gpsp2 = GridPegSolitairePuzzle(grid2, {"*", ".", "#"})
        >>> gpsp1 == gpsp2
        True
        >>> grid3 = []
        >>> grid3.append(["*", "*", "*", "*", "*"])
        >>> grid3.append(["*", "*", ".", "*", "*"])
        >>> gpsp3 = GridPegSolitairePuzzle(grid3, {"*", ".", "#"})
        >>> gpsp1 == gpsp3
        False
        """

        return (type(self) == type(other)
                and (self._marker == other._marker)
                and (self._marker_set == other._marker_set))

    def __str__(self):
        """
        Return a human-readable string representation of GridPegSolitairePuzzle
        self.

        >>> grid = []
        >>> grid.append(["*", "*", ".", "*", "*"])
        >>> grid.append(["*", "*", "*", "*", "*"])
        >>> gpsp = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
        >>> print(gpsp)
        **.**
        *****
        """
        gpsp = ""
        j = 0
        for row in self._marker:
            j += 1
            for i in range(len(row)):
                gpsp += row[i]
            # to remove the <BLANKLINE> at the end
            if j != len(self._marker):
                gpsp += "\n"
        return gpsp

    def is_solved(self):
        """
        Return True iff GridPegSolitairePuzzle self is solved.

        @type self: GridPegSolitairePuzzle
        @rtype: bool

        >>> grid_1 = []
        >>> grid_1.append([".", ".", ".", ".", "."])
        >>> grid_1.append([".", ".", "*", ".", "."])
        >>> gpsp1 = GridPegSolitairePuzzle(grid_1, {"*", ".", "#"})
        >>> gpsp1.is_solved()
        True
        >>> grid_2 = []
        >>> grid_2.append(["*", ".", ".", ".", "."])
        >>> grid_2.append([".", ".", "*", ".", "."])
        >>> gpsp2 = GridPegSolitairePuzzle(grid_2, {"*", ".", "#"})
        >>> gpsp2.is_solved()
        False
        """
        all_markers  = sum(self._marker, [])
        return all_markers.count("*") == 1

    def extensions(self):
        """
        Return list of legal extensions of GridPegSolitairePuzzle self.

        @type self: GridPegSolitairePuzzle
        @rtype: list[GridPegSolitairePuzzle]

        >>> mset = {"*", ".", "#"}
        >>> grid_1 = [["*", "*", ".", "*", "*"]]
        >>> grid_1.append(["*", "*", "*", "*", "*"])
        >>> gpsp1 = GridPegSolitairePuzzle(grid_1, mset)
        >>> extensions = list(gpsp1.extensions())
        >>> left_jump = [["*", "*", "*", ".", "."]]
        >>> left_jump.append(["*", "*", "*", "*", "*"])
        >>> gpsp2 = GridPegSolitairePuzzle(left_jump, mset)
        >>> right_jump = [[".", ".", "*", "*", "*"]]
        >>> right_jump.append(["*", "*", "*", "*", "*"])
        >>> gpsp3 = GridPegSolitairePuzzle(right_jump, mset)
        >>> comparisons = [gpsp2, gpsp3]
        >>> len(extensions) == len(comparisons)
        True
        >>> all([puzzle in extensions for puzzle in comparisons])
        True
        >>> all([puzzle in comparisons for puzzle in extensions])
        True
        >>> grid_2 = [["*", "*"]]
        >>> grid_2.append(["*", "*"])
        >>> grid_2.append([".", "*"])
        >>> grid_2.append(["*", "*"])
        >>> grid_2.append(["*", "*"])
        >>> gps1 = GridPegSolitairePuzzle(grid_2, mset)
        >>> extensions = gps1.extensions()
        >>> up_jump = [["*", "*"]]
        >>> up_jump.append(["*", "*"])
        >>> up_jump.append(["*", "*"])
        >>> up_jump.append([".", "*"])
        >>> up_jump.append([".", "*"])
        >>> gpsp4 = GridPegSolitairePuzzle(up_jump, mset)
        >>> down_jump = [[".", "*"]]
        >>> down_jump.append([".", "*"])
        >>> down_jump.append(["*", "*"])
        >>> down_jump.append(["*", "*"])
        >>> down_jump.append(["*", "*"])
        >>> gpsp5 = GridPegSolitairePuzzle(down_jump, mset)
        >>> comparisons = [gpsp4, gpsp5]
        >>> len(extensions) == len(comparisons)
        True
        >>> all([puzzle in extensions for puzzle in comparisons])
        True
        >>> all([puzzle in comparisons for puzzle in extensions])
        True
        """

        # Convenient names.
        marker, marker_set = self._marker, self._marker_set
        if sum([row.count("*") for row in marker]) == 1 or all(["." not in row
                                                                for row in
                                                                marker]):
            # Return an empty list.
            return [_ for _ in []]
        else:
            legal_jumps = _available_jumps(self._marker)
            # For each piece in board, if there is an available jump add the
            # list[list[str]] to jumps.
            return [GridPegSolitairePuzzle(new_grid, marker_set) for
                    new_grid in legal_jumps]


def _available_jumps(grid):
    """

    Returns a list of boards that you can attain with the legal jumps.

    @type grid: list[list[str]]
    @rtype: list[list[list[str]]]

    >>> grid_1 = []
    >>> grid_1.append(['*', '*', '.', '*', '*'])
    >>> grid_1.append(['*', '*', '*', '*', '*'])
    >>> _available_jumps(grid_1)
    [[['.', '.', '*', '*', '*'], ['*', '*', '*', '*', '*']], [['*', '*', '*', '.', '.'], ['*', '*', '*', '*', '*']]]

    """
    new_grids = []
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            # If the given marker is a peg, check for available moves.
            if grid[row][col] == "*":
                # If this peg has a peg above it, and that peg has an empty
                # spot above it, this peg can jump 2 spots up.
                if ((row - 2) >= 0 and grid[row - 2][col] == "." and
                        grid[row - 1][col] == "*"):
                        jump_up_grid = [row.copy() for row in grid]
                        jump_up_grid[row][col] = "."
                        jump_up_grid[row - 1][col] = "."
                        jump_up_grid[row - 2][col] = "*"
                        new_grids.append(jump_up_grid)
                # Do the same as above, but with below the given peg.
                if ((row + 2) < len(grid) and grid[row + 2][col] == "." and
                        grid[row + 1][col] == "*"):
                        jump_down_grid = [row.copy() for row in grid]
                        jump_down_grid[row][col] = "."
                        jump_down_grid[row + 1][col] = "."
                        jump_down_grid[row + 2][col] = "*"
                        new_grids.append(jump_down_grid)
                # If this peg has a peg to its left, and that peg has a an
                # empty spot to its left, this peg can jump 2 spots left.
                if ((col - 2) >= 0 and grid[row][col - 2] == "." and
                        grid[row][col - 1] == "*"):
                        jump_left_grid = [[peg for peg in row] for row in grid]
                        jump_left_grid[row][col] = "."
                        jump_left_grid[row][col - 1] = "."
                        jump_left_grid[row][col - 2] = "*"
                        new_grids.append(jump_left_grid)
                # Do the same as above, but with the right.
                if ((col + 2) < len(grid[row]) and grid[row][col + 2] == "." and
                        grid[row][col + 1] == "*"):
                        jump_right_grid = [[peg for peg in row] for row in grid]
                        jump_right_grid[row][col] = "."
                        jump_right_grid[row][col + 1] = "."
                        jump_right_grid[row][col + 2] = "*"
                        new_grids.append(jump_right_grid)
    return new_grids


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    from puzzle_tools import depth_first_solve

    grid = [["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"],
            ["*", "*", ".", "*", "*"],
            ["*", "*", "*", "*", "*"]]
    gpsp = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
    import time

    start = time.time()
    solution = depth_first_solve(gpsp)
    end = time.time()
    print("Solved 5x5 peg solitaire in {} seconds.".format(end - start))
    print("Using depth-first: \n{}".format(solution))
