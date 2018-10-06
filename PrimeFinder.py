
# Prime Find
def PrimeFinder(test_num):
    for a_num_less_than_testnum in range(2, test_num):
        if(test_num%a_num_less_than_testnum == 0):
            print("Not a Prime") 
            return 0

    print ("Is Prime")
    return 0

PrimeFinder(186)