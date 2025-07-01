import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
file_path = "C:/Users/shash/OneDrive/Desktop/Internship 2/task 2/Unemployment_Rate_upto_11_2020.csv"
df = pd.read_csv(file_path)

# Step 2: Clean column names
df.columns = df.columns.str.strip()

# Step 3: Clean leading/trailing spaces in date values
df['Date'] = df['Date'].str.strip()

# Step 4: Convert 'Date' to datetime format
df['Date'] = pd.to_datetime(df['Date'], format="%d-%m-%Y")

# Step 5: Rename columns for ease of use
df.rename(columns={
    'Region': 'State',
    'Estimated Unemployment Rate (%)': 'Unemployment_Rate',
    'Estimated Employed': 'Employed',
    'Estimated Labour Participation Rate (%)': 'Labour_Participation',
    'Region.1': 'Region'
}, inplace=True)

# Step 6: Sort data by date
df.sort_values(by='Date', inplace=True)

# Step 7: Print basic info
print("\n📊 First 5 rows of data:\n", df.head())
print("\n🧾 Info:\n")
df.info()
print("\n🔍 Null values:\n", df.isnull().sum())

# Step 8: Line plot - National Unemployment Trend
plt.figure(figsize=(12, 6))
sns.lineplot(x='Date', y='Unemployment_Rate', data=df, errorbar=None)
plt.title("India's Unemployment Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 9: Boxplot - State-wise variation
plt.figure(figsize=(14, 7))
top_states = df['State'].value_counts().index[:10]
sns.boxplot(x='State', y='Unemployment_Rate', data=df[df['State'].isin(top_states)])
plt.xticks(rotation=45)
plt.title("Unemployment Rate Distribution by State")
plt.tight_layout()
plt.show()

# Step 10: Lineplot - Unemployment during COVID (March 2020 onward)
covid_df = df[df['Date'] >= "2020-03-01"]
plt.figure(figsize=(12, 6))
sns.lineplot(x='Date', y='Unemployment_Rate', data=covid_df)
plt.title("Unemployment Rate During COVID-19 (March 2020 onward)")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 11: Monthly average unemployment trends
df['Month'] = df['Date'].dt.month
monthly_avg = df.groupby('Month')['Unemployment_Rate'].mean()

plt.figure(figsize=(10, 5))
monthly_avg.plot(kind='bar', color='skyblue')
plt.title("Average Unemployment Rate by Month")
plt.xlabel("Month")
plt.ylabel("Avg Unemployment Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
