#!/usr/bin/python
# -*- coding: utf-8 -*-
import codecs
import string
import logging
import Trie

class TrieTestError(Exception):
    pass

class TrieTest:
  

    @staticmethod
    def initTrie():
        failed=False
        my_trie=Trie.Trie()
        if my_trie._num_nodes() != 1:
            logging.error("should have a single root node in the tree")
            failed=True
        if failed==False:
            logging.info("OK initTrie()")

            
    @staticmethod
    def handleWhitespace():
        #Test the functions for trimming whitespace (they aren't currently used though)
        failed = False
        if Trie.Trie.trim_whitespace(" New Mexico") != "New Mexico":
            logging.error("handleWhitespace(): expected \"New Mexico\" but saw "+Trie.Trie.trim_whitespace(" New Mexico"))
            failed = True
        if Trie.Trie.squinch_whitespace("Univ  of New    Mexico ") != "Univ of New Mexico ":
            logging.error("handleWhitespace(): expected \"Univ of New Mexico\" but saw "+Trie.Trie.squinch_whitespace("Univ  of New    Mexico "))
            failed = True
        if failed==False:    
            logging.info("OK handleWhitespace()")    


        
    @staticmethod
    def loadFromFile(filepath):
        failed=False
        maxWords=1000 
        #Assume that each line is a distinct word to load into my_trie
        logging.info("loading first "+str(maxWords)+" words from "+str(filepath))
        my_trie=Trie.Trie()
        try:
            inputfile = codecs.open(filepath, 'rb')
            count=0
            for line in inputfile:
                lowered=string.lower(line)
                trimmed=Trie.Trie.trim_whitespace(lowered)
                squinched=Trie.Trie.squinch_whitespace(trimmed)
                logging.debug(squinched)
                my_trie._insert(squinched)
                if count==maxWords:
                    break                
                count += 1

            numWords=my_trie._depthfirst_visit()

            if numWords != maxWords:
                logging.error("loadFromFile() expected "+str(maxWords)+" words but found "+str(numWords))
                failed=True
            
        except IOError:
            raise TrieTestError("couldn't open file "+filepath)
       
        if failed==False:    
            logging.info("OK loadFromFile()")


        
    @staticmethod
    def insertWord():
        failed=False
        my_trie=Trie.Trie()
        my_dictionary = ["universal", "Zerä", "Uno", "Univ", "University", "University of", "University of New Mexico", "Universe", "Udo", "universals", "Univariate", "Univ. of N. Mex", "Universal"]
    
        for word in my_dictionary:
            print '-' * 75
            print "trying to add word: "+word
            my_trie._insert(word) 
        
      
        if my_trie._insert("地元密着型の都心型ショッピングセンタ") is not False:
            logging.error("地元密着型の都心型ショッピングセンタ not already in trie")
            failed=True
            
        if my_trie._insert("サンモール") is not False:
            logging.error("サンモール not already in trie")
            failed=True
        if my_trie._insert("University of New Mexico") is not True:
            logging.error("'University of New Mexico' was added to trie")   
            failed=True
        if failed==False:
            logging.info("OK insertWord()")

            
    @staticmethod
    def deleteWord():
        failed=False
        my_trie=Trie.Trie()
        my_dictionary = ["universal", "Zerä", "Uno", "Univ", "University", "University of", "University of New Mexico", "Universe", "Udo", "universals", "Univariate", "Univ. of N. Mex", "Universal"]
        my_prefix_input="University of New Mexico"    
        for word in my_dictionary:
            print '-' * 75
            print "trying to add word: "+word
            my_trie._insert(word)     
        if my_trie._delete("wine") is not False:
           logging.error("'wine' was not in trie, couldn't be deleted")
           failed=True
        if my_trie._delete(my_prefix_input) is not True:
           logging.error("error: %s was in trie when we deleted it" % my_prefix_input)
           failed=True
        if my_trie._delete("University") is not True:
           logging.error("'University' could not be deleted")
           failed=True
        if my_trie._delete("University of") is not True:
           logging.error("'University of' could not be deleted")
           failed=True           
        if my_trie._delete("Univ") is not True:
           logging.error("'Univ' could not be deleted")
           failed=True
        if failed==False:
           logging.info("OK deleteWord()")
           
    @staticmethod
    def cleanDeleteWord():
        failed=False
        my_trie=Trie.Trie()
        my_dictionary = ["universal", "Zerä", "Uno", "Univ", "University", "University of", "University of New Mexico", "Universe", "Udo", "universals", "Univariate", "Univ. of N. Mex", "Universal"]
     
        for word in my_dictionary:
            print '-' * 75
            print "trying to add word: "+word
            my_trie._insert(word)     

    #TODO: modify so it checks for the current number of nodes
    
        numWordsBefore=my_trie._depthfirst_visit()
        numNodesBefore=my_trie._num_nodes()    
        my_trie._clean_delete("University of New Mexico")
        numWordsAfter=my_trie._depthfirst_visit()
        numNodesAfter=my_trie._num_nodes()
        
        if (numWordsBefore - numWordsAfter) != 1:
            logging.error("failed to delete word")
            failed=True
        if (numWordsAfter>=numWordsBefore):
            logging.error("failed to clean up nodes")
            failed=True
        if failed==False:
            logging.info("OK cleanDeleteWord()")   
    

def main():
    #To set up custom logging to accept any encoding, read something like http://web.archive.org/web/20100107060919/http://tony.czechit.net/2009/02/unicode-support-for-pythons-logging-library/
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',filename='../../logs/TrieTest.log', filemode='w', level=logging.INFO)
    print 'Writing log to ../../logs/TrieTest.log'
    #TrieLoggingFormatter.configureTrieLogging(logging.DEBUG, logging.DEBUG, '../../../logs/TrieLoggingTest.txt')
    TrieTest.initTrie()
    TrieTest.handleWhitespace()
    TrieTest.loadFromFile('../../../share/dicts/german.dic')
    TrieTest.insertWord()
    TrieTest.deleteWord()
    TrieTest.cleanDeleteWord()


if __name__ == '__main__':
    main()
