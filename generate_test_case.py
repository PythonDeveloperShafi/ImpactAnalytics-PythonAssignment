import re

def total_ways(N):
    att =["P","A"]
    lst = ["P","A"]
    i = 1
    while i < N:
        new_lst = []
        for item in att:
            for elem in lst:
                new_lst.append(item+elem)
        i+=1
        lst = new_lst.copy()
        del new_lst
    return(lst)

def invalid_ways(ways):
    lst = []
    for elem in ways:
        if len(re.findall("AAAA", elem)) != 0:
               lst.append(elem)
    return lst

def ways_with_Absent_last(ways):
    lst = []
    for elem in ways:
        if elem[-1] == "A":
            lst.append(elem)
    return lst     

def generate_test_case(N):
    ways = total_ways(N)
    invalid = invalid_ways(ways)
    valid = [x for x in ways if x not in invalid]
    absent = ways_with_Absent_last(valid)

    # print(f"Total Number of ways to attend classes over {N} days = {len(valid)}")
    # print(f"Number of ways in which the graduation ceremony will be missed = {len(absent)}")

    # print(f"Total number of Ways to attend classes over {N} days:")
    # print(*ways, sep = ", ")
    # print(f"count = {len(ways)}")

    # print(f"Invalid Ways to attend classes over {N} days:")
    # print(*invalid, sep = ", ")
    # print(f"count = {len(invalid)}")

    # print(f"Valid Ways to attend classes over {N} days:")
    # print(*valid, sep = ", ")
    # print(f"count = {len(valid)}")

    # print("Ways in which the graduation ceremony will be missed i.e. Class is missed on last day:")
    # print(*absent, sep = ", ")
    # print(f"count = {len(absent)}")

    print(f"Therefore, Answer of (1) = {len(valid)} , Answer of (2) = {len(absent)}/{len(valid)}")


N = int(input())
generate_test_case(N)
