import unittest
from solution import AttendClass


class TestSolution(unittest.TestCase):
    def test_solution(self):
        with open("./test_cases/cases.txt") as fp:
            test_cases = [line.rstrip('\n') for line in fp]
        #test_cases = open("./test_case/dev.txt").read().splitlines()
        for case in test_cases:
            inp, ans1, ans2 = case.split(" ")  
            N = int(inp)
            result1 = f"{AttendClass().ways_to_attend_classes(N)}"
            result2 = f"{AttendClass().ways_miss_graduation(N)}/{AttendClass().ways_to_attend_classes(N)}"
            self.assertEqual(result1,ans1)
            self.assertEqual(result2,ans2)
        

if __name__ == '__main__':
    unittest.main()