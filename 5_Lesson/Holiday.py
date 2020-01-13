#!/usr/bin/python3

from sys import getdefaultencoding
import argparse
import os


def argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('dir', type=str, help='Path directory')
    parser.add_argument('text', type=str, help='Enter the text you want to find')
    return parser.parse_args()


def find_text(files, text):
    count = 0
    for file in files:
        with open(file, 'rb') as myFile:
            print('Open this file -> {}'.format(file))
            for num, line in enumerate(myFile, 1):
                if text in str(line) and count <= 99:
                    count += 1
                    print('Found at line: {} -> {}'.format(num, line))
                elif count > 99:
                    break
    print('Count = {}'.format(count))


def walk_dir(directory):
    file_names = []
    for root, sub_dirs, files in os.walk(directory):
        for file in files:
            file_names.append(os.path.join(root, file))
    return file_names


def look_up(direct, text):
    files = walk_dir(direct)
    find_text(files, text)


args = argument_parser()
look_up(args.dir, args.text)
