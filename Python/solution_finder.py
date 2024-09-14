# Finds the solutions to project euler using keys

solutions = {"001" : 233168,
             "002" : 4613732,
             "004" : 906609,
             "006" : 25164150,
             "007" : 104743,
             "010" : 142913828922,
             "014" : 837799,
             "016" : 1366,
             "020" : 648,
             "025" : 4782,
             "029" : 9183,
             "048" : 9110846700
                       
}


def solution_finder(key):
    return solutions[key]

print("Input the number of the problem in XXX format (e.g. : 017 )")
print(solution_finder(input("Number of the problem : ")))
