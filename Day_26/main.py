# List Comprehensions
numbers = [1, 2, 3]

new_numbers = [n + 1 for n in numbers]

# List Comprehension with conditional
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

short_names = [name for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) > 5]

# Dictionary Comprehension
import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = { student:random.randint(1, 100) for student in names}
passed_students = {
    student:score for (student, score) in students_scores.items() if score >= 60
}