import re
from math import prod

# Part 1
def wf1(workflows, parts):
    count = 0
    for part in parts:
        outcome = 'in'
        while outcome not in 'AR':
            outcome = util(workflows[outcome], part)
        if outcome == 'A':
            count += sum(part.values())
    return count

def util(workflow, part):
    for cat, op, limit, outcome in workflow[:-1]:
        if (op == '<' and part[cat] < int(limit)) or (op == '>' and part[cat] > int(limit)):
            return outcome
    return workflow[-1][0]


# Part 2
def wf2(workflows):
    def solve(bounds, instate):
        # Returns the number of 'A's
        if instate == 'A':
            return prod(b - a + 1 for a, b in bounds.values())
        if instate == 'R':
            return 0
    
        count = 0
        nonsat = bounds.copy()
        for cat, op, limit, outcome in workflows[instate][:-1]:
            sat = {k: v.copy() for k, v in nonsat.items()}

            # Check if all numbers already satisfy the rule
            if (op == '<' and int(limit) > nonsat[cat][1]
                or op == '>' and nonsat[cat][0] > int(limit)):
                return solve(nonsat, outcome)

            # Check if any numbers satisfy the rule
            if (op == '<' and int(limit) < nonsat[cat][0]
                or op == '>' and int(limit) > nonsat[cat][1]):
                continue

            # Split the bounds
            if op == '<':
                nonsat[cat][0] = int(limit)
                sat[cat][1] = int(limit) - 1
            if op == '>':
                nonsat[cat][1] = int(limit)
                sat[cat][0] = int(limit) + 1
            
            # Send the portion that satisfies the rule to the appropriate state
            count += solve(sat, outcome)
        
        # Check the remaining portion to the default state
        if workflows[instate][-1][0] == 'A':
            return count + prod(b - a + 1 for a, b in nonsat.values())

        return count + solve(nonsat, workflows[instate][-1][0])
        
    l, r = 1, 4000
    start = {c: [l, r] for c in 'xmas'}
    return solve(start, 'in') 


with open('input.txt') as file:
    workflows = {}
    line = file.readline()
    while line != '\n':
        newline = line.strip().replace('}', '').split('{')
        rule = newline[1].split(',')
        newrule = []
        for i in range(len(rule)):
            subrule = re.split(r'>|<|:', rule[i].strip())
            if '<' in rule[i]:
                subrule.insert(1, '<')
            elif '>' in rule[i]:
                subrule.insert(1, '>')
            newrule.append(subrule)
        workflows[newline[0]] = newrule
        line  = file.readline()
    

    parts = []
    line = file.readline()
    while line:
        props = [prop.split('=') for prop in re.sub('{|}', '', line.strip()).split(',')]
        parts.append({k: int(v) for k, v in props})
        line = file.readline()

    print(wf1(workflows, parts))
    print(wf2(workflows))
