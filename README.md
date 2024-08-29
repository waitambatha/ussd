# ETL Pipeline Demo with Streamlit

This is a simple Streamlit application demonstrating an ETL (Extract, Transform, Load) pipeline using Python. The app allows users to upload a CSV file, perform data cleaning and transformations, and load the data into a SQLite database.

## Features

- **Extract:** Upload a CSV file containing the raw data.
- **Transform:** Perform data cleaning and transformation operations such as dropping missing values and renaming columns.
- **Load:** Save the transformed data into a SQLite database.
- **Database Query:** Option to display the loaded data from the SQLite database.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Required Python packages:
  - streamlit
  - pandas
  - sqlite3 (comes with Python)

You can install the required packages using `pip`:

```bash
pip install streamlit pandas
Running the App
Clone the repository (if applicable) or download the etl_app.py file to your local machine.

Run the Streamlit app with the following command:

bash
Copy code
streamlit run etl_app.py
Open the app in your web browser (if it doesn't open automatically):

arduino
Copy code
http://localhost:8501
Using the App
Upload your CSV file: Start by uploading the CSV file that you want to process.

Transform the data:

Drop rows with missing values (optional).
Rename columns as needed.
Load the data into a database:

Enter the name of the SQLite database and the table name where the data will be stored.
Click the button to load the data into the database.
Query the database: Optionally, view the data stored in the database directly within the app.

Customization
Feel free to modify the code in etl_app.py to suit your specific ETL requirements. You can add more complex transformations, integrate with other databases, or include additional data sources.