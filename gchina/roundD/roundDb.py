import sys
length = -1
credit = 0
checked = set()
def helper(M, N, clength, ccredit, matrix, en, ex):
    print('haha'+str(en))
    global checked
    global length
    global credit
    if en in checked:
        return
    else:
        checked.add(en)

    if en[0]>=M or en[1]>=N or en[0]<0 or en[1]<0:
        print('a')
        return
    elif matrix[en[0]][en[1]] == -1:
        print('b')
        return
    elif en[0] == ex[0] and en[1] == ex[1]:
        ccredit = ccredit + matrix[en[0]][en[1]]
        clength = clength+1
        if length<0 or clength < length:
            length=clength
            credit=ccredit
        elif clength==length:
            if credit < ccredit:
                credit = ccredit
        print('c')
        return
    print('heihei'+str(en))

    helper(M,N,clength+1, ccredit+matrix[en[0]][en[1]],matrix, (en[0]+1,en[1]),ex)
    helper(M,N,clength+1, ccredit+matrix[en[0]][en[1]],matrix, (en[0]-1,en[1]),ex)
    helper(M,N,clength+1, ccredit+matrix[en[0]][en[1]],matrix, (en[0],en[1]+1),ex)
    helper(M,N,clength+1, ccredit+matrix[en[0]][en[1]],matrix, (en[0],en[1]-1),ex)


def solve_problem(prob):
    global length
    global credit
    global checked
    length=-1
    credit=0
    checked = set()
    en = prob[0]
    ex = prob[1]
    matrix = prob[2]
    M = prob[3]
    N = prob[4]
    helper(M,N,0,0,matrix,en,ex)
    if length == -1:
        return "Mission Impossible"
    else:
        return credit



def read_problem(infile):
    pack= [int(i) for i in infile.next().split(' ')]
    M = pack[0]
    N = pack[1]
    en_x, en_y, ex_x, ex_y = [int(i) for i in infile.next().split(' ')]
    en = (en_x,en_y)
    ex = (ex_x, ex_y)
    matrix = [[int(j) for j in infile.next().split(' ')] for i in range(M)]
    return (en, ex, matrix,M,N)

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
