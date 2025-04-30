from collections.abc import Iterator


class WordIterator(Iterator):

    def __init__(self, words):
        self._position = 0
        self.words = words

    def __next__(self):
        try:
            value = self.words[self._position]
            self._position += 1
            return value

        except IndexError:
            raise StopIteration()


class Menu:
    def __init__(self) -> None:
        self.words = []

    def __getitem__(self, index):
        return self.words[index]

    def __iter__(self) -> WordIterator:
        return WordIterator(self)

    def additem(self, word):
        self.words.append(word)


menu = Menu()
menu.additem("pizza")
menu.additem("rice")
menu.additem("pasta")
menu.additem("fish")
menu.additem("meat")
menu.additem("idiot")


# __iter__ method is there for any iterator action would be taken

for item in menu:
    print(item)

print("-".join(menu))
