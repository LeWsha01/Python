#!/usr/bin/python3

import argparse
import os


def argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('dir', type=str, help='Path directory')
    parser.add_argument('text', type=str, help='Enter the text you want to find')
    return parser.parse_args()


def find_text(file, text):
    with open(file, 'rb') as myFile:
        print('In this file -> {}, search text -> {}'.format(file, text))
        for num, line in enumerate(str(myFile), 1):
            if text in str(line):
                print('Found at line: {} -> {}'.format(num, line))
            # else:
            #     print('False')


def walk_dir(directory):
    file_names = []
    for root, sub_dirs, files in os.walk(directory):
        for file in files:
            file_names.append(os.path.join(root, file))
    return file_names


def look_up(direct, text):
    files = walk_dir(direct)
    result = []
    for file in files:
        result = find_text(file, text)
    print(result)


args = argument_parser()
look_up(args.dir, args.text)

