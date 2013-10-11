import sys
import operator

solve_count = 0
class Activity:
    def __init__(self,pos, val, E):
        self.pos = pos
        self.val = val
        self.upper_limit = E # max that it can have
        self.lower_limit = 0 # min that it should save
        self.considered = False
        self.energy = 0

    def __str__(self):
        return "Pos: {}, Val: {}, Lim: {}\n".format(self.pos, self.val,
                                                    self.limit)

def read_problem(infile):
    E, R, N = [int(val) for val in infile.next().strip().split(' ')]
    credits = [int(val) for val in infile.next().strip().split(' ')]
    return (E,R, N, credits)



def solve_problem(prob):
    global solve_count
    solve_count+=1
    print(solve_count)
    E = prob[0]
    R = prob[1]
    N = prob[2]
    credits = prob[3]
    # sort it from small to large
    activities = sorted([Activity(i, credits[i], E) for i in range(N)],key=operator.attrgetter('val'))
    # create dict by value
    #val_idx_dict = {}
    #for act in activities:
        #val_idx_dict[act.val] = act.pos

    for i in reversed(range(N)):
        activities[i].considered = True
        activities[i].energy = max(activities[i].upper_limit-activities[i].lower_limit,0)
        for j in range(N):
            if not activities[j].considered:
                p_diff = activities[j].pos - activities[i].pos
                if p_diff > 0:
                    activities[j].upper_limit = min(activities[j].upper_limit,
                                                    R*p_diff, E)
                elif p_diff < 0:
                    activities[j].lower_limit = min(max(activities[j].lower_limit,
                                                    activities[i].lower_limit+activities[i].energy
                                                        + R*p_diff,0),E)
    sum = 0
    for act in activities:
        e =  min(E,act.energy)
        sum+=e*act.val
        E  = E-e+R
    return sum







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

