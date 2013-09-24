import sys
def get_problem(infile):
    T, K = infile.next().strip().split(' ')
    return (int(K), [[c for c in row] for row in [infile.next().strip() for
                                                i in range(int(T))]])

# shift to the right
def rotate(case):
    T  = len(case)
    for row in range(T):
        # start from right most
        x  = T - 1
        # from right to left
        for col in reversed(range(T)):
            if case[row][col] != '.':
                case[row][x] = case[row][col]
                x  = x -1
        # fill the left blank with .
        while x >= 0:
            case[row][x] = '.'
            x = x - 1

def check_a_pos(case, K, c, pt, inc):
    '''
    Args:
        pt: (row, col)
    '''
    #print("pos"+str(pt)+"inc"+str(inc)+"c"+c)
    T = len(case)
    for step in range(K):
        row = pt[0]+inc[0]*step
        col = pt[1]+inc[1]*step
        if row <0 or row >= T or col < 0 or col >= T:
            return False
        elif case[row][col] != c:
            return False;
    return True

def check_all(case, K, c):
    T = len(case)
    for row in range(T):
        for col in range(T):
            if case[row][col] == c:
                if check_a_pos(case, K, c, (row,col), (0,1)):
                    return True
                if check_a_pos(case, K, c, (row,col), (1,0)):
                    return True
                if check_a_pos(case, K, c, (row,col), (1,1)):
                    return True
                if check_a_pos(case, K, c, (row, col), (-1,1)):
                    return True
    return False


def solve_problem(prob):
    K = prob[0]
    # print(K)
    case = prob[1]
    rotate(case)
    #for row in case:
        #print row

    r = check_all(case, K, 'R')
    b = check_all(case, K, 'B')
    if r and b:
        # print("Both")
        return "Both"
    elif r and not b:
        # print("Red")
        return "Red"
    elif not r and b:
        # print("Blue")
        return "Blue"
    else:
        # print("Neither")
        return "Neither"



def main():
    infile = open(sys.argv[1], 'r')
    outfile = open(sys.argv[2], 'w')
    N = int(infile.next())
    problems = [get_problem(infile) for i in range(N)]
    results = [solve_problem(prob) for prob in problems]
    for i in range(len(results)):
        outfile.write("Case #{0}: {1}\n".format(i+1, results[i]))

if __name__ == "__main__":
    main()
