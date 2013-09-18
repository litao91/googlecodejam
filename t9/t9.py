import sys


def get_t9(c):
    #print('c: ' + str(c))
    if c != ' ':
        order = ord(c) - ord('a')
        if order<0 or order>25:
            return ''

        val = order/3+2
        rem = order%3+1
        if val == 8 and rem == 1:
            val = 7
            rem = 4
        elif val == 8:
            rem = rem-1
        elif val == 9 and rem == 1:
            val = 8
            rem = 3
        elif val == 9:
            rem = rem-1
        elif val == 10:
            val = 9
            rem = rem + 2


        #print("val"+str(val)+"rem"+str(rem))
        r_str = ''
        for i in range(rem):
            r_str= r_str+str(val)

        #print(r_str)
        return r_str
    else:
        return str(0)
def join_t9(str_lst):
    r_str = str_lst[0]
    for i in range(1, len(str_lst)-1):
        if(str_lst[i-1][-1] == str_lst[i][0]):
            r_str = r_str +' '
        r_str = r_str+str_lst[i]
    return r_str

def main():
    infile =open(sys.argv[1], 'r')
    outfile = open(sys.argv[2], 'w')
    infile.next()
    count = 1

    for line in infile:
        line.replace('\n', '')
        t9 = join_t9( [get_t9(c) for c in line])
        outfile.write("Case #{0}: ".format(count) + t9 +'\n')
        count = count+1

if __name__ == "__main__":
    main()


