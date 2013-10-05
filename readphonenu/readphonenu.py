import sys
count_dict = ['','double','triple','quadruple','quintuple','sextuple','septuple',\
            'octuple','nonuple','decuple']
num_dict = ['zero', 'one', 'two', 'three', 'four', 'five','six', 'seven', 'eight',\
        'nine']


def get_problem(line):
    num, split = line.split(' ')
    num = [int(c.strip()) for c in num]
    split = [int(d.strip()) for d in split.split('-')]
    return (num, split)

def solve_problem(prob):
    num = prob[0]
    split = prob[1]
    # 11 digits
    i = 0
    read = ''
    dig = -1
    count = 0
    for i in range(len(num)):
        is_in_split = False
        s = 0
        for j in split:
            s = s+j
            if s == i:
                is_in_split = True
                break;
        if is_in_split or dig!=num[i]:
            if(dig!=-1):
                if count >10:
                    for k in range(count):
                        read = read +' ' + num_dict[dig]
                else:
                    read = read + ' ' + count_dict[count-1]
                    read = read + ' ' + num_dict[dig]
            dig = num[i]
            count = 1
        else:
            count = count+1
    if count >10:
        for k in range(count):
            read = read +' ' + num_dict[dig]
    else:
        read = read + ' ' + count_dict[count-1]
        read = read + ' ' + num_dict[dig]
    return read.replace('  ',' ').strip()




def main():
    infile = open(sys.argv[1], 'r')
    outfile = open(sys.argv[2],'w')
    N = int(infile.next())
    problems = [get_problem(infile.next()) for i in range(N)]
    result = [solve_problem(prob) for prob in problems]
    for i in range(len(result)):
        outfile.write("Case #{}: {}\n".format(i+1, result[i]))

if __name__ == "__main__":
    main()
