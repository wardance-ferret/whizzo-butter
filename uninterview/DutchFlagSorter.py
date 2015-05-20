from random import randint

class DutchFlagSorterError(Exception):
    pass

class DutchFlagSorter:
    #initialize "class variables" here (in the class body)
   
    def __init__(self, array, pivot_index):
    #initialize "instance variables" here
    #each instance of DutchFlagSorter class has its own copy of an IV
        self.array=array
        self.size=len(self.array)
        self.pivot_index=int(pivot_index)
        self.comparisons=0
        self._sort()
        

    def _random_init(self,array_size,array_smallest_int,array_biggest_int, pivot_index):
        if ((array_size<1) or pivot_index not in range(array_size)):
            raise DutchFlagSorterError ("either the array has dimension less than 1 or the pivot index is out of bounds")
        if not (array_smallest_int <= array_biggest_int):
            raise DutchFlagSorterError ("minimum value should be less than the max value")
        self.array = self._seed_yourself(array_size,array_smallest_int, array_biggest_int)
        self.size=len(self.array)
        self.pivot_index=int(pivot_index)
        self.comparisons=0
        self._sort()    
            

    def _left_shift(self,begin, end):
        i=begin
        while (i <= end):
            self.array[i]=self.array[i+1]
            i +=1

    def _right_shift(self, begin, end):
        i=end
        while (i >= begin):
            self.array[i]=self.array[i-1]
            i -= 1

    def _seed_yourself(self, array_size, array_smallest_int, array_biggest_int):
        seed_input=[]
        for i in range(array_size):
            seed_input.append(randint(array_smallest_int, array_biggest_int))
        return seed_input    
            

    def _test(self,expected_array):
        if (len(expected_array) != self.size):
            return 0
        for  i in range(self.size):
            if expected_array[i] != self.array[i]:
                return 0
        return 1
        
    def _sort(self):
        #The sort should be in-place, with a single slot "temp" for doing swaps.
        i = self.pivot_index
        j = 0
        pivot = self.pivot_index
        #this index follows the pivot element as it gets shifted
        print "-"*65
        print "sorting ",
        self._print()
        print " like a Dutch Flag with the index="+str(pivot)+" as the pivot"

        while (j < pivot):

            if ((self.array[j] > self.array[pivot])
                or ((self.array[j]==self.array[pivot]) and (abs(pivot-j)> 1) )):
                self.comparisons += 1
                print "j="+str(j)+": a["+str(j)+"]="+str(self.array[j]),
                print "greater than pivot="+str(pivot)+": a["+str(pivot)+"]="+str(self.array[pivot])
                temp=self.array[j]
                if ((self.array[j]==self.array[pivot]) and (abs(pivot-j)> 1) ):
                    print "found a duplicate pivot value: "+str(self.array[pivot])
                    temp_i=i
                    i=pivot
                    self._left_shift(j, i-1)
                    self.array[i]=temp
                    i=temp_i
                else:
                    self._left_shift(j, i-1)
                    self.array[i]=temp
                pivot = pivot-1
                print "setting i="+str(i)+": a["+str(i)+"]="+str(self.array[i])
                self._print()
            else:    
                j += 1
                self.comparisons += 1
        j = len(self.array)-1
        i = pivot
        
        
        while (j > pivot):

            if ((self.array[j] < self.array[pivot])
               or ((self.array[j]==self.array[pivot])and
                        (abs(pivot-j)> 1)
                    )
                ):
                self.comparisons += 1
                print "j="+str(j)+": a["+str(j)+"]="+str(self.array[j]),
                print "less than pivot="+str(pivot)+": a["+str(pivot)+"]="+str(self.array[pivot])
                temp=self.array[j]
                if((self.array[j]==self.array[pivot])and
                        (abs(pivot-j)> 1)):
                    print "found a duplicate pivot value: "+str(self.array[pivot])
                    temp_i = i
                    i=pivot
                    self._right_shift( i+1,j)
                    self.array[i]=temp
                    print "setting i="+str(i)+": a["+str(i)+"]="+str(self.array[i])
                    i=temp_i
                else:
                    self._right_shift( i+1,j)
                    self.array[i]=temp
                    print "setting i="+str(i)+": a["+str(i)+"]="+str(self.array[i])
                self._print()
                pivot = pivot+1
            else:    
                j -= 1
                self.comparisons += 1
                

    def _print(self):
        print self.array
        
