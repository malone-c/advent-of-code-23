import math

def boat1(times, dists):
    res = 1
    for i in range(len(times)):
        t, r = times[i], dists[i]
        count = 0
        for s in range(t):
            if s * t - s**2 > r:
                count += 1
        res *= count
    return res

if __name__ == '__main__':
    times = [47, 98, 66, 98]
    dists = [400, 1213, 1011, 1540]
        
    print(boat1(times, dists))
    
    times = [47986698]
    dists = [400121310111540]
        
    print(boat1(times, dists))