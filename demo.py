import sqlite3
import pandas as pd

# Step 1. Laod data file
df = pd.read_csv('TATAMOTORS.NS.csv')

# Step 2. Data Clean Up
df.columns = df.columns.str.strip()

# Step 2.1: Drop rows with any null values
df = df.dropna()

# Step 3. Create/connect to a SQLite database
connection = sqlite3.connect ('demo.db')

# Step 4. Load data file to SQLite
# fail;replace; append
df.to_sql('TATAMOTORS.NS', connection, if_exists='replace')

# Step 5. Close connection