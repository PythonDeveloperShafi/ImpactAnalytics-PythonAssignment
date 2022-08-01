# PROVIDE INPUT i.e. number of days in the academic year
N = int(input())


# SOLUTION
mapping = {} # dictionary to store the repeating values so as to reduce the time.

def ways_to_attend_classes(N): 
    """
    Function to compute total number of ways to attend the classes.
    A valid way to attend the classes is where classes are NOT missed for four or more consecutive days
    """
    
    if N<4:                    
        ways = 2**N
        mapping[N] = ways
        return(ways)
    elif N==4:
        ways = 15
        mapping[N] = ways
        return(ways)
    elif N in mapping.keys():
        return(mapping[N])
    else:
        ways = ways_to_attend_classes(N-1) + \
                ways_to_attend_classes(N-2) + \
                ways_to_attend_classes(N-3) + \
                ways_to_attend_classes(N-4)
        mapping[N] = ways
        return(ways)
    
def ways_miss_graduation(N):
    """
    Function to compute number of ways in which the graduation ceremony will be missed.
    The graduation ceremony is on the last day of the academic year.
    Hence, missing the class on the last day means the graduation ceremong will be missed.
    """
    
    if N<4:
        return(2**(N-1))
    elif N==4:
        return(7)
    else:
        ways = ways_to_attend_classes(N-4) + \
                ways_to_attend_classes(N-3) + \
                    ways_to_attend_classes(N-2)
        return(ways)

# PRINT THE REQUIRED ANSWERS
print(f"Answer of (1) = {ways_to_attend_classes(N)}")
print(f"Answer of (2) =  {ways_miss_graduation(N)}/{ways_to_attend_classes(N)}")
