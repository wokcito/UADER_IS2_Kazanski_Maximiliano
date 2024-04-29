from collections.abc import Iterable, Iterator

class CadenaIterator(Iterator):
    _position: int = None
    _reverse: bool = False

    def __init__(self, chain_of_characters, reverse: bool = False):
        self._chain_of_characters = chain_of_characters
        self._reverse = reverse
        self._position = -1 if reverse else 0
    
    def __next__(self):
        try:
            value = self._chain_of_characters[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value

class CadenaDeCaracteres(Iterable):
    def __init__(self, chain_of_characters):
        self._chain_of_characters = chain_of_characters
    
    def __getitem__(self, index: int):
        return self._chain_of_characters[index]

    def __iter__(self):
        return CadenaIterator(self)
    
    def get_reverse_iterator(self):
        return CadenaIterator(self, True)

string = CadenaDeCaracteres("hola")

print("Directo:")
print("\n".join(string))
print("")

print("Reverso:")
print("\n".join(string.get_reverse_iterator()), end="")