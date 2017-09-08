from node import Node


class Trie:
    def __init__(self):
        self.root = Node("")
        self.show_list = []

    def delete(self):
        self.__init__()

    def insert(self, string):
        node = self.root
        for char in string+"$":
            if char not in node.children:
                node.children[char] = Node(char)
            node = node.children[char]

    def show(self):
        self._show(self.root)

    def _show(self, node):
        for child in node.children:
            if node.children[child].char == "$":
                print("".join(self.show_list))
            self.show_list.append(node.children[child].char)
            self._show(node.children[child])
            del self.show_list[-1]

if __name__ == "__main__" :
    trie = Trie()
    trie.insert("baby")
    trie.insert("bad")
    trie.insert("bank")
    trie.insert("box")
    trie.insert("dog")
    trie.insert("dogs")
    trie.insert("banks")
    trie.show()
