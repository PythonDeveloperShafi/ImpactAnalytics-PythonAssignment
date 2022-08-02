# ImpactAnalytics-PythonAssignment
This repository is a part of Assignment given by Impact Analytics Company.

## Problem Statement
In a university, your attendance determines whether you will be allowed to attend your graduation ceremony. 
You are not allowed to miss classes for four or more consecutive days. 
Your graduation ceremony is on the last day of the academic year, which is the Nth day.

Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.
Represent the solution in the string format as "Answer of (2) / Answer of (1)", don't actually divide or reduce the fraction to decimal

### Input
An integer N representing number of days in the academic year

### Output
Print the following in new line as a string
**The number of ways to attend classes over N days
**The probability that you will miss your graduation ceremony

### Sample Input 1
5

### Sample Output 1
29
14/29

#### Justification 
###### Total number of Ways to attend classes over 5 days:
    PPPPP, PPPPA, PPPAP, PPPAA, PPAPP, PPAPA, PPAAP, PPAAA, PAPPP, PAPPA, PAPAP, PAPAA, PAAPP, PAAPA, PAAAP, PAAAA, APPPP, APPPA, APPAP, APPAA, APAPP, APAPA, APAAP, APAAA, AAPPP, AAPPA, AAPAP, AAPAA, AAAPP, AAAPA, AAAAP, AAAAA
    count = 32
###### Invalid Ways to attend classes over 5 days:
    PAAAA, AAAAP, AAAAA
    count = 3
###### Valid Ways to attend classes over 5 days:
    PPPPP, PPPPA, PPPAP, PPPAA, PPAPP, PPAPA, PPAAP, PPAAA, PAPPP, PAPPA, PAPAP, PAPAA, PAAPP, PAAPA, PAAAP, APPPP, APPPA, APPAP, APPAA, APAPP, APAPA, APAAP, APAAA, AAPPP, AAPPA, AAPAP, AAPAA, AAAPP, AAAPA
    count = 29
###### Ways in which the graduation ceremony will be missed i.e. Class is missed on last day:
    PPPPA, PPPAA, PPAPA, PPAAA, PAPPA, PAPAA, PAAPA, APPPA, APPAA, APAPA, APAAA, AAPPA, AAPAA, AAAPA
    count = 14

Therefore, Answer of (1) = 29 , Answer of (2) = 14/29