# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 05:28:37 2024

@author: edwar
"""

# Simple LP PROBLEM

# Diet problem - determine the cheapest combination of food that will satisfy all nutrition needs

# 3 food items (Food1, Food2, Food3)
# 2 Nutrients (Protein, Carbs)

# Define the probelem
    # List the costs of each food items
        #Food1: 2$/Unit
        #Food2: 3$/Unit
        #Food3: 1$/Unit
    
    #List the amount of each nutrient provided by each food
        #Protein(g) - Food1: 3g, Food2: 2g, Food3: 1g
        #Carbs(g) - Food1: 2g, Food2: 2g, Food3: 3g
        
    #List the minimum required amount of each nutrient
        #Atleast 10g of Protein
        #Atleast 12g of Carbs
        
# Set up the LP Problem
    # Objective funtion [Minimize the cost]
    # Define the constraints [Nutritional requirements]
    

# Import pulp library
    
from pulp import LpProblem, LpVariable, lpSum, LpMinimize, value, LpStatus

# Define the LP problem

problem = LpProblem('Diet_problem', LpMinimize)


# Define the decision variables

food1 = LpVariable('Food1', lowBound=0, cat='Continuous')

food2 = LpVariable('Food2', lowBound=0, cat='Continuous')

food3 = LpVariable('Food3', lowBound=0, cat='Continuous')


# Objective function: Minimize cost

cost = 2 * food1 + 3 * food2 + 1 * food3

problem += cost, 'Total Cost'


# Constraints

problem += 3 * food1 + 2 * food2 + 1 * food3 >= 10, 'proteinRequirement'

problem += 2 * food1 + 2 * food2 + 3 * food3 >= 12, 'CarbsRequirement'

# Solve the Problem

problem.solve()

print('status:', LpStatus[problem.status])
print('Optimal Solution to the problem:')
print('Food1:', value(food1))
print('Food2:', value(food2))
print('Food3:', value(food3))
print('Total Cost:', value(problem.objective))

