#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
import re


class TrieError(Exception):
    pass
    
class Trie:
    """
    A Trie class for doing dictionary lookup of strings.
    """
    @staticmethod
    def trim_whitespace(st):
        st = re.sub(r'^\s+', '', st)
        st = re.sub(r'\s+$', '', st)
        return st
    @staticmethod    
    def squinch_whitespace(st):
        st = re.sub(r'\s+', ' ', st)
        return st
        
    #The Trie class defines an inner class TrieNode for the Trie's nodes.
    class TrieNode:
        def __init__(self, is_word, node_map):
            self.is_word=is_word
            self.node_map=node_map    
      
    def __init__(self):
            self.root=Trie.TrieNode(False, {' ':Trie.TrieNode(False, {})})
            logging.debug("trie created, has one empty node.")
            logging.debug("root points to a "+str(self.root))
            self.num_nodes = 1
            
            
    #Get the number of TrieNodes in the Trie        
    def _num_nodes(self):
        return self.num_nodes
    
    #Explore the nodes in a depth-first order.  Visit the parent of each node before its children. Concatenate a new digit to an existing prefix at each visit, completing a prefix when the node has value is_word=true.   When the prefix is complete, print it.  Prefixes will print in lexicographic order e.g. Udo, Univ, University, Uno.
    #In breadthfirst_visit, I use a queue instead of a stack to sort first by ascending string length, then in lexicographic order,
    #e.g. Udo, Uno, Univ, University.
    def _depthfirst_visit(self, current=None):
        logging.info("traverse Trie in depth-first pre-order (visiting parent node before children), and write all words to the log.") 
        print "traverse Trie depth-first, and only print the longest words to the console."
        prefix=""
        if current is None:
            current = self.root
        
        myStack=[]
        stackPointer=-1
        longestWordSeen=False
        wordPrinted={}
        myStack.append({'prefix':prefix,'currentNode':current, 'visited':{}})
        stackPointer += 1
        
        while len(myStack)!=0:
            logging.debug("=" * 25)
            if (len(myStack[stackPointer]['currentNode'].node_map)==0):
                #shouldn't have to check if myStack[stackPointer]['currentNode'].node_map is None, see how it's initialized!  
                logging.debug("stackPointer: %d",stackPointer)
                logging.debug("current node "+str(myStack[stackPointer]['currentNode'])+" has no map")
                myStack.pop(stackPointer)
                stackPointer -= 1                
            elif len(myStack[stackPointer]['currentNode'].node_map)>0:
                currPointer = stackPointer 
                logging.debug("stackPointer: %d",stackPointer)
                if (len(myStack[stackPointer]['currentNode'].node_map)==len(myStack[stackPointer]['visited'])):
                    logging.debug('all nodes mapped from current node %s were visited', str(myStack[stackPointer]['currentNode']))
                    if myStack[stackPointer]['currentNode'].is_word==True and longestWordSeen==False:
                        longestPrefix = myStack[stackPointer]['prefix']
                        print "["+longestPrefix.encode('utf-8')+"] @ "+str(myStack[stackPointer]['currentNode'])
                        longestWordSeen=True                            
                    myStack.pop(stackPointer)
                    stackPointer -= 1
                    continue
                else: #we haven't visited all nodes mapped from the current node, so a longestWord is still undiscovered
                    longestWordSeen=False                
                for digit in sorted(list(myStack[currPointer]['currentNode'].node_map.iterkeys()),cmp=lambda x,y:cmp(x.lower(),y.lower()),reverse=True):
                    logging.debug('char: [%s]',digit)
                    logging.debug('current node %s maps via [%s] to %s', str(myStack[currPointer]['currentNode']), digit,str(myStack[currPointer]['currentNode'].node_map[digit]))
                    if digit not in myStack[currPointer]['visited']:
                        myStack[currPointer]['visited'][digit]=True
                        #Push to the stack the record of the visited node...
                        prefix=myStack[currPointer]['prefix']
                        logging.debug("prefix: ["+prefix+"]")
                        if myStack[currPointer]['currentNode'].is_word==True and prefix not in wordPrinted:
                            logging.info("["+prefix+"]")
                            wordPrinted[prefix]=True
                        myStack.append({'prefix':prefix+digit,'currentNode':myStack[currPointer]['currentNode'].node_map[digit], 'visited':{}})
                        stackPointer += 1    
        return len(wordPrinted)    

                        
    def _breadthfirst_visit(self):
        logging.info("traverse Trie breadth-first, printing all words to the log.") 
        current=self.root
        prefix=""
        
        myQueue=[]
        queuePointer=-1
        #longestWordPrinted={}
        wordPrinted={}
        myQueue.append({'prefix':prefix,'currentNode':current, 'visited':{}})
        queuePointer += 1
        
        while len(myQueue)!=0:
            logging.debug("=" * 25)            
            if (len(myQueue[0]['currentNode'].node_map)==0):
                #shouldn't have to check if myStack[queuePointer]['currentNode'].node_map is None, see how it's initialized!  
                logging.debug("queuePointer: %d",queuePointer)
                logging.debug("current node "+str(myQueue[0]['currentNode'])+" has no map")
                myQueue.pop(0)
                queuePointer -= 1                
            elif len(myQueue[0]['currentNode'].node_map)>0:
                currPointer = 0 
                logging.debug("queuePointer: %d",queuePointer)
                if (len(myQueue[0]['currentNode'].node_map)==len(myQueue[0]['visited'])):
                    logging.debug('all nodes mapped from current node %s were visited', str(myQueue[0]['currentNode']))
                    #if myQueue[0]['currentNode'].is_word==True and prefix not in longestWordPrinted:
                    #    longestWordPrinted[prefix]=True
                    #    print "["+prefix+"]" 
                    myQueue.pop(0)
                    queuePointer -= 1
                    continue
                for digit in sorted(list(myQueue[currPointer]['currentNode'].node_map.iterkeys()),cmp=lambda x,y:cmp(x.lower(),y.lower()),reverse=False):
                    logging.debug('char: [%s]',digit)
                    logging.debug('current node %s maps via [%s] to %s', str(myQueue[currPointer]['currentNode']), digit,str(myQueue[currPointer]['currentNode'].node_map[digit]))
                    if digit not in myQueue[currPointer]['visited']:
                        myQueue[currPointer]['visited'][digit]=True
                        #append to the queue the record of the visited node...
                        prefix=myQueue[currPointer]['prefix']
                        logging.debug("prefix: ["+prefix+"]")
                        if myQueue[currPointer]['currentNode'].is_word==True and prefix not in wordPrinted:
                            logging.info("["+prefix+"]")
                            wordPrinted[prefix]=True
                        myQueue.append({'prefix':prefix+digit,'currentNode':myQueue[currPointer]['currentNode'].node_map[digit], 'visited':{}})
                        queuePointer += 1 

    def _search(self, s):
        current=self.root
        u = unicode(s, "utf-8")
        for c in u:
            if current.node_map is None or c not in current.node_map:
                logging.error("string "+u+" not found in trie")
                return None
            current=current.node_map[c]
        if current.is_word is False:
            logging.error("string "+u+" was found in trie, but is not a word")
            return None
        else:
            logging.debug("OK.  string "+u+" was a word found in trie")
            return current
    
        
    def _search_returnpath(self, s):
        current=self.root
        pathNodes = []
        u = unicode(s, "utf-8")
        for c in u:
            if current.node_map is None or c not in current.node_map:
                logging.error("string "+u+" not found in trie")
                return None
            current=current.node_map[c]
            pathNodes.append({'currentNode':current, 'currentChar':c})
        if current.is_word is False:
            logging.debug("string "+u+" was found in trie, but is not a word")
            return None
        else:
            logging.debug("OK.  string "+u+" was a word found in trie")
            return pathNodes
        
        
                        
    def _delete(self, s):
        current=self.root
        for c in unicode(s,"utf-8"):
            if current.node_map is None or c not in current.node_map:
                logging.warn("string "+s+" not in tree, cannot delete")
                return False
            current=current.node_map[c]    
        if current.is_word is False:
            logging.warn("string "+s+" is in tree, but not a word")
            return False
        else:
            current.is_word = False
            logging.debug("removing word at node "+str(current))
            return True    

            
            
    def _clean_delete(self, s):
        
        foundList = self._search_returnpath(s)
        
        if foundList is None:
            return False

        toDelete=None    
        #the last node returned in foundList would be the word, so set is_word to
        #False to delete it
        foundList[len(foundList)-1]['currentNode'].is_word=False
        logging.debug("deleted word at "+str(foundList[len(foundList)-1]['currentNode']))        
            
        for found in reversed(foundList):
            if self._depthfirst_visit(found['currentNode'])<1:
                if toDelete is not None and toDelete['currentChar'] in found['currentNode'].node_map:
                    logging.debug("clean_delete for node:"+str(toDelete['currentNode']))
                    del found['currentNode'].node_map[toDelete['currentChar']]
                toDelete=found
        
    #No need to use recursion
    #think about returning None if s wasn't already a word or returning TrieNode reference if s was already a node
    def _insert(self, s):
        current=self.root
        for c in unicode(s, "utf-8"):
            logging.debug("scanning input: char ["+c+"]...")
            if current.node_map is None:
                logging.debug("current node "+str(current)+" has no map")
                current = Trie.TrieNode(False, {' ':Trie.TrieNode(False, {})})
            if c not in current.node_map:
                logging.debug("--> "+c+" not found, adding new node...")
                current.node_map[c]=Trie.TrieNode(False, {' ':Trie.TrieNode(False, {})})
                logging.debug(str(current) + " has "+str(len(current.node_map))+" children")
                self.num_nodes += 1
            logging.debug("current pointed to "+str(current)+"...")
            current=current.node_map[c]
            logging.debug("now, current points to "+str(current)+"!")
        if current.is_word is False:
            logging.debug("added a string!")
            current.is_word=True
            return False
        else:
            return True
            
"""
depthfirst_visit prints to console only the longest words that are not prefixes of other words in the trie.  On the other hand, depthfirst_visit writes to the log all words in pre-order.  Can longest words be printed from a breadth-first visit?  Another name question: are strings with whitespace in them words?  Should I call is_word() "is_word()", or something else? 
"""

def main():

    print "Trie.py builds a trie from a set of strings.  See TrieTest.py for test code."
       
if __name__=='__main__':
    main()