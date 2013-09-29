import sys
def get_problem(infile):
    return [sym for sym in infile.next()]

def to_decimal(val, base):
    decimal = 0
    b = 1
    for digit in reversed(val):
        if(str.isdigit(digit)):
            decimal = decimal + b*int(digit)
        else:
            decimal = decimal + b*(ord(digit)-ord('a')+10)
        b = b*base
    return decimal


def solve_problem(prob):
    val_dict = {}
    val_dict[prob[0]] = 1
    max_digit = 1
    val = '1'
    is_zero_used = False
    for i in range(1,len(prob)-1):
        if prob[i] in val_dict:
            val=val+str(val_dict[prob[i]])
        elif not is_zero_used:
            is_zero_used = True
            val_dict[prob[i]] = 0
            val = val + str(0)
        else:
            max_digit = max_digit+1
            val_dict[prob[i]] = max_digit
            if(max_digit<10):
                val = val+str(max_digit)
            else:
                val = val+chr(ord('a')+max_digit-10)

    return to_decimal(val, max_digit+1)

def main():
    infile = open(sys.argv[1], 'r')
    outfile = open(sys.argv[2], 'w')
    N = int(infile.next())
    problems  = [get_problem(infile) for i in range(N)]
    results = [solve_problem(prob) for prob in problems]
    for i in range(len(results)):
        outfile.write("Case #{}: {}\n".format(i+1, results[i]))


if __name__ == "__main__":
    main()
