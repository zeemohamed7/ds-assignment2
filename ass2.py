import numpy as np

# Student test scores for 3 subjects (math, science, english)
scores = np.array(
    [
        [85, 92, 78],
        [90, 88, 95],
        [75, 70, 85],
        [88, 95, 92],
        [65, 72, 68],
        [95, 88, 85],
        [78, 85, 82],
        [92, 89, 90],
    ]
)

subjects = np.array(["Math", "Science", "English"])

# Student names
names = np.array(["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Henry"])

# Random 4x4 matrix for linear algebra operations
matrix_A = np.random.randint(1, 10, size=(4, 4))
matrix_B = np.random.randint(1, 10, size=(4, 4))


## 1. Array Operations and Indexing
# 1.1 Calculate the average score for each student across all subjects
average_scores = np.mean(scores, axis=1)  # axis=1 meaning compute across columns
# print("Average scores:", average_scores)
# print("Students and their averages:")
# for name, avg in zip(names, average_scores):
#     print(f"{name}: {avg:.2f}")

# 1.2 Find the highest score in each subject
highest_scores = np.max(scores, axis=0)
# print("Subjects and their highest scores:")
# for subject, highest_score in zip(subjects, highest_scores):
#     print(f"{subject}: {highest_score:.2f}")


# 1.3 Select all students who scored above 90 in any subject
mask_above_90 = np.array(scores > 90)  # boolean array of scores above 90
# print(mask_above_90)
any_above_90 = np.any(
    mask_above_90, axis=1
)  # ANY test is true so we can turn it into 1 dimenstional array
# print(any_above_90)
scores_above_90 = names[any_above_90]
# print("Students who scored above 90 in any subject:")
# print(scores_above_90)


# Create a boolean mask to find students who passed all subjects (passing score is 70)
mask_passed = scores >= 70
# print(mask_passed)
all_passed = np.all(mask_passed, axis=1)
# print(all_passed)
students_passed = names[all_passed]
# print("Students who passed all subjects:")
# print(students_passed)


## 2. Array Manipulation
# 2.1 Reshape the scores array to be 12x2
# print(scores.reshape(12, 2))

# 2.2 Create a new array with standardized scores (subtract mean and divide by std dev)
# print((scores - np.mean(scores)) / np.std(scores))

# 2.3 Sort the students by their average score in descending order
# print(np.sort(average_scores)[::-1])  # [::-1] to reverse

# 2.4 Use array methods to find min, max and mean for each subject
# print(np.min(scores, axis=0))
# print(np.max(scores, axis=0))
# print(np.mean(scores, axis=0))


## 3. Linear Algebra
# 3.1 Multiply matrix_A and matrix_B using matrix multiplication
# print(matrix_A @ matrix_B)

# 3.2 Calculate the determinant of matrix_A
# print(np.linalg.det(matrix_A))
# 3.3 Find the inverse of matrix_A (if it exists)
print("Inverse of matrix A")
# print(
#     np.linalg.inv(matrix_A)
# )  # determinant isn't 0, matrix is square, hence there is an inverse

# Calculate the eigenvalues of matrix_A
print("eigenvalues of matrix_A")
# print(np.linalg.eigvals(matrix_A))


# 4. Advanced Operations
# 4.1 Use broadcasting to add 5 points to all math scores (first column)
print("Updated column with + 5")
print(scores[:, 0] + 5)
# 4.2 Find unique scores across all subjects
print("Unique scores:")
print(np.unique(scores))
# 4.3 Use boolean indexing to find students who scored above average in all subjects
avg_in_each_subject = np.mean(scores, axis=0)
scores_above_avg = scores > avg_in_each_subject
all_above_average_mask = np.all(scores_above_avg, axis=1)
above_average_students = names[all_above_average_mask]

print(above_average_students)
# for name, avg in zip(names, average_scores):
#     print(f"{name}: {avg:.2f}")

# Expected Format
# Show your work with clear explanations. For each task, your output should look like:

# # Task 1.1: Average scores per student
# average_scores = scores.mean(axis=1)
# print("Average scores:", average_scores)
# print("Students and their averages:")
# for name, avg in zip(names, average_scores):
#     print(f"{name}: {avg:.2f}")


# 5. Bonus Challenge
# Create a function that takes a student’s name as input and returns:
def student_info(name):
    # find index
    index = np.where(names == name)[0][
        0
    ]  # destructring cause it returns (array([1]),) originally

    # Their individual scores
    individual_scores = scores[index]

    # Their ranking in each subject
    # how many students got higher than them
    higher_mask = individual_scores < scores
    higher_students = np.sum(higher_mask, axis=0)
    rank_in_each_subject = higher_students + 1

    # A boolean indicating if they’re in the top 3 performers overall
    # total for each student
    totals = np.sum(scores, axis=1)
    student_total = np.sum(individual_scores)
    highest_sums = np.sort(totals)
    is_top_three_performer = (
        student_total >= highest_sums[-3]
    )  # compare to third highest

    return (individual_scores, rank_in_each_subject, is_top_three_performer)


print(student_info("Bob"))
