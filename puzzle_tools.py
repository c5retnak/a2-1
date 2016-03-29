"""
Some functions for working with puzzles
"""
from puzzle import Puzzle
from collections import deque
# set higher recursion limit
# which is needed in PuzzleNode.__str__
# uncomment the next two lines on a unix platform, say CDF
# import resource
# resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
import sys
sys.setrecursionlimit(10**6)

def depth_first_solve(puzzle):
    """
    Return a path from PuzzleNode(puzzle) to a PuzzleNode containing
    a solution, with each child containing an extension of the puzzle
    in its parent.  Return None if this is not possible.

    @type puzzle: Puzzle
    @rtype: PuzzleNode
    """
    return depth_first_search(puzzle, set())

def depth_first_search(puzzle, visited):
    """
    Perform a depth first search of this puzzle and its respective extensions,
    returning a PuzzleNode of this puzzle containing a path to a solution. If
    no solution exists, return None.

    @type puzzle: Puzzle
    @type visited: set
    @rtype: PuzzleNode | None
    """
    extensions = puzzle.extensions()
    if puzzle.is_solved():
        return PuzzleNode(puzzle)
    elif not extensions or puzzle.fail_fast():
        return None
    else:
        visited.add(str(puzzle))
        for extension in extensions:
            if not str(extension) in visited:
                search = depth_first_search(extension, visited)
                if search is not None:
                    return PuzzleNode(puzzle, [search])

# TODO
# implement breadth_first_solve
# do NOT change the type contract
# you are welcome to create any helper functions
# you like
# Hint: you may find a queue useful, that's why
# we imported deque
def breadth_first_solve(puzzle):
    """
    Return a path from PuzzleNode(puzzle) to a PuzzleNode containing
    a solution, with each child PuzzleNode containing an extension
    of the puzzle in its parent.  Return None if this is not possible.

    @type puzzle: Puzzle
    @rtype: PuzzleNode
    """

    pn = PuzzleNode(puzzle, [])
    # Adds all the extensions in level-order and excludes repeated cases.
    possible_sols = pn.extensions()
    while not level_nodes.is_empty():
        # Checks the possible extensions
        node = possible_sols.pop(0)
        if unseen(node, seen_list=set()):
            # If it is a solution, it returns the PuzzleNode so that
            # PuzzleNode.children contains the solution.
            if node.is_solved():
                pn.children.append(node)
                return pn
            else:
                return pn.children.append(breadth_first_solve(node))
    # If the possible_sols is empty, it means no solution was returned and
    # found.
    return None


# Class PuzzleNode helps build trees of PuzzleNodes that have
# an arbitrary number of children, and a parent.
class PuzzleNode:
    """
    A Puzzle configuration that refers to other configurations that it
    can be extended to.
    """

    def __init__(self, puzzle=None, children=None, parent=None):
        """
        Create a new puzzle node self with configuration puzzle.

        @type self: PuzzleNode
        @type puzzle: Puzzle | None
        @type children: list[PuzzleNode]
        @type parent: PuzzleNode | None
        @rtype: None
        """
        self.puzzle, self.parent = puzzle, parent
        if children is None:
            self.children = []
        else:
            self.children = children[:]

    def __eq__(self, other):
        """
        Return whether PuzzleNode self is equivalent to other

        @type self: PuzzleNode
        @type other: PuzzleNode | Any
        @rtype: bool

        >>> from word_ladder_puzzle import WordLadderPuzzle
        >>> pn1 = PuzzleNode(WordLadderPuzzle("on", "no", {"on", "no", "oo"}))
        >>> pn2 = PuzzleNode(WordLadderPuzzle("on", "no", {"on", "oo", "no"}))
        >>> pn3 = PuzzleNode(WordLadderPuzzle("no", "on", {"on", "no", "oo"}))
        >>> pn1.__eq__(pn2)
        True
        >>> pn1.__eq__(pn3)
        False
        """
        return (type(self) == type(other) and
                self.puzzle == other.puzzle and
                all([x in self.children for x in other.children]) and
                all([x in other.children for x in self.children]))

    def __str__(self):
        """
        Return a human-readable string representing PuzzleNode self.
        # doctest not feasible.
        """
        return "{}\n\n{}".format(self.puzzle,
                                 "\n".join([str(x) for x in self.children]))
