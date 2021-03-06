from tabulate import tabulate

# Inclusive Range
def irange(start, end):
    return [*range(start,end), end]

def get_odds(rolltable, bars=False):
    full_list = [item for sublist in rolltable for item in sublist]
    odds_list = []

    rows = [["range", "odds"]]
    if bars:
        rows[0].append("bars")

    i = 0
    for sublist in rolltable:
        odds = (len(sublist) / len(full_list)) * 100
        odds_list.append(odds)
        if bars:
            bar = "*" * int(odds)
            rows.append([sublist, odds, bar])
        else:
            rows.append([sublist, odds])
        i += 1
    return rows
    print(tabulate(rows, headers="firstrow", numalign="right"))

rolltable = [
    [1],
    irange(2,3),
    irange(4,10),
    irange(11,17),
    irange(18,19),
    [20]
]

print(tabulate(get_odds(rolltable, bars=True), headers="firstrow", numalign="right"))
