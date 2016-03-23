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

        >>> l1 = WordLadderPuzzle("case", "cape", {"case", "cape"})
        >>> l2 = WordLadderPuzzle("case", "cape", {"case", "cape"})
        >>> l1 == l2
        True
        >>> l3 = WordLadderPuzzle("cane", "cape", {"cane", "cape"})
        >>> l1 == l3
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

        >>> l1 = WordLadderPuzzle("case", "cape", {"case", "cape"})
        >>> print(ladder1)
        case -> cape
        """
        return "{} -> {}".format(self._from_word, self._to_word)

    def __repr__(self):
        """
        Return representation of WordLadderPuzzle self as a string that
        can be evaluated into an equivalent WordLadderPuzzle.

        @type self: WordLadderPuzzle
        @rtype: str

        >>> l1 = WordLadderPuzzle("case", "case", {'case'})
        >>> l1
        WordLadderPuzzle("case", "case", {'case'})
        """
        return "WordLadderPuzzle(\"{}\", \"{}\", {})".format(self._from_word,
                                                             self._to_word,
                                                             self._word_set)

        # TODO
        # override extensions
        # legal extensions are WordLadderPuzzles that have a from_word that can
        # be reached from this one by changing a single letter to one of those
        # in self._chars
    def extensions(self):
        """
        Return a list of extensions of WordLadderPuzzle self.

        @type self: WordLadderPuzzle
        @rtype: list[WordLadderPuzzle]

        >>> l1 = WordLadderPuzzle("ape", "ace", {"ape", "ace"})
        >>> extensions = l1.extensions()
        >>> comparison = [WordLadderPuzzle("ace", "ace", {"ape", "ace"})]
        >>> len(extensions) == len(comparison)
        True
        >>> all([l in comparison for l in extensions])
        True
        >>> all([l in extensions for l in comparison])
        True
        """
        from_word, to_word, word_set, chars = self._from_word, self._to_word, \
                                              self._word_set, self._chars
        if from_word == to_word:
            return []
        else:
            legal_words = []
            i = 0
            for i in range(len(from_word)):
                # If character at the given index does not match between the
                # words, determine legal words that can be changed by one letter.
                if not from_word[i] == to_word[i]:
                    arraigned_words = [from_word[:i] + char + from_word[i + 1:] for char in (set(chars) - set(from_word[i]))]
                    legal_words += [word for word in arraigned_words if word in self._word_set]
        return [WordLadderPuzzle(ext, to_word, word_set) for ext in legal_words]

        # TODO
        # override is_solved
        # this WordLadderPuzzle is solved when _from_word is the same as
        # _to_word
    def is_solved(self):
        """
        Return True if WordLadderPuzzle self is sovled. Otherwise return False.

        @type self: WordLadderPuzzle
        @rtype: bool

        >>> l1 = WordLadderPuzzle("ape", "ace", {"ape", "ace"})
        >>> l1.is_solved()
        False
        >>> l2 = WordLadderPuzzle("ace", "ace", {"ape", "ace"})
        >>> l2.is_solved()
        True
        """
        if self._from_word == self._to_word:
            return True
        else:
            return False


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
