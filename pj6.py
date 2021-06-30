"""
Project (Week 6)

1) (10pts) Study the textbook Code Fragment 12.5 and implement the Quick-Sort for a Python list. Hint: Use Python list for S, L, E, and G. Use list built-in methods to achieve the enqueuer and dequeuer operations. Test your code and show your results before and after the sorting by using a Python list of simple integers.

2) (5pts) Study the textbook Code Fragment 12.6 and (modify if necessary) to implement another in-place Quick-Sort for a Python list. Test your code and show your results before and after the sorting by using a Python list of simple integers. 

3) (5pts) Experimentally compare the performance of above in-place and not in-place Quick-Sort code with a list of random float data. You can select the size of the Python list between 100-10000 so each run will take just several seconds.


Submit your code together with the run results.


"""
"""
The program will prompt a user to enter the following options:
1. the number of floating numbers to be sort; default is 10.
2. verbose mode: 0 is to turn off verbose mode; 
	otherwise, the randomly generated data and sorted result will be displayed
3. type of quick sort to run: 1 is for not in place quick sort; 2 is for in place quick sort;
        oterwise, both types will be executed.
        if a user to choose to run type 1 or type 2, a list of simple integers will be generated. 
	Otherwise, a list of random float data will be generated.
"""
import random
from time import time
from linked_queue import LinkedQueue
from quick_queue import quick_sort
from quick_inplace import inplace_quick_sort

def test(number, verbose, test):
    #floating number
    if test == 1 or test == 2:
        ilist = [ random.randint(2,30)  for i in range(0,number)]
    else: 
        ilist = [ round(random.uniform(1,number+1),2)  for i in range(0,number)]

    #print input numbers
    if verbose != 0:
        print("\nGenerated ", number, " data = ", ilist)

    C = LinkedQueue()
    for item in ilist:
        C.enqueue(item)

    if test != 2:
        if verbose != 0:
            print("\nSorted by not inplace quick sort: ")

        start = time() 
        quick_sort(C)
        end = time()

        # print sorted numbers
        if verbose != 0:
            outlist=[]
            for i in range(0,number):
                item = C.dequeue()
                outlist.append(item)
                #print(item)
            print(outlist)
        quicksort_time = end - start
        print("not inplace quick sort: time taken= ", quicksort_time)

    if test != 1:
        if verbose != 0:
            print("\nSorted by inplace_quick_sort")

        start = time()
        inplace_quick_sort(ilist,0,number-1)
        end = time()

        if verbose != 0:
            print(ilist)
        inplace_time = end - start
        print("inplace quick sort: time taken= ", inplace_time)

def main():
    print("Quick sort") 

    while True:
        number = input("\nEnter the number of random generated float data to be sorted(default: 1000)(q or Q: stop the program ")
        if number is 'q' or number is 'Q':
            break
        elif number is '':
            number = 1000
        else:
            number = int(number)
            if number < 1:
               print("Use the default number: 1000")
               number = 10
        verbose = 1
        vb = input("Verbose mode (0=off, otherwise= on) :")
        if vb == '0':
            verbose = 0
        print("type of quick sorts:\n\t1= for not-in-place quick sort; \n\t2= for in-place quick sort; \n\tothers= for run both types of quick sort): ")
        type = input("Enter test type: ") 
        if type is '':
            print("Run both types of quick sort")
            type = 3
        else:
            type = int(type)
        test(number, verbose, type)

if __name__ == '__main__':
    main()

