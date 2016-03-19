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
        assert len(marker) > 0
        assert all([len(x) == len(marker[0]) for x in marker[1:]])
        assert all([all(x in marker_set for x in row) for row in marker])
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
            if j != len(self._marker):
                gpsp += "\n"
        return gpsp

    def __repr__(self):
        pass

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

        # convenient name
        all_spots = self._marker

        lex = []

        return lex

    # create empty_space_list
        # [spot[r][c], ...]
    # for every spot in empty_space_list
        # above: if spot[r-2][c] exists and not # and spot[r-1][c] not in empty_space_list
        # below: if spot[r+2][c] exists and not # and spot[r+1][c] not .
        # left: if spot[r][c-2] exists and not # "
        # right: if spot[r][c+2] exists and not # "
            # create new grid, then add it
            # lex.append(GridPegSolitaire())


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
