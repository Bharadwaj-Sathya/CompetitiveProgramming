# 1873. Calculate Special Bonus

# Table: Employees

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | employee_id | int     |
# | name        | varchar |
# | salary      | int     |
# +-------------+---------+
# employee_id is the primary key (column with unique values) for this table.
# Each row of this table indicates the employee ID, employee name, and salary.
 

# Write a solution to calculate the bonus of each employee. The bonus of an employee is 100% of their salary if the ID of the employee is an odd number and the employee's name does not start with the character 'M'. The bonus of an employee is 0 otherwise.

# Return the result table ordered by employee_id.

# The result format is in the following example.

 

# Example 1:

# Input: 
# Employees table:
# +-------------+---------+--------+
# | employee_id | name    | salary |
# +-------------+---------+--------+
# | 2           | Meir    | 3000   |
# | 3           | Michael | 3800   |
# | 7           | Addilyn | 7400   |
# | 8           | Juan    | 6100   |
# | 9           | Kannon  | 7700   |
# +-------------+---------+--------+
# Output: 
# +-------------+-------+
# | employee_id | bonus |
# +-------------+-------+
# | 2           | 0     |
# | 3           | 0     |
# | 7           | 7400  |
# | 8           | 0     |
# | 9           | 7700  |
# +-------------+-------+
# Explanation: 
# The employees with IDs 2 and 8 get 0 bonus because they have an even employee_id.
# The employee with ID 3 gets 0 bonus because their name starts with 'M'.
# The rest of the employees get a 100% bonus.

import pandas as pd


def calculate_bonus(row):
    if row['employee_id'] % 2 == 1 and not row['name'].startswith('M'):
        return row['salary']
    else:
        return 0

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # Apply the calculate_bonus function to each row
    employees['bonus'] = employees.apply(calculate_bonus, axis=1)
    
    # Select only the employee_id and bonus columns
    result = employees[['employee_id', 'bonus']]
    
    # Order the result by employee_id
    result.sort_values(by='employee_id', inplace=True)
    
    return result

# Example usage:
employees_data = {
    'employee_id': [2, 3, 7, 8, 9],
    'name': ['Meir', 'Michael', 'Addilyn', 'Juan', 'Kannon'],
    'salary': [3000, 3800, 7400, 6100, 7700]
}

employees_df = pd.DataFrame(employees_data)

result = calculate_special_bonus(employees_df)
print(result)