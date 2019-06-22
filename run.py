from linearSystems.examples.example1 import serify
from linearSystems.examples.example_2 import parallelize

import sys


def run_model():
    """
        Runs the function soecifed as argument vector
    """
    cmds = {'parallelize': parallelize, 'serify': serify}
    opts = 'Options: parallelize, serify'

    try:
        input_arg = sys.argv[1]
    except IndexError:
        print('Specify a command')
        print(opts)
    else:
        if input_arg not in cmds.keys():
            print('Specify a valid command')
            print(opts)
            return
        cmds.get(input_arg)()


if __name__ == '__main__':
    run_model()
