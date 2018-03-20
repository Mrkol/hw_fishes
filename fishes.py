import automata
import argparse
import sys


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-i", "--input", type=str,
        help="The file to read the field from."
        + " Stdin is used by default.",
        default=0)

    parser.add_argument(
        "-o", "--output", type=str,
        help="The file to write the resulting state to."
        + " Stdout is used by default.",
        default=1)

    parser.add_argument(
        "-r", "--rules", type=str,
        help="The file to load a ruleset from. Default is rules.txt.",
        default="rules.txt")

    parser.add_argument(
        "-s", "--steps", type=int,
        help="Amount of steps to advance the field by. Default is 1.",
        default=1)

    args = parser.parse_args()

    with open(args.input, 'r') as file_in,\
            open(args.output, 'w') as file_out,\
            open(args.rules, 'r') as file_rules:
        atmta = automata.CellularAutomata()

        atmta.read_rules(file_rules)
        atmta.read_state(file_in)
        atmta.fast_forward(args.steps)
        atmta.write_state(file_out)


if __name__ == '__main__':
    main()
