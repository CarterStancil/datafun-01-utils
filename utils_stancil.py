''' ITERATION 4

Module: Stancil Solutions - Reusable Module for My Data Analytics Projects

This module provides a simple, reusable foundation for my analytics projects. 
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do.

Process:

We don't write code from top to bottom; instead, we often write it from the outside in.
Here's what a first draft of my utils_case.py might look like:

1. I start with this docstring at the very beginning.
   I use it to clarify the purpose of my Python file and organize my thoughts.
   
2. I'll declare a global variable for my byline string and just set it to some simple text.

3. I'll declare a main() function for my module. When I run this script, I can use main() to test my byline.

4. I'll add the boilerplate conditional execution code so I only run the main() function when 
   this script is executed directly (but not when I import it into another file).

I'll test it in an online interpreter to ensure this version runs correctly before continuing.
'''

#####################################
# Declare a global variable named byline.
#####################################

byline: str = 'Stancil Solutions: The Absolute Best'

#####################################
# Define a main() function for this module.
#####################################

# Create a function named main.
# A function is a block of code that performs a specific task.
# This function will simply print the byline to the console.
# Add a type hint to indicate that this function doesn't return anything when called 
# (that is, it has a Python type of None).
# It doesn't need any additional information passed in, 
# so there's nothing needed inside the parentheses.
# Everything afer the colon (:) must be indented (usually 4 spaces)

# Online Python - IDE, Editor, Compiler, Interpreter

#####################################
# Declare a global variable named byline.
#####################################

byline: str = 'Stancil Solutions: The Absolute Best'

#####################################
# Define a main() function for this module.
#####################################

# Create a function named main.
# A function is a block of code that performs a specific task.
# This function will simply print the byline to the console.
# Add a type hint to indicate that this function doesn't return anything when called 
# (that is, it has a Python type of None).
# It doesn't need any additional information passed in, 
# so there's nothing needed inside the parentheses.
# Everything afer the colon (:) must be indented (usually 4 spaces)

import statistics

#Declare Global Variables 

#Boolean variable for hybrid workplace
has_hybrid_workplace: bool = True

#Int variable for years in operation
years_in_operation: int = 9

#String List for employee characteristics
employee_characteristics: list = ["Timely", "Personable", "Respectful"]

#Float list for customer satisfaction scores
customer_satisfaction_scores: list = [9.8, 7.8, 8.4, 10, 9.1]

#Calculate basic stats using built in functions min(), max() and statistics modules functions mean() and stdev()
min_score: float = min(customer_satisfaction_scores)
max_score: float = max(customer_satisfaction_scores)
mean_score: float = statistics.mean(customer_satisfaction_scores)
stdev_score: float: = statistics.stdev(customer_satisfaction_scores)


byline: str = f"""
-------------------------------------
Stancil Solutions: The Absolute Best
-------------------------------------
Has Hybrid Workplace: {has_hybrid_workplace}
Years in Operation: {years_in_operation}
Employee Characteristics: {employee_characteristics}
Customer Satisfaction Scores: {customer_satisfaction_scores}
"""


#####################################
# Define the get_byline() Function
#####################################

def get_byline() -> str:
    '''Return a byline for my analytics projects.'''
    return byline

#####################################
# Define a main() function for this module.
#####################################

# The function now calls get_byline() to retrieve the byline.

def main() -> None:
    '''Print the byline to the console when this function is called.'''
    print(get_byline())

#####################################
# Conditional Execution - Only call main() when executing this module as a script.
#####################################

if __name__ == '__main__':
    main()
