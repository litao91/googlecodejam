import sys
def del_new_line(s):
    return s.replace("\n", '')
def main():
    infile = open(sys.argv[1], 'r')
    outfile = open(sys.argv[2], 'w')
    infile.next()
    count = 1
    for line in infile:
        tokens = [del_new_line(s) for s in line.split(' ')]
        tokens.reverse()
        revsed = ' '.join(tokens)
        outfile.write("Case #{0}: ".format(count)+ revsed+'\n')
        count = count+1

if __name__ == "__main__":
    main()
