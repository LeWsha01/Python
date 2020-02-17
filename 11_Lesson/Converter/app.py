#!/usr/bin/env python3

from converter.data import menu
from converter import __version__


if __name__ == '__main__':
    print(f'Version: {__version__}')
    print(__name__)
    menu.menu()