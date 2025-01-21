# Local Attendance Project

This project is a simple Flask-based application that allows students to submit their roll numbers via a web interface. The submitted roll numbers are stored in an SQLite database, and an additional script is provided to export the data to a CSV file when the server is terminated.

---

## Features

- Web-based form to submit roll numbers.
- Ensures unique roll numbers and IP addresses.
- Prevents duplicate submissions from the same IP.
- Stores submissions in an SQLite database.
- Exports the database to a CSV file.

---

## Prerequisites

Ensure you have the following installed:

- Python 3.7 or higher
- Flask
- Flask-SQLAlchemy

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/roll-number-submission.git
   cd roll-number-submission
   ```

2. Install the required dependencies:
   ```bash
   pip install flask flask-sqlalchemy
   ```

3. Set up the directory structure:
   ```
   project/
   ├── app.py                # Flask server
   ├── export_to_csv.py      # Database export script
   ├── database.db           # SQLite database (auto-created)
   ├── templates/            # HTML templates
       └── index.html        # Frontend form
   ```

---

## Usage

### 1. Run the Server

Start the Flask application:

```bash
python server.py
```

The server will start at `http://127.0.0.1:8080`.

To make it accessible on your local network, modify the `server.py` file:
```python
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
```
Access the app on your local network at `http://<your-local-ip>:8080`.

### 2. Submit Roll Numbers

Open the application in your browser, enter a roll number, and submit. Duplicate roll numbers or submissions from the same IP address are rejected with an error message.

### 3. Export Data

After stopping the server, run the `export_to_csv.py` script to export the database to a CSV file:

```bash
python export_to_csv.py
```

The exported data will be saved to `roll_numbers_export.csv` in the project directory.

---

## File Descriptions

### 1. `app.py`
The main Flask application that handles:
- Displaying the form
- Validating and storing submissions
- Preventing duplicate submissions
- Displaying the list of submitted roll numbers

### 2. `export_to_csv.py`
A script to export the SQLite database table to a CSV file.

### 3. `templates/index.html`
The HTML template for the roll number submission form.

### 4. `database.db`
The SQLite database file (auto-created).

---

## Example Outputs

### Submitted Roll Numbers

```json
[
    "12345",
    "67890"
]
```

### CSV File

```csv
Roll Number,IP Address
12345,192.168.1.10
67890,192.168.1.11
```

---

## Contributing

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Create a pull request.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.
