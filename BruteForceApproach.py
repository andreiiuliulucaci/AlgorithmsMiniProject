
import timeit
import tracemalloc

#print(bigArray)

def BruteForce(array,N):
    maxInt = 0
    for i in range(N):
        currInt = 0
        for j in range(N):
            currInt += array[j]
            if currInt > maxInt:
                maxInt = currInt
    print(maxInt)




#tracemalloc.start()


def AlgorithmRunningTimeBFA():
    mySetup = '''
import numpy as np
bigArray = np.random.randint(-200, 200, size=10000)
N = len(bigArray)
'''
    myCode = '''
def BruteForce(array):
    maxInt = 0
    for i in range(N):
        currInt = 0
        for j in range(N):
            currInt += array[j]
            if currInt > maxInt:
                maxInt = currInt
    print(maxInt)

BruteForce(bigArray)
'''
    print("Time taken for Brute force is: " + str(timeit.timeit(setup = mySetup,stmt = myCode,number = 10)) + "seconds")

#current, peak = tracemalloc.get_traced_memory()
#print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
#tracemalloc.stop()