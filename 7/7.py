from collections import Counter

def camel(hands, bids):
    ranks, counters = [], []

    # Get hand types and replace Js if applicable
    for hand in hands:
        counter = Counter(hand)
        counters.append(counter)
        if 1 not in counter or counter[1] == 5:
            continue
            
        # Perform J replacement
        n_j = counter[1]
        del counter[1]
        counter[counter.most_common()[0][0]] += n_j

    # Compare hands pairwise
    for i, hand1 in enumerate(hands):
        n_wins = 1
        for j, hand2 in enumerate(hands):
            if i == j:
                continue
            vals1, vals2 = sorted(counters[i].values(), reverse=True), sorted(counters[j].values(), reverse=True)
            if vals1 > vals2 or (vals1 == vals2 and hand1 > hand2):
                n_wins += 1
                continue
        ranks.append(n_wins)
    
    return sum(bids[i] * ranks[i] for i in range(len(hands)))


if __name__ == '__main__':
    with open('input.txt') as file:
        lines = [line.strip().split(' ') for line in file]

    faces = {'TJQKA'[i]: i + 10 for i in range(5)}
    numbers = {str(i): i for i in range(2, 10)}
    cardmap = faces | numbers

    hands = [[cardmap[card] for card in line[0]] for line in lines]
    bids = [int(line[1]) for line in lines]

    print(camel(hands, bids))

    cardmap['J'] = 1
    hands = [[cardmap[card] for card in line[0]] for line in lines]

    print(camel(hands, bids))