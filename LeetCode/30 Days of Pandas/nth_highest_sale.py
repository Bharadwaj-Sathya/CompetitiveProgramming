# 177. Nth Highest Salary

# Table: Employee

# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | salary      | int  |
# +-------------+------+
# id is the primary key (column with unique values) for this table.
# Each row of this table contains information about the salary of an employee.


# Write a solution to find the nth highest salary from the Employee table. If there is no nth highest salary,
# return null.

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
# n = 2
# Output:
# +------------------------+
# | getNthHighestSalary(2) |
# +------------------------+
# | 200                    |
# +------------------------+
# Example 2:

# Input:
# Employee table:
# +----+--------+
# | id | salary |
# +----+--------+
# | 1  | 100    |
# +----+--------+
# n = 2
# Output:
# +------------------------+
# | getNthHighestSalary(2) |
# +------------------------+
# | null                   |
# +------------------------+


import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # Drop duplicate salaries to get unique values
    unique_salaries = employee['salary'].unique()

    # Sort unique salaries in descending order
    unique_salaries_sorted = sorted(unique_salaries, reverse=True)

    # Check if N is positive and there are at least N unique salaries
    if N > 0 and N <= len(unique_salaries_sorted):
        # Select the Nth highest salary
        nth_highest_salary = unique_salaries_sorted[N - 1]
        return pd.DataFrame({f'getNthHighestSalary({N})': [nth_highest_salary]})
    else:
        # If N is not positive or there are fewer than N unique salaries, return null
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})


employee = pd.DataFrame({
    'id': [1, 2, 3],
    'salary': [100, 200, 300]
})

N = 2

output = nth_highest_salary(employee, N)
print(output)
