# Homework 3-4: Coding style and Unit tests.

##### Grade: 12/14    
-1: In Python, function names by convention use underscores ('_') to separate words, not camelCase.   
-1: In dataframe.py: you don't need to have a 'pass' that is at the same indentation level right before a return statement. (It might not make a huge difference now, but doing this clusters your code and will likely reduce maintainability in the future.)     

-0: In dataframe.py line #60 - this 'return False' is redundant (you could've let the code fall through to the final return).

-----

## Please note that VS Code runs Lint automatically, no output if everything is correct

**Note: This homework has a total of 14 points.**

In this homework, you will create two python modules and put them in PEP8 style.

1. Function code (5 points). Last week you wrote python codes that read an online file and created a data frame that has at least 3 columns. Now: (a) create a python module ``dataframe.py`` that reads the data in homework 2;  and (b) ``dataframpe.py`` should generate an ValueError execption if the dataframe doesn't have the expected column names.

1. Test code (5 points). Create a python file ``test_dataframe.py`` that has unit tests for dataframe.py. Include at least 2 of the following tests:

   - You have the expected columns.
   - Values in the column are all of the expected type.
   - There are no nan values.
   - The dataframe has at least one row.
   
1. Coding style (4 points). Make all codes PEP8 compliant and provide the output from pylint to demonstrate that you have accomplished this.
