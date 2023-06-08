#!/usr/bin/python3
if __name__ == "__main__":
	import hidden_4
	bunchOfNames = dir(hidden_4)
	for aName in bunchOfNames:
		if aName.startswith("__"):
			continue
		print(aName)
