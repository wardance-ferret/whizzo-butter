
# A subclass of Exception.
# "pass" is a stub method that does nothing
# but saves us from an empty class body.
class WordReverserError(Exception):
    pass

"""
WordReverser.py takes a string input and reverses the words (white-space delimited strings).
"""
class WordReverser():

	#what does this annotation do in Python?
    @staticmethod
    def as_words(s):
        return s.split()

    #instance members (fields , methods)
    def __init__(self, string):
        self.array=WordReverser.as_words(string)
        self.size=len(self.array)
        self._reverse()
    
    def _reverse(self):
        i=0
        j=self.size-1
        while (i < j ):
            if self.array[i] != self.array[j]:
                temp=self.array[j]
                self.array[j]=self.array[i]
                self.array[i]=temp
            i+=1
            j-=1
            
        print ("input reversed as: " + " ".join(self.array))
                
    def _test(self,expected_string):
        expected_array = WordReverser.as_words(expected_string)
        if (len(expected_array) != self.size):
            return 0
        for  i in range(self.size):
            if expected_array[i] != self.array[i]:
                return 0
        return 1
        
        

"""main() is test code for WordReverser.py."""        
def main():
    print ("WordReverser.py takes a string input and reverses the words (white-space delimited strings).")
    
    my_reversed = WordReverser("Angel loves Eric madly")
    expected = "madly Eric loves Angel"
    
    if not my_reversed._test(expected):
        print ("test[0]: words in string not reversed as "),
        print (expected)
    

if __name__ == '__main__':
    main()
