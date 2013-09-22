import sys
from sets import Set
def get_problem(infile):
    M = int(infile.next())
    return [infile.next().strip().split(' ') for i in range(M)]


def solve(problem):
    incomp_map = {}
    pair_iter = iter(problem)
    first_pair = pair_iter.next()
    # create a map
    for pair in pair_iter:
        if pair[0] not in incomp_map:
            incomp_map[pair[0]] = [pair[1]]
        else:
            incomp_map[pair[0]].append(pair[1])

        if pair[1] not in incomp_map:
            incomp_map[pair[1]] = [pair[0]]
        else:
            incomp_map[pair[1]].append(pair[0])

    # print(incomp_map)

    set_A_new = Set([first_pair[0]])
    set_A_old = Set()
    set_B_new = Set([first_pair[1]])
    set_B_old = Set()
    while(True):
        if(not set_A_new and not set_B_new and incomp_map):
            (key, items) = incomp_map.popitem()
            set_A_new.add(key)
            for item in items:
                set_B_new.add(item)
        elif(not set_A_new and not set_B_new and not incomp_map):
            break;

        while(set_A_new):
            # print(set_A_new)
            A_item = set_A_new.pop()
            set_A_old.add(A_item)
            if A_item not in incomp_map:
                break;
            B_items = incomp_map.pop(A_item)
            for B_item in B_items:
                if B_item in set_A_old or B_item in set_A_new:
                    # print('B'+B_item)
                    return 'No'
                elif B_item not in set_B_old:
                    set_B_new.add(B_item)

        while(set_B_new):
            # print(set_B_new)
            B_item = set_B_new.pop()
            set_B_old.add(B_item)
            if B_item not in incomp_map:
                break;
            A_items = incomp_map.pop(B_item)
            for A_item in A_items:
                if A_item in set_B_old or A_item in set_B_new:
                    #print('B'+A_item)
                    return 'No'
                elif A_item not in set_A_old:
                    set_A_new.add(A_item)
    return 'Yes'



def main():
    infile = open(sys.argv[1], 'r')
    outfile = open(sys.argv[2], 'w')
    T = int(infile.next())
    problems =[get_problem(infile) for i in range(T)]
    results = [solve(problem) for problem in problems]
    for i in range(len(results)):
        outfile.write("Case #{0}: {1}\n".format(i+1, results[i]))

if __name__ == "__main__":
    main()


