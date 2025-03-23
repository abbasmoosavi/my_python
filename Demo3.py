import pandas as pd

# Dataset
data = {
    "Student": ["Amit", "John", "Jacob", "David", "Steve"],
    "Rank": [1, 4, 3, 5, 2],
    "Marks": [95, 70, 80, 60, 90],
}

df = pd.DataFrame(data, index=["RowA", "RowB", "RowC", "RowD", "RowE"])

print("Student Records\n\n", df)

print("\nValue= \n", df.iloc[3, 2])
print("\nValue= \n", df.iloc[[3, 2]])
