

import os
import sys


BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)

from src.script import client
if __name__ == '__main__':
    client()
