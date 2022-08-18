# Reliability_concrete
## Description
The codes are applicable to find the probability of failure for Alkali Activated Concrete (AAC) and Portland Cement (PC) Concrete. For each type of concrete, there are three codes avaliable that represent the three loading cases: compression, splitting tension and flexure.

## Installation
PyRe (Python Reliability) needs to be installed prior to running these codes. 
For more information on this visit - http://github.com/hackl/pyre

## Input parameters
"p_fac" is an array  consisting of the various load factors used.

"limitstatefunction" is developed for each case as [(Resistance of the specimen)-(Load imposed on the specimen)]
 There are four limit state functions in each file for the four load factors taken into consideration.
 
 "X1" is the value of compressive strength for the specific mix under consideration.
 
 "X2" is the peak load that the speciemen could resist in the respective loading case.

## Output
On running the code, four set of outputs are drawn corresponding to the four limit state functions defined for each load factor.

