import sys
def read_problem(infile):
    B = int(infile.next())
    prob = []
    for i in range(B):
        prob.append([int(j) for j in infile.next().split(' ')])
    return (B,prob)
    # do something

def get_dis(pos1, pos2):
    return abs(pos1[0]-pos2[0])+abs(pos1[1]-pos2[1])


def solve_problem(prob):
    B = prob[0]
    poses = prob[1]
    people = []
    for i in range(B):
        x1 = poses[i][0]
        y1 = poses[i][1]
        x2 = poses[i][2]
        y2 = poses[i][3]
        for j in range(x1, x2+1):
            for k in range(y1,y2+1):
                people.append((j,k))

    min_dis = -1
    min_pos = (-1,-1)
    for pos1 in people:
        m_sum = 0
        for pos2 in people:
            m_sum+=get_dis(pos1,pos2)
        if min_dis<0 or min_dis >= m_sum:
            if min_dis!=m_sum:
                min_dis = m_sum
                min_pos = pos1
            else:
                if min_pos[0] > pos1[0]:
                    min_pos = pos1
                elif min_pos[0] == pos1[0] and min_pos[1]>pos1[1]:
                    min_pos = pos1





    return "{} {} {}".format(min_pos[0],min_pos[1], min_dis)

def main():
    infile = open(sys.argv[1], 'r')
    outfile = open(sys.argv[2], 'w')
    T = int(infile.next())
    problems = [read_problem(infile) for i in range(T)]
    results = [solve_problem(prob) for prob in problems]
    for i in range(T):
        outfile.write("Case #{}: {}\n".format( i+1, results[i]))

if __name__ == "__main__":
    main()
