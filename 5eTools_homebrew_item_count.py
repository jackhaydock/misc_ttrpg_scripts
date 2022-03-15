import urllib.request, json

link = "https://raw.githubusercontent.com/jackhaydock/Jackalope_Homebrew/master/Jackalope.json"

with urllib.request.urlopen(link) as url:
    data = json.load(url)
    total = 0
    for key in data.keys():
        if key == "_meta":
            print("_meta: N/A")
        elif key == "race":
            both_races = 0
            base_races = 0
            subraces = 0
            for race in data[key]:
                base_races += 1
                if "subraces" in race.keys():
                    subraces += len(race["subraces"])
            both_races = base_races + subraces
            print("{}: {} ({} base, {} sub)".format(key, both_races, base_races, subraces))
            total += both_races
        else:
            print("{}: {}".format(key, len(data[key])))
            total += len(data[key])
    print("Total: {}".format(total))
