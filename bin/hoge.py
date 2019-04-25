import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import library


def hoge():
    library.echo('hoge')


if __name__ == '__main__':
    hoge()
