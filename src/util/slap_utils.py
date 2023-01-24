import sys

def parse_args():
    entries = sys.argv[1:]
    query_dict = {}
    for entry in entries:
        key, value = entry.split('=')
        # Remove the leading '--' from the key
        key = key[2:]
        query_dict[key] = None if len(value) == 0 else value
    return query_dict

def get_arg(key, default=None):
    return parse_args().get(key, default)