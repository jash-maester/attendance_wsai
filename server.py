from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import argparse
from sqlalchemy import Column, DateTime
from datetime import datetime

app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the RollNumber model
class RollNumber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    roll_number = db.Column(db.String(20), unique=True, nullable=False)
    ip_address = db.Column(db.String(30), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime(), unique=False, nullable=False)
    course_code = db.Column(db.String(20), unique=False, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_roll_number():
    roll_number = request.form.get('roll_number')
    ip_address = request.remote_addr  # Get the client's IP address
    course_id = request.form.get('course_id') # get the course id

    if not roll_number:
        return jsonify({"error": "Roll number is required"}), 400

    # Check if the IP address has already submitted
    if RollNumber.query.filter_by(ip_address=ip_address).first():
        return jsonify({"error": "You have already submitted a roll number"}), 403

    # Check if the roll number is already submitted
    if RollNumber.query.filter_by(roll_number=roll_number).first():
        return jsonify({"error": "This roll number has already been submitted"}), 403

    # Save the roll number, IP address and timestamp to the database
    ts = datetime.now()
    new_roll_number = RollNumber(roll_number=roll_number, ip_address=ip_address, 
                                 timestamp = ts, course_code = course_id)
    db.session.add(new_roll_number)
    db.session.commit()

    return jsonify({"message": "Roll number submitted successfully", "roll_number": roll_number}), 200

@app.route('/rollnumbers', methods=['GET'])
def get_roll_numbers():
    # Fetch all roll numbers from the database
    roll_numbers = RollNumber.query.all()
    return jsonify([roll.roll_number for roll in roll_numbers])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", help="server port to bind (default is 8080)", required=False, default=8080, type=int)
    args = parser.parse_args()

    app.run(host='0.0.0.0', port=args.port, debug=True)
