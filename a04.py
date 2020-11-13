### YOUR CODE FOR openLocks() FUNCTION GOES HERE ###
def openLocks(number_of_lockers, number_of_students):
    list=["opened"]*number_of_lockers
    lockersopened = 0
    c=0
    if number_of_lockers==0:
        return 0
    if number_of_lockers<0:
        return None
    if number_of_students==0:
        return 0
    if number_of_students<0:
        return None
    
    for s in range(1,number_of_lockers+1):
        for r in range(2, number_of_students+1):
            if s%r==0:
                if list[s-1]=="closed":
                    list[s-1]="opened"
                else:
                    list[s-1]="closed"                
    while c< number_of_lockers:
        if list[c]=="opened":
            lockersopened = lockersopened + 1
        c = c + 1
    return lockersopened
    print (list)
#### End OF MARKER





### YOUR CODE FOR mostTouchableLocker() FUNCTION GOES HERE ###
def mostTouchableLocker(number_of_lockers,number_of_students): 
    if number_of_lockers < 0 or number_of_students < 0:
        return None
    if number_of_lockers == 0 or number_of_students== 0:
        return 0
    list=[0]*number_of_lockers
    counter=number_of_lockers
    for i in range(1, number_of_lockers + 1):
        for j in range(1,number_of_students + 1):
            if i%j==0:
                list[i-1] += 1
    maximum = max(list)
    x = list[::-1].index(maximum)
    y = len(list) - x
    return y
#### End OF MARKER


