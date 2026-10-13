import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dates = ["2026-05-01", "2026-05-02", "2026-05-03", "2026-05-04", "2026-05-05",
         "2026-05-06", "2026-05-07", "2026-05-08", "2026-05-09", "2026-05-10",
         "2026-05-11", "2026-05-12", "2026-05-13", "2026-05-14", "2026-05-15",
         "2026-05-15"]
cities = [" islamabad", "ISLAMABAD ", "Islamabad", "islamabad ", " Islamabad", "ISLAMABAD",
          "Islamabad", " islamabad", "Islamabad ", "ISLAMABAD", "islamabad", " Islamabad ",
          "Islamabad", "ISLAMABAD ", "islamabad", "islamabad"]
temps = ["34C", "35C", "31C", "26C", "25C", "29C", "33C", "36C",
         "30C", "34C", "28C", "24C", "32C", "30C", "35C", "35C"]
humidity = [40, 38, 57, 82, 85, 62, np.nan, 36,
            59, np.nan, 66, 88, 46, np.nan, 42, 42]
conditions = ["sunny", "SUNNY ", " Cloudy", "rainy", " Rainy", "CLOUDY ", "Sunny", " sunny",
              "cloudy", "SUNNY", "Cloudy ", "RAINY", "sunny ", "cloudy", " Sunny", " Sunny"]

df = pd.DataFrame({"Date": dates, "City": cities, "Temperature": temps,
                   "Humidity": humidity, "Condition": conditions})

df["City"] = df["City"].str.strip().str.title()
df["Condition"] = df["Condition"].str.strip().str.title()
df["Temperature"] = df["Temperature"].str.replace("C", "", regex=False).astype(float)
df["Date"] = pd.to_datetime(df["Date"])

print("Duplicate rows:", df.duplicated().sum())
df = df.drop_duplicates()
print("Rows after dropping duplicates:", len(df))

median_humidity = df["Humidity"].median()
df["Humidity"] = df["Humidity"].fillna(median_humidity)
print("Missing Humidity filled with median:", median_humidity)

encoded = pd.get_dummies(df, columns=["Condition"], dtype=int)
print(encoded.filter(like="Condition_").head())

corr = df["Temperature"].corr(df["Humidity"])
print("Correlation (Temperature, Humidity):", round(corr, 2))

counts = df["Condition"].value_counts()
print("Condition counts:")
print(counts)

fig, axes = plt.subplots(2, 2, figsize=(12, 9))

axes[0, 0].plot(df["Date"], df["Temperature"], marker="o", color="steelblue")
axes[0, 0].set_title("Temperature over Date")
axes[0, 0].set_xlabel("Date")
axes[0, 0].set_ylabel("Temperature (C)")
axes[0, 0].tick_params(axis="x", rotation=45)
axes[0, 0].grid(True, alpha=0.3)

axes[0, 1].scatter(df["Temperature"], df["Humidity"], color="darkorange", s=60)
axes[0, 1].set_title("Temperature vs. Humidity")
axes[0, 1].set_xlabel("Temperature (C)")
axes[0, 1].set_ylabel("Humidity (%)")
axes[0, 1].grid(True, alpha=0.3)

axes[1, 0].pie(counts.values, labels=counts.index, autopct="%1.1f%%", startangle=90,
               colors=["#F58518", "#4C78A8", "#54A24B"])
axes[1, 0].set_title("Days per Condition")

axes[1, 1].hist(df["Temperature"], bins=5, color="seagreen", edgecolor="white")
axes[1, 1].set_title("Temperature Distribution")
axes[1, 1].set_xlabel("Temperature (C)")
axes[1, 1].set_ylabel("Number of Days")

fig.suptitle("Weather Overview", fontsize=16)
plt.tight_layout()
plt.savefig("weather_dashboard.png")
plt.show()

print("Saved weather_dashboard.png")