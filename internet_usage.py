
import pandas as pd
import matplotlib.pyplot as plt

hours = [2, 3, 3, 4, 4, 4, 5, 5, 6, 4]

purpose = [
    "Study", "Social Media", "Study", "Entertainment",
    "Social Media", "Study", "Communication",
    "Entertainment", "Study", "Social Media"
]

print("Mean:", sum(hours) / len(hours))
print("Median:", 4)
print("Maximum:", max(hours))
print("Minimum:", min(hours))
print("Range:", max(hours) - min(hours))

count = pd.Series(purpose).value_counts()
print("\nInternet Usage Purpose:")
print(count)

count.plot(kind="bar")
plt.title("Internet Usage Among Students")
plt.xlabel("Purpose")
plt.ylabel("Number of Students")
plt.show()
