# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 05:44:46 2024

@author: edwar
"""

# Maximise profit from producing diffrent products

# Products

    # 3 products(Product1, Product2, Product3)
    # 2 Resources (Resourse1, Resource2)
    
# Data

    # product1 :$5/unit
    # product2 :$4/unit
    # product3 :$3/unit
    
# Resourse consumption per unit

    # Resource1 :Product1: 2, Product2: 3, Product3: 1
    # Resource2 :Product1: 1, Product2: 2, product3: 3
    
# Resourse availability

    # Resource1: 100 units
    # Resource2: 80 units
    
from pulp import LpProblem, LpVariable, lpSum, LpMaximize, value, LpStatus

"""
profits: List of profits for each product.
resource_consumption: 2D list where each row represents the consumption of resources by each product.
resource_availability: List of total available units for each resource.

"""

def max_profit(profits, resource_consumption, resource_availability):
    
    # number of products
    
    num_products = len(profits)
    
    # Define the lp problem
    
    problem = LpProblem('Resource_Allocation_Problem', LpMaximize)
    
    # Define decision variables
     
    quantities = [
        LpVariable(f'Product{i+1}', lowBound=0, cat= 'Continuous') for i in range(num_products)
        ]
    
    # Objective function : Max profits
    
    profit = lpSum(profits[i] * quantities[i] for i in range(num_products))
    problem += profit, 'Total Profit'
    
    # Constraints
    
    for j in range(len(resource_availability)):
        problem += lpSum(resource_consumption[j][i] * quantities[i] for i in range(num_products)) <= resource_availability[j], f'Resource{j+1}_Constraint'
        
    # solve the problem
    
    problem.solve()
    
    # print the results
    
    status = LpStatus[problem.status]
    optimal_quantities = [value(q) for q in quantities]
    total_profit = value(problem.objective)
    
    return status, optimal_quantities, total_profit







