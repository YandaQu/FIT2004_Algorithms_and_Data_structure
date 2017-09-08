from node import Node


class Trie:
    def __init__(self):
        self.root = Node("")
        self.show_list = []
        self.solution = []

    def delete(self):
        self.__init__()

    def insert(self, string):
        node = self.root
        for char in string+"$":
            if char not in node.children:
                node.children[char] = Node(char)
            node = node.children[char]

    def print_out(self,node):
        self.show(node)
        for item in self.solution:
            print(item)
        self.solution = []

    def show(self, node):
        self._show(node)

    def _show(self, node):
        for child in node.children:
            if node.children[child].char == "$":
                self.solution.append("".join(self.show_list))
            self.show_list.append(node.children[child].char)
            self._show(node.children[child])
            del self.show_list[-1]

    def search(self,string):
        node = self.root
        for char in string+"$":
            if char in node.children:
                node = node.children[char]
                if char == "$":
                    return True
            else:
                return False

    def prefix(self, pre):
        node = self.root
        for char in pre:
            if char in node.children:
                node = node.children[char]
            else:
                raise KeyError("prefix not found!")
        self.show(node)
        for item in self.solution:
            print(pre+item)
        self.solution = []

if __name__ == "__main__":
    trie = Trie()
    trie.insert("baby")
    trie.insert("bad")
    trie.insert("bank")
    trie.insert("box")
    trie.insert("dog")
    trie.insert("dogs")
    trie.insert("banks")
    trie.print_out(trie.root)
    print(trie.search("baby"))
    print(trie.search("bad"))
    print(trie.search("bank"))
    print(trie.search("notin"))
    trie.prefix("b")
