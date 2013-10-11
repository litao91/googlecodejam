import sys
def read_problem(infile):
    M, N = [ int(v) for v in infile.next().split(' ')]
    vals =  [[int(v) for v in infile.next().split(' ')]for i in range(M)]
    return (M,N, vals)
    # do something


def arr_all_leq(arr, val):
    for v in arr:
        if v > val:
            return False
    return True

def solve_problem(prob):
    M = prob[0]
    N = prob[1]
    shape = prob[2]
    val_dict = {}
    for i in range(M):
        for j in range(N):
            if shape[i][j] not in val_dict:
                val_dict[shape[i][j]] = []
            val_dict[shape[i][j]].append((i,j))
    val_lst = sorted([key for key in val_dict.iterkeys()])
    # from small to large
    for val in val_lst:
        poses = val_dict[val]
        for pos in poses:
            row_ok = True
            col_ok = True
            #print("=====")
            #print(pos)
            row = shape[pos[0]]
            col = [shape[i][pos[1]] for i in range(M)]
            #print(val)
            #print(row)
            #print(col)
            if not arr_all_leq(row, val):
                row_ok = False
            if not arr_all_leq(col, val):
                col_ok = False
            if not (row_ok or col_ok):
             #   print(pos)
                return "NO"
    return "YES"


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
