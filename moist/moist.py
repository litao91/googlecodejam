import sys

def get_problem(infile):
    N = int(infile.next())
    return [infile.next().strip() for i in range(N)]

def solve_problem(case):
    card_iter = iter(case)
    smallest = card_iter.next()
    count = 0
    for card in card_iter:
        if card < smallest:
            count = count+1
        else:
            smallest = card

    return count


def main():
    infile = open(sys.argv[1], 'r')
    outfile = open(sys.argv[2], 'w')
    T = int(infile.next())
    R = [solve_problem(get_problem(infile)) for i in range(T)]
    for j in range(len(R)):
        outfile.write("Case #{0}: {1}\n".format(j+1, R[j]))

if __name__ == "__main__":
    main()

