import sys
import yaml

def parse_args():
    entries = sys.argv[1:]
    query_dict = {}
    for entry in entries:
        # Split only on the first '='
        key, value = entry.split('=', 1)
        # Remove the leading '--' from the key
        key = key[2:]
        query_dict[key] = None if len(value) == 0 else value
    return query_dict

def get_arg(key, default=None):
    return parse_args().get(key, default)

def get_tokens():
    with open('tokens.yaml') as f:
        return yaml.safe_load(f)