"""main() is just some test code for DutchFlagSorter.
    The sort takes an array of integers and the index of an array element which will be used
    as a "pivot."  That is, the sort will shift elements in array[0],...array[pivot-1] to the right
    of array[pivot] if they are greater than array[pivot], and shift elements in array[pivot+1]...array[len(array)-1]
    less than array[pivot] to the left of that element.  If an element is equal to array[pivot], it will be directly
    adjacent to that element. 
    
    The code compares the expected result of the sort with the actual result.
    The sort should be "stable" i.e. the integers will not change position relative
    to each other, only with respect to the pivot.    
"""
def main():

    #balanced case 1: some stuff on the left needs to go to the right of the pivot, and vice-versa. 
    my_sorted = DutchFlagSorter([4,0,2,1,2,0], 3)
    my_sorted._print()
    expected = [0,0,1,4,2,2]
    if not my_sorted._test(expected):
        print "test [0] error: array not sorted as ",
        print expected

    #balanced case 2: some stuff on the left needs to go to the right of the pivot, and vice-versa.
    #the pivot's value is duplicated (here, two 1's)
    my_sorted = DutchFlagSorter([4,1,2,1,2,0], 3)
    my_sorted._print()
    expected = [0,1,1,4,2,2]
    if not my_sorted._test(expected):
        print "test[1] error: array not sorted as ",
        print expected

    #easy case: stuff on the left just needs to be thrown to the right, but nothing on the right of the pivot needs to come left
    my_sorted = DutchFlagSorter([4,0,2,1,2,3], 3)
    my_sorted._print()
    expected = [0,1,4,2,2,3]
    my_sorted._test(expected)
    if not my_sorted._test(expected):
        print "test [2] error: array not sorted as ",
        print expected

    my_sorted = DutchFlagSorter([4,1,2,1,5,3], 3)
    my_sorted._print()
    expected = [1,1,4,2,5,3]
    my_sorted._test(expected)
    if not my_sorted._test(expected):
        print "test [3] error: array not sorted as ",
        print expected



    #really bad case:  everything on the left needs to go to the right, and vice-versa
    my_sorted = DutchFlagSorter([9,6,7,5,1,4,3,2],3)
    my_sorted._print()
    expected = [1,4,3,2,5,9,6,7]
    my_sorted._test(expected)
    if not my_sorted._test(expected):
        print "test[4] error: array not sorted as ",
        print expected

    #binary case!
    my_sorted = DutchFlagSorter([0,1,1,0,1,0,1,0],3)
    my_sorted._print()
    expected = [0,0,0,0,1,1,1,1]
    my_sorted._test(expected)
    if not my_sorted._test(expected):
        print "test[5] error: array not sorted as ",
        print expected

    #neg integers!
    my_sorted = DutchFlagSorter([4,-1,2,1,-5,3],3)
    my_sorted._print()
    expected = [-1,-5,1,4,2,3]
    my_sorted._test(expected)
    if not my_sorted._test(expected):
        print "test[5] error: array not sorted as ",
        print expected

    #only one integer value
    my_sorted = DutchFlagSorter([-1,-1,-1,-1,-1,-1],3)
    my_sorted._print()
    print "my sort took "+str(my_sorted.comparisons)+" comparisons..."
    expected = [-1,-1,-1,-1,-1,-1]
    my_sorted._test(expected)
    if not my_sorted._test(expected):
        print "test[6] error: array not sorted as ",
        print expected


    #random array init!
    my_sorted = DutchFlagSorter([],0)    
    my_sorted._random_init(70, -15 , 500, 15)
    my_sorted._print()
    print "my sort took "+str(my_sorted.comparisons)+" comparisons..."
    
if __name__ == '__main__':
    main()
