from tabulate import tabulate

def fill_rows(die_range, die_name):
    rows = [
        [die_name],
        ["base"],
        ["reroll better"],
        ["reroll same or better"],
        ["reroll same or worse"],
        ["reoll worse"]
    ]
    for i in die_range:
        # Skip multi-occurances
        if i in rows[0]:
            continue

        # Count multi-occurances
        count = die_range.count(i)

        # Odds of base roll
        odds = (count/len(die_range)) * 100

        # Odds of better reroll
        better_range = [a for a in die_range if a > i]
        better = (len(better_range)/len(die_range)) * 100
        better_or_same = better + odds

        # Odds of worse reoll
        worse_range = [b for b in die_range if b < i]
        worse = (len(worse_range)/len(die_range)) * 100
        worse_or_same = worse + odds

        # Add odds to table
        rows[0].append(round(i,2))
        rows[1].append(round(odds,2))
        rows[2].append(round(better,2))
        rows[3].append(round(better_or_same,2))
        rows[4].append(round(worse_or_same,2))
        rows[5].append(round(worse,2))
    return rows

def roll_odds(dice):
    for d in dice:
        if type(d) is int:
            rows = fill_rows(range(1,d+1), "d{}".format(d))
        else:
            rows = fill_rows(d[1], d[0])
        print()
        print(tabulate(rows, headers="firstrow", numalign="right"))

# Major dice
roll_odds([4,6,8,12,20])
# Wierd dice test
roll_odds([
    (
        "Oria's cold d6",
        [2,2,3,4,5,6]
    ),
    (
        "Lamonix's Reliable Special",
        [10,10,10,10,10,10,10,10,10,10,11,12,13,14,15,16,17,18,19,20]
    )
])
