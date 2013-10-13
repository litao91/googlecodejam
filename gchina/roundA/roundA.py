import sys
def read_problem(infile):
    prob = []
    n = int(infile.next())
    for i in range(n*n):
        prob.append([int(j) for j in infile.next().split(' ')])
    return (n,prob)
    # do something
def check_line(pos, prob, dir):
    n = prob[0]*prob[0]
    matrix = prob[1]
    val_set = set()
    p =[pos[0], pos[1]]
    for i in range(n):
        x  = p[0]+dir[0]*i
        y = p[1] + dir[1]*i
        #print(x,y)
        if matrix[x][y] in val_set or matrix[x][y]>n or matrix[x][y]<=0:
            return False
        else:
            val_set.add(matrix[x][y])
    return True

def check_square(pos, prob):
    n = prob[0]
    matrix = prob[1]
    val_set = set()
    p =[pos[0], pos[1]]
    for i in range(n):
        for j in range(n):
            x = p[0]+i
            y = p[0]+j
            if matrix[x][y] in val_set:
                return False
            else:
                val_set.add(matrix[x][y])
    return True



def solve_problem(prob):
    # check rows
    n = prob[0]
    n2 = prob[0]*prob[0]
    for i in range(n2):
        if not check_line((0,i),prob, (1,0)):
            return "No"
        if not check_line((i,0), prob, (0,1)):
            return "No"
    for i in range(0,n2,n):
        for j in range(0,n2,n):
            if not check_square((i,j), prob):
                return "No"
    return "Yes"



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
