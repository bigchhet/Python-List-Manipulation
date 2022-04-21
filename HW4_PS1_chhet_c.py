#Chhai Chhet
#1239352
#Homework 4 Program Set 1
#This program showcases the ability to manipulate the properties within a list

def swapFirstLast(data:list)->list:
    '''Swap the first and last element in a list.'''
    #set first variable to the value of the first item in list  
    first = data[0]
    
    #set last variable to the value of the last item in list  
    last = data[-1]

    #swap the values
    data[0] = last
    data[-1] = first

    #return the list with updated values
    return data

 
def shiftRight(data:list)->list:   
    '''Shift the elements of list to the right.'''
    #saving the size of the list
    size = len(data)

    #saving the value of the last index of list
    last = data[size- 1]

    #shifting the position of each element in list by 1
    data[1:] = data[0:size - 1]

    #saving the last index of previous list into first position
    data[0] = last

    #return the list with updated values
    return data
        

def replaceEven(data:list)->list:
    '''Replace all even index in list with 0'''
    #save the length of list into variable
    size = len(data)

    #logic for checking each element in list
    for index in range(size):

        #checks if element in list is an even number
        if data[index] % 2 == 0:

            #set even number to 0
            data[index] = 0

    #return the list with updated values
    return data


def replaceNeighbors(data:list)->list:
    '''Switches each index of list except first and last index with its neighbor'''
    #save size of the list into variable
    size = len(data)

    #check each element in list except first and last element
    for index in range(1, size -1):

        #if previous element is greater than next element change current index to previous elemet
        if  data[index - 1] > data[index + 1]:
            data[index] = data[index - 1]

        #change current element to next element
        else:
            data[index] = data[index + 1]

    #return the list with updated values
    return data


def removeMiddle(data:list)->list:
    '''Removes middle value(s) of the list'''
    #save the size of the data into a local variable
    size = len(data)

    #save half the size of list
    half = int(size/2)

    #save the middle value of the list into local variable
    middle = data[half]

    #logic for determining if more than 1 value should be removed
    if size % 2 == 0:
        right = data[half - 1]
        left = data[half]
        data.remove(left)
        data.remove(right)

    #if not 2 values remove, just remove the initial middle value from the list
    else:
        data.remove(middle)

    #return the list with updated values
    return data
    

def evenToFront(data:list)->list:
    '''Shift all even digits to the front of the list'''
    #initialize a local variable spot to zero
    spot = 0

    #save the value of size of list into local variable
    size = len(data)

    #logic for traversing list and updating values
    for index in range(size):

        #save current value for each iteration for later comparison
        current = data[index]

        #logic for determining if a number in the list is even
        if (current % 2 == 0):

            #logic for removing the even number and inserting it front
            data.remove(current)
            data.insert(spot, current)
            spot = spot + 1

    #return the list with updated values        
    return data


def secondLargest(data:list)->int:
    '''Determines the second largest value in a list'''
    #store the size of the list into local variable
    size = len(data)

    #set first to 0
    first = 0

    #logic for finding the largest number in list
    for index in range(size):

        #set current variable to the current value being at looked within the list
        current = data[index]

        #update the first variable to the current value if current is greater than first
        if(current > first):
            first = current

    #set second to 0 and update it iteratively if the current index is larger than second but less than first
    second = 0

    #logic for finding the second largest number in list
    for index in range(size):

        #set current variable to the current value being at looked within the list
        current = data[index]

        #update the second variable to the current value if current is greater than second while second is still less than first
        if(current > second and current < first):
            second = current

    #return the wanted integer
    return second


def isIncreasing(data:list)->bool:
    '''Determines whether a list is in increasing order'''
    #intialize a local bool variable to true
    check = True

    #save the size of the array to check all necessary values
    size = len(data) - 1

    #logic for determining if a list is in creasing order
    for index in range(size):

        #save the current index of the list into current variable
        current = data[index]

        #save the next index of the list into next variable
        next = data[index + 1]

        #if current is greater than next, set the check variable to false
        if(current > next):
            check = False

    #return the wanted boolean value
    return check


def hasAdjacentDuplicate(data:list)->bool:
    '''Determines if a list has any duplicate adjacent numbers'''
    #intialize a local boolean variabled named check to false
    check = False

    #save the size of the array to check all necessary values
    size = len(data) - 1

    #logic for determining if a list has any adjacent duplicates values
    for index in range(size):

        #save the current index of list into current variable
        current = data[index]

        #save the next index of current of list into next next variable 
        next = data[index + 1]

        #if current equals next, set check boolean to true
        if(current == next):
            check = True

    #return the wanted boolean value
    return check


