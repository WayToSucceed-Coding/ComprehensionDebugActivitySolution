import matplotlib.pyplot as plt

# Step 1: Dataset of students and their scores
students_data = [
    {"name": "Alice", "score": 88},
    {"name": "Bob", "score": 72},
    {"name": "Charlie", "score": 95},
    {"name": "David", "score": 60},
    {"name": "Eve", "score": 77},
    {"name": "Frank", "score": 85},
]

# Dictionary comprehension to filter students with score >= 75 
high_score_students = {student["name"]:student["score"] for student in students_data if student["score"] >= 75}  

#Plot the bar chart
names = list(high_score_students.keys())
scores = list(high_score_students.values())

plt.figure(figsize=(10, 6))
plt.bar(names, scores)
plt.xlabel("Student Names")
plt.ylabel("Scores")
plt.title("Student Scores")
plt.show()
