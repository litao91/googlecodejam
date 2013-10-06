import sys
import math
def get_problem(line):
    tokens =  line.split(' ')
    return (int(tokens[0]), int(tokens[1]))



def solve_problem(prob):
    r = prob[0]
    t = prob[1] # millilitres of black paint
    #return int(math.floor(-r + math.sqrt(4*(r*r)+4*t)/2))
    #print((-2*r+1+math.sqrt((2*r-1)*(2*r-1)+8*t))/4)
    # return math.floor((-2*r+1+math.sqrt((2*r-1)**2+8*t))/4)
    res, lo, hi = 0, 1, t
    while lo <= hi:
        mid = math.floor((lo + hi) / 2)
        if mid * ( 2 * r + 2 * mid -1) > t:
            hi = mid -1
        else:
            lo, res = mid+1, mid
    return int(res)


    #paint_used = 0
    #cur_r = r
    #count = 0
    #while True:
        #paint_used += (cur_r+1)**2 - cur_r**2
        #if paint_used > t:
            #return count
        #cur_r += 2
        #count += 1


def main():
    infile = open(sys.argv[1],'r')
    outfile = open(sys.argv[2], 'w')
    T = int(infile.readline())
    problems = [get_problem(infile.readline()) for i in range(T)]
    results = [solve_problem(prob) for prob in problems]
    for i in range(len(results)):
        outfile.write("Case #{}: {}\n".format(i+1, results[i]))

if __name__ == "__main__":
    main()
