import json, sys, requests
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-f", "--file", dest="filename",
                    help="file to read", metavar="FILE")
parser.add_argument("-u", "--drive", dest="drive_id", default=False,
                    help="ID of drive file")
parser.add_argument("-a", "--actor", dest="actor",
                    help="part of actor name to search for")
parser.add_argument("-d", "--detail", dest="detail",
                    help="detail to search for", default=False)
parser.add_argument("-p", "--pretty", action="store_true",
                    dest="pretty_print", default=False,
                    help="pretty print output")
args = parser.parse_args()

#------------------------------------------------------------------------------#

def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

def get_actors_from_url(url, actor_name):
    actors = []
    lines = urllib.request.urlopen(url)

    for line in lines:
        data = json.loads(line)
        if actor_name.lower() in data["name"].lower():
            actors.append(data)

    return actors

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

def print_entire_actor(actors):
    for actor in actors:
        if args.pretty_print:
            print(json.dumps(actor, indent=4))
        else:
            print(actor)

def print_detail(actors, detail):
    for actor in actors:
        output = get_detail_by_key(actor, args.detail)
        try:
            print(actor["name"])
        except UnicodeEncodeError:
            print(actor["name"].encode(encoding="ascii",errors="replace"))

        if args.pretty_print:
            print(json.dumps(output, indent=4))
        else:
            print(output)

#------------------------------------------------------------------------------#
if __name__ == "__main__":
    if args.drive_id:
        download_file_from_google_drive(args.drive_id, args.filename)

    actors = get_actors_by_name(args.filename, args.actor)

    if args.detail:
        print_detail(actors, args.detail)
    else:
        print_entire_actor(actors)
