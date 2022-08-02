# SOLUTION

class AttendClass():
    def __init__(self):
        self.mapping = {}
        
    def ways_to_attend_classes(self,N): 
        """
        Function to compute total number of ways to attend the classes.
        A valid way to attend the classes is where classes are NOT missed for four or more consecutive days
        """
        if N<4:                    
            ways = 2**N
            self.mapping[N] = ways
            return(ways)
        elif N==4:
            ways = 15
            self.mapping[N] = ways
            return(ways)
        elif N in self.mapping.keys():
            return(self.mapping[N])
        else:
            ways = self.ways_to_attend_classes(N-1) + \
                    self.ways_to_attend_classes(N-2) + \
                    self.ways_to_attend_classes(N-3) + \
                    self.ways_to_attend_classes(N-4)
            self.mapping[N] = ways
            return(ways)
        
    def ways_miss_graduation(self,N):
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
            ways = self.ways_to_attend_classes(N-4) + \
                    self.ways_to_attend_classes(N-3) + \
                        self.ways_to_attend_classes(N-2)
            return(ways)


