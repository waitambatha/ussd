import streamlit as st
import pandas as pd
import sqlite3
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


# Title of the app
st.title(" ussd sesssions with streamlit ")

# Step 1: Extract - Load the predefined CSV file
st.header("Step 1: Extract")
file_path = 'ussd.csv'  # Update with your file path if necessary
df = pd.read_csv(file_path)

# Show the first few rows of the dataset
st.subheader("Dataset Preview")
st.write(df.head())

# Step 2: Transform - Data Cleaning and Transformation
st.header("Step 2: Transform")

# Option to drop missing values
if st.checkbox("Drop rows with missing values"):
    df.dropna(inplace=True)
    st.write("Dropped rows with missing values.")

# Option to rename columns
st.subheader("Rename Columns")
for col in df.columns:
    new_col_name = st.text_input(f"Rename column '{col}'", col)
    if new_col_name:
        df.rename(columns={col: new_col_name}, inplace=True)

# Show transformed data
st.subheader("Transformed Data Preview")
st.write(df.head())

# Step 3: Load - Save Data to SQLite and PostgreSQL Databases
st.header("Step 3: Load")

# SQLite
db_name_sqlite = st.text_input("Enter SQLite Database Name", "etl_database.db")
table_name_sqlite = st.text_input("Enter Table Name for SQLite", "etl_table_sqlite")

if st.button("Load Data into SQLite"):
    # Connect to SQLite database (or create it if it doesn't exist)
    conn_sqlite = sqlite3.connect(db_name_sqlite)
    df.to_sql(table_name_sqlite, conn_sqlite, if_exists='replace', index=False)
    conn_sqlite.close()
    st.success(f"Data loaded successfully into {db_name_sqlite} (Table: {table_name_sqlite})")



# Option to display SQL table from SQLite
if st.checkbox("Display Data from SQLite"):
    conn_sqlite = sqlite3.connect(db_name_sqlite)
    query_sqlite = f"SELECT * FROM {table_name_sqlite}"
    result_df_sqlite = pd.read_sql(query_sqlite, conn_sqlite)
    conn_sqlite.close()

    st.subheader(f"Data in {table_name_sqlite} Table (SQLite)")
    st.write(result_df_sqlite)

# Option to display SQL table from PostgreSQL

