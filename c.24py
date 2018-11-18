# Generate a list of all combinations 
def allNumCombinations(num):
    for i in range(1, num+1):
	    for j in range(1, num+1):
		    for k in range(1, num+1):
			    for l in range(1, num+1):
				    yield [i, j, k, l]

# Generate all possible arithmetic operator locations
def allOpsCombinations(oplists):
    for op1 in oplists:
	    for op2 in oplists:
		    for op3 in oplists:
			    yield [op1, op2, op3]

# Compare two lists for exact content
def isSameList(l1, l2):
    if len(l1) != len(l2):
        return False
    else:
        for i in range(0, len(l1)):
            if l1[i] != l2[i]:
                return False
    return True

totalComboCnt = 0
totalExprCs = 0
comboCounts = {} # store the number combinations that can lead to the result
resultCounts = {}  # store the number of expressions that lead to the result				
for clisting in allNumCombinations(13):
    totalComboCnt += 1
    possibleResults = []  # Store the list of result that can come up with by this combination
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
        totalExprCs += len(exprlisting)
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
            if abs(result - result_rounded) < 0.00001:
                if result_rounded_str not in resultCounts:
                    resultCounts[result_rounded_str] = []
                resultCounts[result_rounded_str].append(expr)
                if result_rounded not in possibleResults:
                    possibleResults.append(result_rounded)
                ####if result_rounded == -2:
                ####    print(expr)
    for r in possibleResults:
        result_str = str(r)
        if result_str not in comboCounts:
            comboCounts[result_str] = []
        comboCounts[result_str].append(clisting)
        
print("Total number combinations: " + str(totalComboCnt))  
for key in comboCounts.keys():
    print("Result: " + str(key) + ' ' + "Number combination: " + str(len(comboCounts[key])))
                  
#print("Total expression combinations: " + str(totalExprCs))
#for key in resultCounts.keys():
#    print("Result: " + str(key) + ' ' + "Combinations: " + str(len(resultCounts[key])))
    