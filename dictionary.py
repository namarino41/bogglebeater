from lib.trie import Trie

class Dictionary:
    def __init__(self, dictionaryLocation):
        dictionaryFile = open(dictionaryLocation, 'r')
        dictionary = set(map(lambda word: word.rstrip(), dictionaryFile.readlines()))
        self.sortedDictionary = Trie()
        # self.sortedDictionary = {}

        for word in dictionary:
            self.sortedDictionary.insert(word)
            
    def isWord(self, word):
        return self.sortedDictionary.search(word)

    def isStartOfExistingWord(self, string):
        if string == "":
            return False
        return self.sortedDictionary.startsWith(string)
