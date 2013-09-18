import sys

def stockcredit(c_num, C, I, P, outfile):
    # build a value-index map
    more_list = []
    vi_dict = {}
    half = C/2
    for i in range(I):
        if P[i] >= half:
            more_list.append(i)
        if P[i] <= half:
            vi_dict[P[i]] = i
    #print(vi_dict)



    for idx in more_list:
        subs =  C - P[idx]
        if subs in vi_dict:
            idx1 = idx+1
            idx2 = vi_dict[subs]+1
            if(idx1==idx2):
                continue
            if(idx1>idx2):
                tmp = idx1
                idx1 = idx2
                idx2 = tmp
            outfile.write("Case #{0}: {1} {2}\n".format(c_num+1, idx1,
                                                        idx2))
            break;


def main():
    filename = sys.argv[1]
    outfile = open(sys.argv[2], 'w')

    infile = open(filename, 'r')
    N = int(infile.next())
    for i in range(N):
        C = int(infile.next())
        I = int(infile.next())
        P = [int(num) for num in infile.next().split(' ')]
        stockcredit(i, C,I,P, outfile)

if __name__ == "__main__":
    main()







