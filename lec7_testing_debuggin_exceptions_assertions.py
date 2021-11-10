###########################
### DEFENSIVE PROGRAMMING
### - Write specifications for functions
### - Modulirize programs
### - Check conditions on inputs/outputs (assertions)
###
### TESTING/VALIDATION
### - Compare input/output pairs to specification
### - It's not working
### - How can I break my program?
###
### DEBUGGING
### - Study events leading up to an error
### - Why is not working?
### - How can I fix my program?
###
### CLASSES OF TESTS
### 
### UNIT TESTING
### - Validate each piece of program
### - Testing each function separately
### 
### REGRESSION TESTING
### - Add test for bugs as you find them
### - Catch reintroduced errors that were previously fixed
###
### INTEGRATION TESTING
### - Does overall program work?
### - Tend to rush to do this
###
### TESTINGS APPROACHES
### 
### Intuition about natural boundaries to the problem, if no natural partitions come up, might do random testing
###
### Black box testing: explore paths through specification
###
### Glass box testing: explore paths through code
###
### BLACK BOX TESTING
### - Design without looking at the code, can be done by someone other than the implementer to avoid some implementer biases
### - Testing can be reused if implementation changes
### - Paths through specification
### - Build test cases in different natural space partitions
### - consider boundary conditions
###
### GLASS BOX TESTING
### - Use code directly to guide design of test cases
### - Called path-complete if every potential path through code is tested at least once
### - DRAWBACKS: Can go throught loops arbitrarily many times, missing paths
###
### DEBUGGING STEPS
### - Study program code
### - don't ask what is wrong
### - ask how did i get the unexpected result
### - is it part of a family?
###
### Scientific method
### - Study available data
### - form hypothesis
### - repeatable experiments
### - pick simplest input to test with