# Maximizing Number of Tasks

def maximizeTasks(A, T):
    currentTime, numberOfTasks = 0, 0
    A.sort()
    for i in range (len(A)):
        currentTime += A[i]
        if currentTime >= T:
            break
        numberOfTasks += 1
    return numberOfTasks

# Test case #1: output = 3 (1, 2, 2)
print (maximizeTasks([4,2,1,2,5],8))

# Test case #2: output = 6 (1, 2, 3, 4, 5, 7)
print (maximizeTasks([3,1,7,4,9,2,5], 23))