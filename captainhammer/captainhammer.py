import sys
import math
def solve_problem(case):
    V = case[0]
    D = case[1]
    sin_val = 9.8/(V*V)*D
    if(sin_val<=1):
        return 0.5*math.degrees(math.asin(9.8/(V*V)*D))
    elif(sin_val-1<= 0.00001):
        return 45


def main():
    infile = open(sys.argv[1],'r')
    outfile = open(sys.argv[2],'w')
    T = int(infile.next())
    problems = [[int(val) for val in infile.next().strip().split(' ')]
                for i in range(T)]
    results = [solve_problem(case) for case in problems]

    for i in range(len(results)):
        outfile.write("Case #{0}: {1}\n".format(i+1, results[i]))


if __name__ == "__main__":
    main()


