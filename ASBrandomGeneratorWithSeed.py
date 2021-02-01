import numpy as np
import math

def ASBrandomGeneratorWithSeed (seed,limit):
	seed = seed + 458							# operations for a random generated number between 0 and "limit" 
	x1 = (seed**2)+(2*seed)+1997							
	x2 = x1 + int(math.log(seed, 2))
	x3 = x2 + int(math.log(x2, 5))
	x4 = x3 + (seed**2) 
	x5 = int(math.log(x4 ,10))
	x6 = (x4**2) + x5
	x7 = x6 + int(math.log(seed ,10))
	res = int(x7) % limit
	return res;															


seed = int(input("Integer seed value:"));
limit = int(input("Integer limit value"));

result = ASBrandomGeneratorWithSeed(seed,limit);

print("Result: ", result);