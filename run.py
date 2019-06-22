from linearSystems.examples import example1, example_2, example_3, example_4

import sys


def run_model():
    """
        Runs the function soecifed as argument vector
    """
    cmds = {
        'example2': example_2,
        'example1': example1,
        'example3': example_3,
        'example4': example_4
    }
    opts = f'Options: {list(cmds.keys())}'

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