def hasDuplicate(data:list)->bool:
    '''Determines if a list has any duplicate numbers'''
    #intialize a local boolean variabled named check to false
    check = False

    #save the size of the array to check all necessary values
    size = len(data)

    #logic for determining if a list has any duplicate values
    #get value for first local variable
    for index in range(size - 1):

        #save first index of list for comparison into local variable
        current1 = data[index]

        #get value for second local variable
        for index2 in range(index + 1, size):

            #save second index of list for comparison into local variable
            current2 = data[index2]

            #check if variable 1 == variable 2, if true update check variable to true
            if (current1 == current2):
                check = True
                
    #return the wanted boolean value    
    return check


ONE_TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#ONE_TEN =  [12, 20, 10, 14, 54, 16, 75, 38, 79, 103]
#ONE_TEN = [1, 25, 25, 4, 5, 4, 7, 60, 9, 10]


def main() :
    print("The original data for all functions is: ", ONE_TEN) 
 
    #a. Demonstrate swapping the first and last element. 
    data = list(ONE_TEN) 
    swapFirstLast(data)         #call this function       
    print("After swapping first and last: ", data) 
 
    #b. Demonstrate shifting to the right. 
    data = list(ONE_TEN) 
    shiftRight(data)            #call this function 
    print("After shifting right: ", data) 
 
    #c. Demonstrate replacing even elements with zero. 
    data = list(ONE_TEN) 
    replaceEven(data)           #call this function 
    print("After replacing even elements: ", data) 
 
    #d. Demonstrate replacing values with the larger of their neighbors. 
    data = list(ONE_TEN) 
    replaceNeighbors(data)      #call this function 
    print("After replacing with neighbors: ", data) 
 
    #e. Demonstrate removing the middle element. 
    data = list(ONE_TEN) 
    removeMiddle(data)          #call this function 
    print("After removing the middle element(s): ", data) 
 
    #f. Demonstrate moving even elements to the front of the list. 
    data = list(ONE_TEN) 
    evenToFront(data)           #call this function 
    print("After moving even elements: ", data) 
 
    #g. Demonstrate finding the second largest value. 
    print("The second largest value is: ", secondLargest(ONE_TEN)) 
 
    #h. Demonstrate testing if the list is in increasing order. 
    print("The list is in increasing order: ", isIncreasing(ONE_TEN)) 
 
    #i. Demonstrate testing if the list contains adjacent duplicates. 
    print("The list has adjacent duplicates: ", hasAdjacentDuplicate(ONE_TEN)) 
 
    #j. Demonstrate testing if the list contains duplicates. 
    print("The list has duplicates: ", hasDuplicate(ONE_TEN))
    

#tells program what to call first
if __name__ == "__main__":
    main()


#-----------------------------------------OUTPUT---------------------------------------------------

#TEST 1
# The original data for all functions is:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# After swapping first and last:  [10, 2, 3, 4, 5, 6, 7, 8, 9, 1]
# After shifting right:  [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# After replacing even elements:  [1, 0, 3, 0, 5, 0, 7, 0, 9, 0]
# After replacing with neighbors:  [1, 3, 4, 5, 6, 7, 8, 9, 10, 10]
# After removing the middle element(s):  [1, 2, 3, 4, 7, 8, 9, 10]
# After moving even elements:  [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]
# The second largest value is:  9
# The list is in increasing order:  True
# The list has adjacent duplicates:  False
# The list has duplicates:  False


#TEST 2
# The original data for all functions is:  [12, 20, 10, 14, 54, 16, 75, 38, 79, 103]
# After swapping first and last:  [103, 20, 10, 14, 54, 16, 75, 38, 79, 12]
# After shifting right:  [103, 12, 20, 10, 14, 54, 16, 75, 38, 79]
# After replacing even elements:  [0, 0, 0, 0, 0, 0, 75, 0, 79, 103]
# After replacing with neighbors:  [12, 12, 14, 54, 54, 75, 75, 79, 103, 103]
# After removing the middle element(s):  [12, 20, 10, 14, 75, 38, 79, 103]
# After moving even elements:  [12, 20, 10, 14, 54, 16, 38, 75, 79, 103]
# The second largest value is:  79
# The list is in increasing order:  False
# The list has adjacent duplicates:  False
# The list has duplicates:  False


#TEST 3
# The original data for all functions is:  [1, 25, 25, 4, 5, 4, 7, 60, 9, 10]
# After swapping first and last:  [10, 25, 25, 4, 5, 4, 7, 60, 9, 1]
# After shifting right:  [10, 1, 25, 25, 4, 5, 4, 7, 60, 9]
# After replacing even elements:  [1, 25, 25, 0, 5, 0, 7, 0, 9, 0]
# After replacing with neighbors:  [1, 25, 25, 25, 25, 25, 60, 60, 60, 10]
# After removing the middle element(s):  [1, 25, 25, 4, 7, 60, 9, 10]
# After moving even elements:  [1, 4, 60, 10, 25, 25, 5, 4, 7, 9]
# The second largest value is:  25
# The list is in increasing order:  False
# The list has adjacent duplicates:  True
# The list has duplicates:  True