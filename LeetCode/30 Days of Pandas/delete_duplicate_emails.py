# 196. Delete Duplicate Emails

# Table: Person

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | email       | varchar |
# +-------------+---------+
# id is the primary key (column with unique values) for this table.
# Each row of this table contains an email. The emails will not contain uppercase letters.


# Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.

# For SQL users, please note that you are supposed to write a DELETE statement and not a SELECT one.

# For Pandas users, please note that you are supposed to modify Person in place.

# After running your script, the answer shown is the Person table. The driver will first compile and run your piece of code and then show the Person table. The final order of the Person table does not matter.

# The result format is in the following example.


# Example 1:

# Input:
# Person table:
# +----+------------------+
# | id | email            |
# +----+------------------+
# | 1  | john@example.com |
# | 2  | bob@example.com  |
# | 3  | john@example.com |
# +----+------------------+
# Output:
# +----+------------------+
# | id | email            |
# +----+------------------+
# | 1  | john@example.com |
# | 2  | bob@example.com  |
# +----+------------------+
# Explanation: john@example.com is repeated two times. We keep the row with the smallest Id = 1.

import pandas as pd


def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # Sort the rows based on id (Ascending order)
    person.sort_values(by='id', ascending=True, inplace=True)
    # Drop the duplicates based on email.
    person.drop_duplicates(subset='email', keep='first', inplace=True)


# Input data
data = {
    'id': [1, 2, 3],
    'email': ['john@example.com', 'bob@example.com', 'john@example.com']
}

# Create DataFrame
person_df = pd.DataFrame(data)

print("Input:")
print(person_df)

# Call the function
delete_duplicate_emails(person_df)

print("\nOutput:")
print(person_df)
