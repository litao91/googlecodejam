import sys
def read_problem(infile):
    N = int(infile.next())
    matrix = [[char for char in infile.next()] for i in range(N)]
    return (N,matrix)

def check_win(N, matrix, pos, color):
    if matrix[pos[0]pos[1]

    # do something
def solve_problem(prob):
    N = prob[0]
    matrix = prob[1]



def main():
    infile = open(sys.argv[1], 'r')
    outfile = open(sys.argv[2], 'w')
    T = int(infile.next())
    problems = [read_problem(infile) for i in range(T)]
    results = [solve_problem(prob) for prob in problems]
    for i in range(T):
        outfile.write("Case #{}: {}\n".format( i+1, results[i]))

if __name__ == "__main__":
    main()
