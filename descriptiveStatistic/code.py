import numpy as np
from faker import Faker

fake = Faker()

# Generate data for 20 students
num_students = 20

# Create empty lists to hold the data
student_ids = [1001 + i for i in range(num_students)]  # Sequential student IDs starting from 1001
names = [fake.name() for _ in range(num_students)]  # Generate random names
years_of_study = np.random.randint(1, 5, size=num_students)  # Random years of study between 1 and 4
gpas = np.round(np.random.uniform(3.1, 4.0, size=num_students), 2)  # Random GPAs between 3.1 and 4.0

# Printing the data in a tabular format
print("| Student ID | Name               | Year of Study | GPA  |")
print("|------------|--------------------|---------------|------|")
for i in range(num_students):
    print(f"| {student_ids[i]:<10} | {names[i]:<18} | {years_of_study[i]:<13} | {gpas[i]:<4} |")