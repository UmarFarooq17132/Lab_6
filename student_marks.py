import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Raw input data
raw_data = {
    "Name": [" ali", "SARA ", "bilal", " Ayesha", "HAMZA", "zain ", "Noor", " usman "],
    "Marks": ["72", "85", "absent", "64", "90", "78", "81", "69"]
}

df = pd.DataFrame(raw_data)

# (a) Clean Name using .str.strip() and .str.title()
df["Name"] = df["Name"].str.strip().str.title()

# (b) Convert Marks to numbers and fill "absent" with the mean of other marks
df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")
mean_marks = round(df["Marks"].mean(), 1)
df["Marks"] = df["Marks"].fillna(mean_marks)

# (c) Print cleaned DataFrame
print("Cleaned DataFrame:")
print(df)

# (d) Draw bar plot of marks per student
plt.figure(figsize=(8, 5))
plt.bar(df["Name"], df["Marks"], color="skyblue", edgecolor="black")
plt.title("Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.ylim(0, 100)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()

# Save the plot
plt.savefig("marks_bar.png")
plt.show()