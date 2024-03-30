import argparse

def get_parse_args():
    parser = argparse.ArgumentParser(description="Plot average temperatures.")
    parser.add_argument('mode', choices=['0', '1'], help="Mode of operation: 0 for display, 1 for save to file")
    return parser.parse_args()
