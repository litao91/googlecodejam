import sys
def read_problem(infile):
    r =  [infile.next() for i in range(4)]
    try:
        infile.next()
    except:
        return r
    return r

def check_win_pos(prob, pos,direct, who):
    pure_t = True
    #print("Pos: "+str(pos))
    #print("Dir:" + str(direct))

    i = pos[0]
    for p in range(4):
        i = pos[0]+direct[0]*p
        j = pos[1]+direct[1]*p
        #print(i,j)
        if i >= 4 or j>=4 or i <0 or j <0:
            return False
        elif prob[i][j] != who and prob[i][j] != 'T':
            return False
        elif prob[i][j] == who:
            pure_t = False;
    return not pure_t


def is_filled(prob):
    for line in prob:
        if line.find('.') != -1:
            return False
    return True


def check_win(prob, who):
    for i in range(4):
        for j in range(4):
            if check_win_pos(prob, (i,j),(1,0), who) or \
               check_win_pos(prob, (i,j),(1,1), who) or \
               check_win_pos(prob, (i,j),(0,1), who) or \
               check_win_pos(prob, (i,j),(1,-1), who):
                return True
    return False;

def solve_problem(prob):
    if check_win(prob, 'X'):
        return "X won"
    elif check_win(prob, 'O'):
        return "O won"
    elif is_filled(prob):
        return "Draw"
    else:
        return "Game has not completed"




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
