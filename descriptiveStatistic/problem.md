# Descriptive Statistic
Descriptive statistics play a crucial role in summarizing and understanding data. Typically, when we discuss descriptive statistics, we refer to measures that aggregate data in ways that provide insights into the dataset's overall behavior. Key measures include:

* Mean: The average value, providing a central point around which the data are distributed.
* Median: The middle value in a sorted list of numbers, which divides the dataset into two halves.
* Mode(s): The most frequently occurring value(s) in a dataset.
* Minimum (Min): The smallest value in the dataset.
* Maximum (Max): The largest value in the dataset.
* Quartiles: Values that divide the dataset into four equal parts, highlighting the spread and middle half of the dataset.
* Standard Deviation: A measure of the amount of variation or dispersion in the dataset.
* Variance: The average of the squared differences from the Mean, offering another perspective on data spread.

These quantifications help us understand the dataset, providing a convenient means to visualize or present the data comprehensively. Descriptive statistics offer a straightforward way to convey the essence of the data, making it accessible and interpretable to a wide audience.
Let's say we have such data table.
| Student ID | Name               | Year of Study | GPA  |
|------------|--------------------|---------------|------|
| 1001       | Alex Johnson       | 1             | 3.5  |
| 1002       | Maria Smith        | 2             | 3.6  |
| 1003       | Brian Brown        | 1             | 3.2  |
| 1004       | Fiona Cheng        | 3             | 3.8  |
| 1005       | David Wilson       | 2             | 3.4  |
| 1006       | Emma Watson        | 4             | 3.9  |
| 1007       | George Miller      | 1             | 3.1  |
| 1008       | Hannah Davis       | 2             | 3.5  |
| 1009       | Ian Baker          | 4             | 3.7  |
| 1010       | Jasmine Taylor     | 3             | 3.6  |
| 1011       | Kyle Anderson      | 1             | 3.3  |
| 1012       | Lily Martin        | 2             | 3.5  |
| 1013       | Michael Garcia     | 4             | 3.8  |
| 1014       | Natalie Carter     | 3             | 3.7  |
| 1015       | Oliver Scott       | 2             | 3.4  |
| 1016       | Peyton Jones       | 1             | 3.2  |
| 1017       | Quentin Rodriguez  | 4             | 4.0  |
| 1018       | Riley King         | 3             | 3.6  |
| 1019       | Sophia Lee         | 2             | 3.5  |
| 1020       | Tyler Moore        | 1             | 3.1  |

In case you don't want to use my data you can try to generate your own using below python code.
```python
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
```