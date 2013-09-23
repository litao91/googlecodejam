import sys
from sets import Set

def get_problem(infile):
    NM = [int(val) for val in infile.next().strip().split(' ')]
    N = NM[0]
    M = NM[1]
    exist_dir = None
    new_dir = None
    exist_dir = [infile.next().strip() for i in range(N)]
    new_dir = [infile.next().strip() for j in range(M)]
    return (exist_dir, new_dir)
def insert_dir_to_set(S, new_dir):
    tokens = new_dir.split('/')
    for res in expand_dir(tokens):
        S.add(res)

def expand_dir(tokens):
    tokens.pop(0)
    for i in range(len(tokens)):
        res = ''
        for j in range(i+1):
           res = res+'/'+tokens[j]
           yield res

def solve_problem(case):
    exist_dir = case[0]
    new_dir = case[1]
    dir_set = Set()
    for d in exist_dir:
        insert_dir_to_set(dir_set, d)
    count = 0
    for d in new_dir:
        expanded = expand_dir(d.split('/'))
        for d in expanded:
            if d not in dir_set:
                dir_set.add(d)
                count = count+1
    return count




def main():
    infile = open(sys.argv[1], 'r')
    outfile = open(sys.argv[2],'w')
    T = int(infile.next())
    problems = [get_problem(infile) for i in range(T)]
    result = [solve_problem(case) for case in problems]
    for i in range(len(result)):
        outfile.write("Case #{0}: {1}\n".format(i+1, result[i]))



if __name__ == "__main__":
    main()

