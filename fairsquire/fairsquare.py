import sys
import math
prob_cnt = 0
def is_pali(num):
    nstr = str(num)
    n = len(nstr)
    for i,j in zip(range(n), reversed(range(n))):
        if i>=j:
            return True
        if nstr[i] != nstr[j]:
            return False

def read_problem(infile):
    return [int (i) for i in infile.next().split(' ')]
    # do something
def solve_problem(prob):
    global prob_cnt
    prob_cnt+=1
    print(prob_cnt)
    #print("====")
    A = prob[0]
    B = prob[1]
    low = int(math.floor(math.sqrt(A)))
    up = int(math.ceil(math.sqrt(B)))
    n_lo = len(str(low))
    n_hi = len(str(up))
    low = int(max(0,low/(10**(n_lo/2+1))))
    up = int(math.ceil(up/(10**(n_hi/2-1))))
    #print(low,up)
    count = 0
    for i in range(low, up):
        rev = "".join(reversed(str(i)))
        for d in ['','0','1','2','3','4','5','6','7','8','9']:
            pal = 0
            if(i!=0):
                pal = int(""+str(i)+d+rev)
            elif d!='':
                pal = int(d)
            #print(pal)
            square = pal**2
            if square>= A and square <= B:
                if is_pali(i) and is_pali(square):
                    count+=1
    return count

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
