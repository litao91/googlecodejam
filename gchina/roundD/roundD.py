import sys
def read_problem(infile):
    pack= [int(i) for i in infile.next().split(' ')]
    M = pack[0]
    N = pack[1]
    en_x, en_y, ex_x, ex_y = [int(i) for i in infile.next().split(' ')]
    en = (en_x,en_y)
    ex = (ex_x, ex_y)
    matrix = [[int(j) for j in infile.next().split(' ')] for i in range(N)]
    return (en, ex, matrix)

def get_submatrix(en, ex, matrix):
    stepx = 1
    stepy = 1
    sizex = 0
    sizey = 0
    if en[0]-ex[1] > 0:
        stepx =  -1

    if en[1]-ex[1] > 0:
        stepy = -1
    sizex = abs(en[0]-ex[0])
    sizey = abs(en[1]-ex[1])
    submatrix = []
    for i in range(en[0],ex[0]+stepx, stepx):
        submatrix.append([])
        for j in range(en[1],ex[1]+stepy, stepy):
            submatrix[-1].append(matrix[i][j])
    return (sizex+1, sizey+1, submatrix)


    # do something
def solve_problem(prob):
    en = prob[0]
    ex = prob[1]
    matrix = prob[2]
    sizex, sizey, submatrix = get_submatrix(en,ex,matrix)
    credit_matrix = [[None for i in range(sizey)] for j in range(sizex)]
    # initial condition of dy
    credit_matrix[0][0] = submatrix[0][0]
    print(submatrix)
    for x in range(1,max(sizex, sizey)-1):
        if x > sizey:
            break;
        for y in range(max(sizex, sizey)-1):
            i = y
            j = x-y
            if j < 0 or j<0:
                break
            elif i>sizex or j > sizey:
                continue


            if matrix[i][j] == -1:
                credit_matrix[i][j] = -1
            else:
                cur_credit = matrix[i][j]
                max_credit = -1
                if i-1>=0:
                    if matrix[i-1][j]!=-1 and cur_credit+matrix[i-1][j] > max_credit :
                        max_credit = cur_credit+matrix[i-1][j]
                if j-1>=0:
                    if matrix[i][j-1]!=-1 and cur_credit+matrix[i][j-1] > max_credit :
                        max_credit = cur_credit+matrix[i][j-1]
                credit_matrix[i][j] = max_credit
    if submatrix[sizex-1][sizey-1] == -1:
        return "Mission Impossible"
    else:
        return str(submatrix[sizex-1][sizey-1])

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
