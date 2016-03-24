from puzzle import Puzzle


class WordLadderPuzzle(Puzzle):
    """
    A word-ladder puzzle that may be solved, unsolved, or even unsolvable.
    """

    def __init__(self, from_word, to_word, ws):
        """
        Create a new word-ladder puzzle with the aim of stepping
        from from_word to to_word using words in ws, changing one
        character at each step.

        @type from_word: str
        @type to_word: str
        @type ws: set[str]
        @rtype: None
        """
        (self._from_word, self._to_word, self._word_set) = (from_word,
                                                            to_word, ws)
        # set of characters to use for 1-character changes
        self._chars = "abcdefghijklmnopqrstuvwxyz"

    def __eq__(self, other):
        """
        Return whether WordLadderPuzzle self is equivalent to other.

        @type self: WordLadderPuzzle
        @type other: WordLadderPuzzle
        @rtype: bool

        >>> ladder_1 = WordLadderPuzzle("case", "cape", {"case", "cape"})
        >>> ladder_2 = WordLadderPuzzle("case", "cape", {"case", "cape"})
        >>> ladder_1 == ladder_2
        True
        >>> ladder_3 = WordLadderPuzzle("cane", "cape", {"cane", "cape"})
        >>> ladder_1 == ladder_3
        False
        """
        return (type(self) == type(other) and
                self._from_word == other._from_word and
                self._to_word == other._to_word and
                self._word_set == other._word_set)

    def __str__(self):
        """
        Return a string representation of WordLadderPuzzle self.

        @type self: WordLadderPuzzle
        @rtype: str

        >>> ladder_1 = WordLadderPuzzle("case", "cape", {"case", "cape"})
        >>> print(ladder_1)
        case -> cape
        """
        return "{} -> {}".format(self._from_word, self._to_word)

    def __repr__(self):
        """
        Return representation of WordLadderPuzzle self as a string that
        can be evaluated into an equivalent WordLadderPuzzle.

        @type self: WordLadderPuzzle
        @rtype: str

        >>> ladder_1 = WordLadderPuzzle("case", "case", {"case"})
        >>> ladder_1
        WordLadderPuzzle("case", "case", {'case'})
        """
        return "WordLadderPuzzle(\"{}\", \"{}\", {})".format(self._from_word,
                                                             self._to_word,
                                                             self._word_set)

    def extensions(self):
        """
        Return a list of legal extensions of WordLadderPuzzle self.

        @type self: WordLadderPuzzle
        @rtype: list[WordLadderPuzzle]

        >>> legal_words = {"cape", "cope", "tape", "tare"}
        >>> ladder_1 = WordLadderPuzzle("cape", "cope", legal_words)
        >>> extensions = ladder_1.extensions()
        >>> comparison = [WordLadderPuzzle("cope", "cope", legal_words)]
        >>> comparison += [WordLadderPuzzle("tape", "cope", legal_words)]
        >>> len(extensions) == len(comparison)
        True
        >>> all([puzzle in extensions for puzzle in comparison])
        True
        >>> all([puzzle in comparison for puzzle in extensions])
        True
        """
        # Variable declarations for convenience.
        from_word, to_word, set_, chars = (self._from_word, self._to_word,
                                           self._word_set, self._chars)
        if from_word == to_word or len(from_word) != len(to_word):
            return []
        # Generate a list of all legal words that are possible to reach by
        # changing one character in the from_word of this WordLadderPuzzle.
        else:
            legal_words = []
            for i in range(len(from_word)):
                trial_words = [(from_word[:i] + char + from_word[i + 1:]) for
                               char in (set(chars) - set(from_word[i]))]
                legal_words += [word for word in trial_words if word in set_]
        return [WordLadderPuzzle(from_, to_word, set_) for from_ in legal_words]

    def is_solved(self):
        """
        Return True if the from_word in this WordLadderPuzzle is the to_word.
        Otherwise, the puzzle is unsolved.

        @type self: WordLadderPuzzle
        @rtype: bool

        >>> ladder_1 = WordLadderPuzzle("ape", "ace", {"ape", "ace"})
        >>> ladder_1.is_solved()
        False
        >>> ladder_2 = WordLadderPuzzle("ace", "ace", {"ape", "ace"})
        >>> ladder_2.is_solved()
        True
        """
        return True if self._from_word == self._to_word else False


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    from puzzle_tools import breadth_first_solve, depth_first_solve
    from time import time
    with open("words", "r") as words:
        word_set = set(words.read().split())
    w = WordLadderPuzzle("same", "cost", word_set)
    start = time()
    sol = breadth_first_solve(w)
    end = time()
    print("Solving word ladder from same->cost")
    print("...using breadth-first-search")
    print("Solutions: {} took {} seconds.".format(sol, end - start))
    start = time()
    sol = depth_first_solve(w)
    end = time()
    print("Solving word ladder from same->cost")
    print("...using depth-first-search")
    print("Solutions: {} took {} seconds.".format(sol, end - start))
