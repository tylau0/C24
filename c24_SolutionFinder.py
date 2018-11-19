import itertools
# Generate all possible arithmetic operator locations
def allOpsCombinations(oplists):
    for op1 in oplists:
	    for op2 in oplists:
		    for op3 in oplists:
			    yield [op1, op2, op3]
    
plisting = [7, 3, 7, 3]
for clisting in itertools.permutations(plisting):
    for olisting in allOpsCombinations(['+', '-', '*', '/']):
        exprlisting = []
        # No bracket
        exprlisting.append(str(clisting[0]) + olisting[0] + str(clisting[1]) + olisting[1] + str(clisting[2]) + olisting[2] + str(clisting[3]))
        # 1 bracket
        ## embrace 3
        exprlisting.append('(' + str(clisting[0]) + olisting[0] + str(clisting[1]) + olisting[1] + str(clisting[2]) + ')' + olisting[2] + str(clisting[3]))
        exprlisting.append(str(clisting[0]) + olisting[0] + '(' + str(clisting[1]) + olisting[1] + str(clisting[2]) + olisting[2] + str(clisting[3]) + ')')
        ## embrace 2
        exprlisting.append('(' + str(clisting[0]) + olisting[0] + str(clisting[1]) + ')' + olisting[1] + str(clisting[2]) + olisting[2] + str(clisting[3]))
        exprlisting.append(str(clisting[0]) + olisting[0] + '(' + str(clisting[1]) + olisting[1] + str(clisting[2]) + ')' + olisting[2] + str(clisting[3]))
        exprlisting.append(str(clisting[0]) + olisting[0] + str(clisting[1]) + olisting[1] + '(' + str(clisting[2]) + olisting[2] + str(clisting[3]) + ')')
        # 2 brackets
        exprlisting.append('(' + str(clisting[0]) + olisting[0] + str(clisting[1]) + ')' + olisting[1] + '(' + str(clisting[2]) + olisting[2] + str(clisting[3]) + ')')
        for expr in exprlisting:
            ####print(expr)
            try: 
                result = eval(expr)
            except ZeroDivisionError:
                continue
            ####print(expr + '=' + str(result))
            result_rounded = round(result)
            result_rounded_str = str(result_rounded)
            # skip those that don't evaluate to integers
            if abs(result - result_rounded) < 0.0000000001 and result_rounded == 24:
                print(expr)
                