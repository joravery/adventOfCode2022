class Node:
    def __init__(self, i, j, letter) -> None:
        self.letter = letter
        self.coordinates = (i,j)
        self.shortest_path = float('inf')
        self.predecessor = None

    def __str__(self):
        return f"{self.letter} at pos {self.coordinates}, with predecessor: {self.predecessor.letter}, and shortest path: {self.shortest_path}"

    def __repr__(self):
        return self.__str__
