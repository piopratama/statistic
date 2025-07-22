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

In case you don't want to use my data, then you can try to generate your own using below python code (make sure you install faker using pip).
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

Before we are going any further let's jsut focus on how do we calculate some of the quantifications we mention earlier. In this case I am intrested to use GPA data. To do this we will implement python library called numpy.

```python
# Calculate descriptive statistics for GPAs
mean_gpa = np.mean(gpas)
median_gpa = np.median(gpas)
min_gpa = np.min(gpas)
max_gpa = np.max(gpas)
std_dev_gpa = np.std(gpas)
variance_gpa = np.var(gpas)

mean_gpa, median_gpa, min_gpa, max_gpa, std_dev_gpa, variance_gpa
```

if you are using the data in the table I gave, then you will got this result:
```
Mean GPA: 3.52
Median GPA: 3.5
Minimum GPA: 3.1
Maximum GPA: 4.0
Standard Deviation: Approximately 0.25
Variance: Approximately 0.063
```

# Interpretation
Descriptive statistics offer valuable insights into the academic performance of our students. The mean GPA of 3.52 suggests that, on average, students are performing well academically. The median GPA of 3.5, being very close to the mean, indicates a relatively symmetric distribution of GPAs around the central value, with slight skewness to the right. This suggests that while most students have GPAs close to the median and are performing quite well, a smaller number of students with significantly lower GPAs are affecting the average, causing a left-skewed distribution. The minimum GPA of 3.1 and the maximum GPA of 4.0 indicate that most students are performing well, with only a small range of variation in academic achievement. Furthermore, the standard deviation and variance values, which are relatively low at approximately 0.25 and 0.063 respectively, indicate that the GPAs are tightly clustered around the mean. This suggests that there's not much disparity in academic performance among the students, and most of them are performing consistently well. Overall, the descriptive statistics paint a picture of a student cohort that is performing well academically, with consistent and symmetrical distribution of GPAs around the mean. These insights can inform teaching strategies and interventions to further support student success.

# Simulation
This addition expands the discussion beyond descriptive statistics, introducing the concept of predictive modeling and simulation as a method to leverage the insights gained from descriptive statistics for forecasting future outcomes. It adds depth to the analysis and encourages further exploration of the dataset's potential applications.
Let's apply simulation based on the quantifier we have done.
```python
import numpy as np

# Define descriptive statistics of the original GPA dataset
mean_gpa = 3.52
median_gpa = 3.5
std_dev_gpa = 0.25
min_gpa = 3.1
max_gpa = 4.0

# Simulate a new dataset based on the characteristics of the original dataset
num_students = 1000  # Number of students in the new dataset
simulated_gpas = np.random.normal(loc=mean_gpa, scale=std_dev_gpa, size=num_students)

# Ensure the generated GPAs are within the range of the original dataset
simulated_gpas = np.clip(simulated_gpas, min_gpa, max_gpa)

# Print some statistics of the simulated dataset
print("Mean GPA of the simulated dataset:", np.mean(simulated_gpas))
print("Median GPA of the simulated dataset:", np.median(simulated_gpas))
print("Standard Deviation of the simulated dataset:", np.std(simulated_gpas))
print("Minimum GPA of the simulated dataset:", np.min(simulated_gpas))
print("Maximum GPA of the simulated dataset:", np.max(simulated_gpas))
```

# Simulation Purpose
Ever thought of data simulation as a research superhero? It's not just about making predictions – it's like having a secret weapon for exploring, analyzing, and uncovering hidden insights!
Picture this: you're not just crunching numbers; you're going on a data adventure, searching for clues, and solving mysteries along the way. It's like being a detective in the world of data!
But here's the coolest part: simulation isn't just for making predictions. It's also your go-to when you're low on real-world data. Whether it's because of privacy concerns, data shortages, or any other roadblocks, simulation comes to the rescue!
So, next time you're stuck with limited data, don't panic. Dive into the world of simulation, where every data point is a new discovery, and every analysis is a thrilling journey into the unknown!
## Manual Calculation Without Libraries
Sometimes using libraries can hide the underlying math. The script `manual_stats.py` demonstrates how to compute the mean, median, mode, variance and standard deviation with nothing more than Python's built‑in features.
