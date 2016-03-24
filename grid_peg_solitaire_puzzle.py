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
        Return a human-readable string representation of GridPegSolitairePuzzle self.

        >>> grid = []
        >>> grid.append(["*", "*", ".", "*", "*"])
        >>> grid.append(["*", "*", "*", "*", "*"])
        >>> gpsp = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
        >>> print(gpsp)
        **.**
        *****
        """

        # rows = [[row[i] for i in range(len(row))]
        #         for row in self._marker]
        # return "\n".join(rows)

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

        >>> grid = []
        >>> grid.append([".", ".", ".", ".", "."])
        >>> grid.append([".", ".", "*", ".", "."])
        >>> gpsp = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
        >>> gpsp.is_solved()
        True
        """

        return [self._marker[i].count("*") == 1 for i in range(len(self._marker))].count(True) == 1

    def extensions(self):
        """
        Return list of legal extensions of GridPegSolitairePuzzle self.

        @type self: GridPegSolitairePuzzle
        @rtype: list[GridPegSolitairePuzzle]
        """

        # convenient names
        marker, marker_set = self._marker, self._marker_set

        if all(["." not in row for row in marker]):
            # return an empty list
            return [_ for _ in []]
        else:
            jumps = []
            #for each piece in board, if there is an available jump (helper fn)
            #add the list[list[str]] to jumps
            return [GridPegSolitairePuzzle(new_marker, marker_set) for new_marker in jumps]

def available_jump(self):
    """

    @type self: list[list[str]]
    @return: list[list[list[str]]]
    """

    jumps = []
    for row in range(len(self)):
        for col in range(len(self[row])):
            if self[row][col] == "*":
                if (row-2) > -1 and self[row-2][col] == "." and self[row-1][col] == "*":
                    jump1 = self.copy()
                    jump1[row][col], jump1[row-1][col], jump1[row-2][col] = ".", ".", "*"
                    jumps.append(jump1)
                if (col-2) > -1 and self[row][col-2] and self[row][col-1] == "*":
                    jump3 = self.copy()
                    jump3[row][col], jump3[row-1][col], jump3[row-2][col] = ".", ".", "*"
                    jumps.append(jump3)
                if (col+2) < len(self[row]) and self[row][col+2] and self[row][col+1] == "*":
                    jump4 = self.copy()
                    jump4[row][col], jump4[row-1][col], jump4[row-2][col] = ".", ".", "*"
                    jumps.append(jump4)
    return jumps

def jump_up(grid):
    """

    @type grid: list[list[str]]
    @return: list[list[str]]
    """

    if (row+2) < len(self) and self[row+2][col] and self[row+1][col] == "*":
        jump2 = grid.copy()
        jump2[row][col], jump2[row-1][col], jump2[row-2][col] = ".", ".", "*"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    from puzzle_tools import depth_first_solve

    grid = [["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"],
            ["*", "*", ".", "*", "*"],
            ["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"]]
    gpsp = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
    gpsp.extensions()
    # import time
    #
    # start = time.time()
    # solution = depth_first_solve(gpsp)
    # end = time.time()
    # print("Solved 5x5 peg solitaire in {} seconds.".format(end - start))
    # print("Using depth-first: \n{}".format(solution))
