import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Raw input data (15-day weather log with duplicate and missing values)
raw_data = {
    "Date": ["2026-03-01", "2026-03-02", "2026-03-03", "2026-03-04", "2026-03-05", 
             "2026-03-06", "2026-03-07", "2026-03-08", "2026-03-09", "2026-03-10", 
             "2026-03-11", "2026-03-12", "2026-03-13", "2026-03-14", "2026-03-15", "2026-03-03"],
    "City": [" Lahore", "ISLAMABAD", "Karachi", "lahore", "Islamabad", 
             "KARACHI", "Lahore", "islamabad", "Karachi", "LAHORE", 
             "karachi", "Islamabad", "Lahore", "Karachi", "Islamabad", "Karachi"],
    "Temperature": ["32C", "28C", "35C", "30C", "27C", "36C", "31C", "29C", "34C", "33C", "37C", "26C", "30C", "35C", "25C", "35C"],
    "Humidity": [55.0, 60.0, np.nan, 58.0, np.nan, 45.0, 52.0, 65.0, np.nan, 50.0, 42.0, 70.0, 56.0, 48.0, 75.0, np.nan],
    "Condition": ["sunny", " Rainy", "CLOUDY ", "sunny ", "Rainy", "SUNNY", "cloudy", "Rainy ", "sunny", "Sunny", "sunny", "CLOUDY", "sunny", "cloudy", "Rainy", "CLOUDY "]
}

df = pd.DataFrame(raw_data)

# (a) Data Cleaning
df["City"] = df["City"].str.strip().str.title()
df["Condition"] = df["Condition"].str.strip().str.title()
df["Temperature"] = df["Temperature"].str.replace("C", "", regex=False).astype(float)
df["Date"] = pd.to_datetime(df["Date"])

# Drop duplicates
df = df.drop_duplicates()
print("Rows after dropping duplicates:", len(df))

# Fill missing Humidity with median
median_humidity = df["Humidity"].median()
df["Humidity"] = df["Humidity"].fillna(median_humidity)
print("Missing Humidity filled with median:", median_humidity)

# (b) One-hot encode Condition
df_encoded = pd.get_dummies(df, columns=["Condition"], dtype=int)
print("\nOne-hot encoded columns:")
print(df_encoded.filter(like="Condition_").head())

# (d) Correlation coefficient calculation
corr = round(df["Temperature"].corr(df["Humidity"]), 2)
print("\nCorrelation (Temperature, Humidity):", corr)

# (e/f) 2x2 Subplot Dashboard Creation
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 1. Line Plot: Temperature over Date
axes[0, 0].plot(df["Date"].dt.strftime("%m-%d"), df["Temperature"], marker="o", color="crimson")
axes[0, 0].set_title("Temperature Over Time")
axes[0, 0].set_xlabel("Date")
axes[0, 0].set_ylabel("Temperature (°C)")
axes[0, 0].tick_params(axis="x", rotation=45)
axes[0, 0].grid(True, alpha=0.3)

# 2. Scatter Plot: Temperature vs. Humidity
axes[0, 1].scatter(df["Temperature"], df["Humidity"], color="purple", s=60)
axes[0, 1].set_title("Temperature vs. Humidity")
axes[0, 1].set_xlabel("Temperature (°C)")
axes[0, 1].set_ylabel("Humidity (%)")
axes[0, 1].grid(True, alpha=0.3)

# 3. Pie Chart: Weather Condition Share
cond_counts = df["Condition"].value_counts()
axes[1, 0].pie(cond_counts.values, labels=cond_counts.index, autopct="%1.1f%%", startangle=90)
axes[1, 0].set_title("Condition Distribution")

# 4. Histogram: Temperature Distribution
axes[1, 1].hist(df["Temperature"], bins=5, color="seagreen", edgecolor="white")
axes[1, 1].set_title("Temperature Distribution")
axes[1, 1].set_xlabel("Temperature (°C)")
axes[1, 1].set_ylabel("Days")

fig.suptitle("Weather Overview", fontsize=16)
plt.tight_layout()
plt.savefig("weather_dashboard.png")
plt.show()