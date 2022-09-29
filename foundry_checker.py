import json, sys
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-f", "--file", dest="filename",
                    help="file to read", metavar="FILE")
parser.add_argument("-a", "--actor", dest="actor",
                    help="actor to check")
parser.add_argument("-d", "--detail", dest="detail",
                    help="detail to check")
parser.add_argument("-p", "--pretty", action="store_true",
                    dest="pretty_print", default=False,
                    help="pretty print output")
args = parser.parse_args()

def get_actors_by_name(file_name, actor_name):
    actors = []

    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        for line in lines:
            data = json.loads(line)
            if actor_name.lower() in data["name"].lower():
                actors.append(data)

    return actors

def get_detail_by_key(actor, detail_name):
    if detail_name in actor["data"].keys():
        return actor["data"][detail_name]
    else:
        print(f"{detail_name} not found, see possible keys below.")
        print(actor["data"].keys())
        sys.exit()

actors = get_actors_by_name(args.filename, args.actor)
for actor in actors:
    output =get_detail_by_key(actor, args.detail)
    try:
        print(actor["name"])
    except UnicodeEncodeError:
        print(actor["name"].encode(encoding="ascii",errors="replace"))

    if args.pretty_print:
        print(json.dumps(output, indent=4))
    else:
        print(output)
