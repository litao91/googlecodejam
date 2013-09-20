import sys
import re
def parse_case(case, word_length):
    base = "(\([a-z]+\)|[a-z])"
    regex = ''
    for i in range(word_length):
        regex = regex+base
    regex = re.compile(regex)
    lst =  [chars.replace('(','').replace(')','') for chars in
            regex.search(case).groups()]
    return lst

def is_match(word, case):
    #print(word)
    #print(case)
    #print('')
    for i in range(len(case)):
        if case[i].find(word[i]) < 0:
            return False
    return True

def main():
    infile = open(sys.argv[1], 'r');
    outfile = open(sys.argv[2], 'w')
    counts = [int(num) for num in infile.next().split(' ')]
    word_length = counts[0]
    vocab_count = counts[1]
    num_cases = counts[2]
    vocab = []
    for i in range(vocab_count):
        vocab.append(infile.next())


    for j in range(num_cases):
        count = 0
        case = infile.next()
        char_lst = parse_case(case, word_length)
        for word in vocab:
            if(is_match(word.replace('\n', ''), char_lst)):
                count= count+1
        outfile.write("Case #{0}: {1}".format(j+1, count) +'\n')
if __name__ == "__main__":
    main()
