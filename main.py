import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
trades = pd.read_csv("historical_data.csv")
sentiment = pd.read_csv("fear_greed_index.csv")

# Print column names
print("TRADES COLUMNS:")
print(trades.columns)

print("\nSENTIMENT COLUMNS:")
print(sentiment.columns)

# Convert trade timestamp to date
trades['Date'] = pd.to_datetime(trades['Timestamp'], unit='ms').dt.date

# Convert sentiment date to date format
sentiment['Date'] = pd.to_datetime(sentiment['date']).dt.date

# Merge datasets using Date
merged = pd.merge(trades, sentiment, on='Date')

# Print merged columns
print("\nMERGED COLUMNS:")
print(merged.columns)

# Average profit/loss by sentiment
result = merged.groupby('classification')['Closed PnL'].mean()

print("\nAVERAGE PROFIT BY SENTIMENT:")
print(result)

# Plot graph
result.plot(kind='bar')

plt.title("Average Closed PnL by Market Sentiment")
plt.xlabel("Market Sentiment")
plt.ylabel("Average Closed PnL")

plt.tight_layout()

plt.show()