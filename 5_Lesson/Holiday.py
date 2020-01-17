#!/usr/bin/python

import argparse
import os


def argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', help='Path for files')
    parser.add_argument('text', type=str, help='Find text')
    return parser.parse_args()


def find_text(file, text):
    count = 0
    for fil in file:
        if os.path.isfile(fil):
            with open(fil, 'rb') as myFile:
                print('Open this file -> {}'.format(fil))
                for num, line in enumerate(myFile, 1):
                    if text in str(line) and count <= 99:
                        count += 1
                        print('Found at line: {} -> {}'.format(num, line))
                        print('Number in count -> {}'.format(count))
                    elif count > 99:
                        break
        else:
            continue


def get_files(directory, texts):
    if directory is None:
        directory = os.getcwd()
    files = os.listdir(directory)
    print(files)
    find_text(files, texts)


args = argument_parser()
get_files(args.path, args.text)
