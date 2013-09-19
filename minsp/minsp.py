import sys
def main():
    infile = open(sys.argv[1], 'r')
    outfile = open(sys.argv[2], 'w')
    case_num = int(infile.next())
    for i in range(case_num):
        vec_len = int(infile.next())
        vec_1 = sorted([int(mem) for mem in infile.next().split(' ')])
        vec_2 = sorted([int(mem) for mem in infile.next().split(' ')])
        min_sum = 0
        for j in range(vec_len):
            min_sum = min_sum + vec_1[j]*vec_2[-j-1]
        outfile.write("Case #{0}: {1}\n".format(i+1, min_sum))


if __name__ == "__main__":
    main()

