# 1907. Count Salary Categories

# Table: Accounts

# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | account_id  | int  |
# | income      | int  |
# +-------------+------+
# account_id is the primary key (column with unique values) for this table.
# Each row contains information about the monthly income for one bank account.


# Write a solution to calculate the number of bank accounts for each salary category. The salary categories are:

# "Low Salary": All the salaries strictly less than $20000.
# "Average Salary": All the salaries in the inclusive range [$20000, $50000].
# "High Salary": All the salaries strictly greater than $50000.
# The result table must contain all three categories. If there are no accounts in a category, return 0.

# Return the result table in any order.

# The result format is in the following example.


# Example 1:

# Input:
# Accounts table:
# +------------+--------+
# | account_id | income |
# +------------+--------+
# | 3          | 108939 |
# | 2          | 12747  |
# | 8          | 87709  |
# | 6          | 91796  |
# +------------+--------+
# Output:
# +----------------+----------------+
# | category       | accounts_count |
# +----------------+----------------+
# | Low Salary     | 1              |
# | Average Salary | 0              |
# | High Salary    | 3              |
# +----------------+----------------+
# Explanation:
# Low Salary: Account 2.
# Average Salary: No accounts.
# High Salary: Accounts 3, 6, and 8.

import pandas as pd

# Function to categorize income


def categorize_income(income):
    if income < 20000:
        return 'Low Salary'
    elif 20000 <= income <= 50000:
        return 'Average Salary'
    else:
        return 'High Salary'


def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    # Applying categorization function and counting accounts for each category
    accounts['category'] = accounts['income'].apply(categorize_income)
    result = accounts.groupby('category').size(
    ).reset_index(name='accounts_count')

    # Filling missing categories with count 0
    categories = ['Low Salary', 'Average Salary', 'High Salary']
    result = result.set_index('category').reindex(
        categories, fill_value=0).reset_index()
    return result


# Sample data
data = {
    'account_id': [3, 2, 8, 6],
    'income': [108939, 12747, 87709, 91796]
}

print(count_salary_categories(data))
