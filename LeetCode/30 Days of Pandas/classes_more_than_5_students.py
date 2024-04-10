# 596. Classes More Than 5 Students
# Table: Courses

# +-------------+---------+
# | Column Name | Type |
# +-------------+---------+
# | student | varchar |
# | class | varchar |
# +-------------+---------+
# (student, class) is the primary key (combination of columns with unique values) for this table.
# Each row of this table indicates the name of a student and the class in which they are enrolled.


# Write a solution to find all the classes that have at least five students.

# Return the result table in any order.

# The result format is in the following example.


# Example 1:

# Input:
# Courses table:
# +---------+----------+
# | student | class |
# +---------+----------+
# | A | Math |
# | B | English |
# | C | Math |
# | D | Biology |
# | E | Math |
# | F | Computer |
# | G | Math |
# | H | Math |
# | I | Math |
# +---------+----------+
# Output:
# +---------+
# | class |
# +---------+
# | Math |
# +---------+
# Explanation:
# - Math has 6 students, so we include it.
# - English has 1 student, so we do not include it.
# - Biology has 1 student, so we do not include it.
# - Computer has 1 student, so we do not include it.

import pandas as pd


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    # Group by class and count the number of students in each class
    class_counts = courses.groupby('class')['student'].count().reset_index()
    # Filter out classes with at least five students
    result = class_counts[class_counts['student'] >= 5][['class']]
    return result


# Example usage:
courses_data = pd.DataFrame({
    'student': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    'class': ['Math', 'English', 'Math', 'Biology', 'Math', 'Computer', 'Math', 'Math', 'Math']
})

result = find_classes(courses_data)
print(result)
