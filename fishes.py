import automata
import argparse
import sys

parser = argparse.ArgumentParser()


parser.add_argument("-f", "--file", type = str,
    help = "The file to read the field from. Stdin is used by default.")

parser.add_argument("-o", "--output", type = str,
    help = "The file to write the resulting state to. Stdout is used by default.")

parser.add_argument("-r", "--rules", type = str,
    help = "The file to load a ruleset from. Default is rules.txt.")

parser.add_argument("-s", "--steps", type = int,
    help = "Amount of steps to advance the field by. Default is 1.")

args = parser.parse_args()

input = sys.stdin

if args.file:
    input = open(args.file, 'r')

output = sys.stdout

if args.output:
    output = open(args.output, 'w')

rules = open("rules.txt", 'r')

if args.rules:
	rules.close()
	rules = open(args.rules, 'r')

steps = 1

if args.steps:
	steps = args.steps


automata = automata.CellularAutomata()

automata.ReadRules(rules)
automata.ReadState(input)
automata.FastForward(steps)
automata.WriteState(output)

if args.file:
	input.close()

if args.output:
	output.close()

if args.rules:
	rules.close()
