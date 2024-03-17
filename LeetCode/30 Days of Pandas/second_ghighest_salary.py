# 176. Second Highest Salary


# Table: Employee

# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | salary      | int  |
# +-------------+------+
# id is the primary key (column with unique values) for this table.
# Each row of this table contains information about the salary of an employee.


# Write a solution to find the second highest salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

# The result format is in the following example.


# Example 1:

# Input:
# Employee table:
# +----+--------+
# | id | salary |
# +----+--------+
# | 1  | 100    |
# | 2  | 200    |
# | 3  | 300    |
# +----+--------+
# Output:
# +---------------------+
# | SecondHighestSalary |
# +---------------------+
# | 200                 |
# +---------------------+
# Example 2:

# Input:
# Employee table:
# +----+--------+
# | id | salary |
# +----+--------+
# | 1  | 100    |
# +----+--------+
# Output:
# +---------------------+
# | SecondHighestSalary |
# +---------------------+
# | null                |
# +---------------------+


import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # Remove duplicate salaries and sort the DataFrame by salary in descending order
    sorted_df = employee.drop_duplicates(subset='salary').sort_values(by='salary', ascending=False)
    
    # Getting the second highest salary
    second_highest_salary = sorted_df['salary'].iloc[1] if len(sorted_df) > 1 else None
    
    # Creating the output DataFrame
    output_df = pd.DataFrame({'SecondHighestSalary': [second_highest_salary]})
    
    return output_df


employee = pd.DataFrame({
    'id': [1, 2, 3],
    'salary': [100, 200, 300]
})


output = second_highest_salary(employee)
print(output)
