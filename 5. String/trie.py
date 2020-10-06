class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curNode = self.root
        for c in word:
            if c not in curNode.children:
                curNode.children[c] = Node()
            curNode = curNode.children[c]
        curNode.isWord = True

    def search(self, word: str) -> bool:
        curNode = self.root
        for c in word:
            if c not in curNode.children:
                return False
            curNode = curNode.children[c]
        return curNode.isWord

    def startsWith(self, prefix: str) -> bool:
        curNode = self.root
        for c in prefix:
            if c not in curNode.children:
                return False
            curNode = curNode.children[c]
        return True
