from collections import deque
from collections import defaultdict
import math

def pulse(dest_map, op_map):
    targets = {'gl': 0, 'bb': 0, 'mr': 0, 'kk': 0}
    q = deque()
    pulse_counts = [0, 0]
    solns = [0, 0]

    for i in range(1, 10_000):
        q.append(('button', 0))
        
        while q:
            # Get new source and input to that source
            source, signal = q.popleft()

            # If target node, add time to first viewing
            if source in targets and signal == targets[source] == 0:
                targets[source] = i

            # Termination conditions
            if source not in dest_map: continue
            if op_map[source] == '%' and signal: continue
            
            # Determine what signal to send
            if op_map[source] == '%':
                signal = flip_map[source] = not flip_map[source]
            elif op_map[source] == '&':
                signal = flip_map[source] = not all(flip_map[parent] for parent in parent_map[source])
            
            # Send the signal
            pulse_counts[signal] += len(dest_map[source])
            q.extend((dest, signal) for dest in dest_map[source])

        # Save part 1 solution
        if i == 1_000:
            solns[0] = math.prod(pulse_counts)

        # Save part 2 solution
        if all(cycle_lengths := targets.values()):
            solns[1] = math.lcm(*cycle_lengths)

        if all(solns):
            return solns

    return


with open('input.txt') as f:
    lines = [line.strip().split(' -> ') for line in f.readlines()]

dest_map = {}
op_map = {}
flip_map = defaultdict(lambda: False)

for line in lines:
    op_map[line[0]] = None

    if line[0][0] in '%&':
        del op_map[line[0]]
        op_map[line[0][1:]] = line[0][0]
        line[0] = line[0].replace('%', '').replace('&', '')
    
    dest_map[line[0]] = line[1].split(', ')

parent_map = defaultdict(list)
for parent, children in dest_map.items():
    for child in children:
        parent_map[child].append(parent)

dest_map['button'] = ['broadcaster']
op_map['button'] = None

print(pulse(dest_map, op_map))