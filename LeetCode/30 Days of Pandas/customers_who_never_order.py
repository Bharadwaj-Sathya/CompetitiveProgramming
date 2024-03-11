# 183. Customers Who Never Order

# Table: Customers

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# +-------------+---------+
# id is the primary key (column with unique values) for this table.
# Each row of this table indicates the ID and name of a customer.


# Table: Orders

# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | customerId  | int  |
# +-------------+------+
# id is the primary key (column with unique values) for this table.
# customerId is a foreign key (reference columns) of the ID from the Customers table.
# Each row of this table indicates the ID of an order and the ID of the customer who ordered it.


# Write a solution to find all customers who never order anything.

# Return the result table in any order.

# The result format is in the following example.


# Example 1:

# Input:
# Customers table:
# +----+-------+
# | id | name  |
# +----+-------+
# | 1  | Joe   |
# | 2  | Henry |
# | 3  | Sam   |
# | 4  | Max   |
# +----+-------+
# Orders table:
# +----+------------+
# | id | customerId |
# +----+------------+
# | 1  | 3          |
# | 2  | 1          |
# +----+------------+
# Output:
# +-----------+
# | Customers |
# +-----------+
# | Henry     |
# | Max       |
# +-----------+

import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = customers.merge(orders, how="left", left_on='id',
                         right_on='customerId')
    df = df[df['customerId'].isna()]
    df = df[['name']].rename(columns={'name': 'Customers'})
    return df


# Create the Customers DataFrame
customers_data = {
    'id': [1, 2, 3, 4],
    'name': ['Joe', 'Henry', 'Sam', 'Max']
}

customers_df = pd.DataFrame(customers_data)

# Create the Orders DataFrame
orders_data = {
    'id': [1, 2],
    'customerId': [3, 1]
}

orders_df = pd.DataFrame(orders_data)

print(find_customers(customers_df, orders_df))
