import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset with proper parsing
try:
    df = pd.read_csv("data/unemployment.csv", header=0)

    if df.empty:
        raise ValueError("⚠️ The dataset appears to be empty. Please check 'unemployment.csv' in the 'data/' folder.")

    print("\n✅ Dataset Loaded Successfully!")
except FileNotFoundError:
    print("🚨 Error: 'unemployment.csv' file not found. Please make sure it's placed inside 'data/' folder.")
    exit()
except ValueError as e:
    print(str(e))
    exit()

# Display basic data insights
print("\n📌 First few rows of the dataset:")
print(df.head())

print("\n📌 Dataset Info:")
print(df.info())

print("\n📌 Summary Statistics:")
print(df.describe())

# Check for missing values
print("\n📌 Missing Values in Each Column:")
print(df.isnull().sum())

# Convert Date column to datetime format (if applicable)
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'])
    print("\n📌 Date column converted to datetime format.")
else:
    print("\n🚨 Error: 'Date' column missing! Please check your dataset.")

# Data Visualization: Unemployment Rate Over Time
if 'Date' in df.columns and 'Unemployment Rate' in df.columns:
    plt.figure(figsize=(10,6))
    sns.lineplot(x=df["Date"], y=df["Unemployment Rate"], marker='o', color="blue")
    plt.title("📈 Unemployment Rate Over Time", fontsize=14)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Unemployment Rate", fontsize=12)
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()

    # Save visualization
    plt.savefig("reports/unemployment_trends.png", dpi=300)
    print("\n✅ Analysis completed! Visualization saved as 'unemployment_trends.png' in reports/ folder.")
else:
    print("\n🚨 Error: Required columns missing! Please check your dataset structure.")