from os import listdir
from os.path import isfile, join, splitext
from io import StringIO
import automata

testFolder = "./tests"
rules = "./rules.txt"

tests = [splitext(file)[0]
	for file in listdir(testFolder) 
	if isfile(join(testFolder, file)) and splitext(file)[1] == ".in"]

print("Testing on following files: ", tests)

for file in tests:
	atmt = automata.CellularAutomata()

	with  open(rules, 'r') as ruleset,\
		open(join(testFolder, file + ".in"), 'r') as input,\
			open(join(testFolder, file + ".out"), 'r') as expected,\
				StringIO() as output:
		steps = int(input.readline())

		atmt.ReadRules(ruleset)
		atmt.ReadState(input)
		atmt.FastForward(steps)
		atmt.WriteState(output)

		expectedString = expected.read().strip()
		outputString = output.getvalue().strip()

		if expectedString != outputString:
			print("Test file \"", file, "\" failed.")
			print("Test expected:")
			print(expectedString)
			print("But resulted in:")
			print(outputString)





