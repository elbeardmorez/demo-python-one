from itertools import groupby
import re
import sys
import os

debug = 0
data_prices = "data.prices.txt"

def isdirty(s):
    return True if re.search("[^A-Z]", s) else False


#TODO run once only per test run!
def build_state():
    def build_prices():
        prices = {}
        path = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(path, "data", data_prices), 'r') as fo:
            for line in fo:
                tks = line.rstrip('\n').split(':')
                if debug > 1:
                    print("adding product %r at price %s" % (tks[0], tks[1]))
                prices[tks[0]] = int(tks[1])
        return prices
    return (build_prices())  # state tuple of prices, ...


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    if debug:
        print("considering skus %r" % skus)

    if isdirty(skus):
        return -1

    # build supermarket pricing / offers state
    (costs) = build_state()

    # TODO: external flat file with simple format for update!
    freebies = {
        'E': [(2, 80, 'B')],
        'N': [(3, 120, 'M')],
        'R': [(3, 150, 'Q')]
    }
    # TODO: external flat file with simple format for update!
    offers = {
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)],
        'F': [(3, 20)],
        'H': [(10, 80), (5, 45)],
        'K': [(2, 120)],
        'P': [(5, 200)],
        'Q': [(3, 80)],
        'U': [(4, 120)],
        'V': [(3, 130), (2, 90)]
    }
    # these items are not part of other offers.. [thank you!]
    group_offers = {
        'S': [(3, 45, ['S', 'T', 'X', 'Y' , 'Z' ])],
        'T': [(3, 45, ['S', 'T', 'X', 'Y' , 'Z' ])],
        'X': [(3, 45, ['S', 'T', 'X', 'Y' , 'Z' ])],
        'Y': [(3, 45, ['S', 'T', 'X', 'Y' , 'Z' ])],
        'Z': [(3, 45, ['S', 'T', 'X', 'Y' , 'Z' ])]
    }

    a_skus = sorted(list(skus))

    # group and count
    counts = {}
    for k, g in groupby(a_skus):  # identity lambda as def
        counts[k] = len(list(g))

    # total
    val = 0

    # consider freebie offers
    for k, count in counts.items():
        if debug:
            print("considering %r, count %d" % (k, count))
        if k in freebies:
            for quantity, cost, free in freebies[k]:
                if debug:
                    print("considering freebie offer on %r, %d for %d"
                          % (k, quantity, cost))
                while count >= quantity:
                    if debug:
                        print("offer requirements met, %d for %d on %r"
                              % (quantity, cost, k))
                    val += cost
                    count -= quantity
                    counts[k] -= quantity  # outer context
                    free_items = list(free)
                    if len(free_items) > 0:
                        # reduce count(s) for given items
                        for p in free_items:
                            if p in counts:
                                counts[p] -= 1

    # consider value offers
    for k, count in counts.items():
        if debug:
            print("considering %r, count %d" % (k, count))
        if k in offers:
            # hmm, possible multiple offers.. order matters
            # TODO don't rely on order matters! sort by best deal value
            for quantity, cost in offers[k]:
                if debug:
                    print("considering offer on %r, %d for %d"
                          % (k, quantity, cost))
                while count >= quantity:
                    if debug:
                        print("offer requirements met, %d for %d on %r"
                              % (quantity, cost, k))
                    val += cost
                    count -= quantity
                    counts[k] -= quantity  # outer context

    # group offers
    costs_ordered = sorted(costs.items(), key=lambda kvp: kvp[1]);

    def order_by_price(items):
        return [k for (k, v) in costs_ordered if k in items]

    for k, count in counts.items():
        if k in group_offers:
            for min_p, cost, p_set in group_offers[k]:
                # sort set by price descending to ensure most expensive set
                # is applied first
                p_set_ordered = order_by_price(p_set)[::-1]

                gi_purchased_count = 0
                gi_purchased = []
                applied = False
                for i in p_set_ordered:
                    if debug:
                        print("consider %r for group offer" % i)
                    if not i in counts:
                        continue
                    count_item = counts[i]
                    while count_item > 0:
                        # drain most expensive first
                        if debug:
                            print("adding %r for group offer" % i)
                        gi_purchased_count += 1
                        gi_purchased.append(i)
                        count_item -= 1
                        if gi_purchased_count == min_p:
                            if debug:
                                print("applying group offer for %r"
                                      % gi_purchased)
                            for i in gi_purchased:
                                counts[i] -= 1
                            val += cost
                            # reset
                            gi_purchased_count = 0
                            gi_purchased = []

    # single item costs only remain
    for k, count in counts.items():
        val += (count * costs[k])

    if debug:
        print("returning %r for %r" % (val, skus))
    return val


if __name__ == '__main__':
    if (len(sys.argv) > 1):
        checkout(sys.argv[1])
