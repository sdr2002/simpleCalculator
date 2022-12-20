import math
import logging

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                    level=logging.DEBUG,
                    datefmt='%Y-%m-%d %H:%M:%S')
LOGGER = logging.getLogger()

SPECIAL_VAL = {
    'π': math.pi,
}

MNVAR_OPS_DICT = {
    'sq': lambda x: math.pow(x,2),
    'rt': lambda x: math.pow(x,0.5),
    'pn': lambda x: -1.0*x,
    'r2': lambda x: round(x,2),
    'r0': lambda x: round(x,0),
}

BIVAR_OPS_DICT = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
}

MO_keys = list(MNVAR_OPS_DICT.keys())
BO_keys = list(BIVAR_OPS_DICT.keys())

OP_keys = MO_keys + BO_keys


def run_calculator():
    """Implementation of simple calculator
    https://www.calculatorsoup.com/calculators/math/basic.php

    User types the input followed by enter key

    Exit: q
    Number: digits &  . & +|- & π
    Op_basic: + & - & x & /
    """
    LOGGER.info("Calculator operational")

    mem_num = None
    mem_op = None

    to_terminate = False
    while not (to_terminate):
        res = None
        print("Enter input and press enter: ")
        inst = input()
        try:
            inst = float(inst)
        except ValueError:
            pass

        if inst == 'q':
            to_terminate = True
            print("Exiting calculator...")
            continue
        elif isinstance(inst, (int, float)):
            if not(mem_op is None):
                # 1 + 2
                res = BIVAR_OPS_DICT[mem_op](mem_num, inst)
                mem_num = res
                print(res)
            else:
                # 1, + 1, 1 2
                mem_num = inst
                res = inst
                print(res)
            mem_op = None
        elif inst in OP_keys:
            if inst in MO_keys:
                if mem_num is None:
                    print("You need to specify a number first.")
                else:
                    res = MNVAR_OPS_DICT[inst](mem_num)
                    mem_num = res
                    print(res)
                mem_op = None
            else:
                #inst in BO_keys
                if not(mem_num is None):
                    mem_op = inst
        else:
            print(f"Invalid input({inst}), while mem_num({mem_num}) & mem_op({mem_op})")

    return to_terminate


def main():
    LOGGER.info('Local main')

    stop = False
    while not (stop):
        try:
            stop = run_calculator()
        except KeyboardInterrupt:
            LOGGER.info("Keyboard termination called.")
            stop = True
        except Exception as e:
            LOGGER.error(f"Error occurred: {e}")
            LOGGER.error("Calculator terminates.")
            stop = True


if __name__ == "__main__":
    main()
