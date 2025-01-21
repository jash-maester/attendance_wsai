import sqlite3
import csv

# Path to the SQLite database file
DATABASE_PATH = "instance/database.db"
CSV_FILE_PATH = "roll_numbers_export.csv"

def export_to_csv():
    # Connect to the SQLite database
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    try:
        # Query all data from the RollNumber table
        cursor.execute("SELECT roll_number, ip_address FROM roll_number")
        rows = cursor.fetchall()

        # Export data to a CSV file
        with open(CSV_FILE_PATH, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            # Write the header
            writer.writerow(["Roll Number", "IP Address"])

            # Write the rows
            writer.writerows(rows)

        print(f"Data exported successfully to {CSV_FILE_PATH}")

    except sqlite3.OperationalError as e:
        print(f"Error: {e}")
    finally:
        # Close the database connection
        conn.close()

if __name__ == "__main__":
    export_to_csv()
