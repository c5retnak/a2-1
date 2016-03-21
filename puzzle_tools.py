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


# TODO
# implement depth_first_solve
# do NOT change the type contract
# you are welcome to create any helper functions
# you like
def depth_first_solve(puzzle):
    """
    Return a path from PuzzleNode(puzzle) to a PuzzleNode containing
    a solution, with each child containing an extension of the puzzle
    in its parent.  Return None if this is not possible.

    @type puzzle: Puzzle
    @rtype: PuzzleNode
    """


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

    # Adds all the extensions in level-order and excludes repeated cases.
    possible_sols = unique_extensions(puzzle)
    while not possible_sols.is_empty():
        # Checks the possible extensions
        node = possible_sols.popleft()
        # If it is a solution, it returns the PuzzleNode so that PuzzleNode.children contains the solution.
        if node.is_solved():
            puzzle.children.append(node)
            return puzzle
        # If it is not, it adds the PuzzleNode it just checked anyways, so that if the solution is found in the future
        # it remembers the path to it
        else:
            puzzle.children.append(node)
    # If the possible_sols is empty, it means no solution was returned and found.
    return None

def unique_extensions(puzzle):
    """
    @param puzzle: Puzzle
    @rtype: deque
    """

    # Create a new Queue
    uniques_extns = deque()
    # Base case: if there are no more extensions, add the PuzzleNode if it's not already in the Queue.
    if not puzzle.extensions():
        uniques_extns.append(puzzle) if puzzle not in uniques_extns
    # Recursive case: if there are extensions, run the function on each PuzzleNode in the set of extensions.
    # J: problem, is it going to do it by level order or through depth?
    else:
        unique_extensions(node) for node in puzzle.extensions

    return uniques_extns

def is_empty(nodes):
    """
    Return whether nodes is empty.
    Modified from lecture.

    @type nodes: deque[PuzzleNode]
    @rtype: Bool
    """

    return len(nodes) == 0


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
