# Days Lived Calculator

A Flask-based web application that calculates how many days a person has lived, based on their date of birth.

## Features
- Accepts a name and date of birth input from the user.
- Calculates the number of days the user has lived since their birthdate.
- Displays the result on a new page.
- Validates the date input to ensure it's in the correct format (YYYY-MM-DD).

## Requirements
- Python 3.x
- Flask

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Dev-Coder20/Days_Lived_Calculator_App.git
   cd Days_Lived_Calculator_App
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask app:
   ```bash
   python app.py
   ```

4. Open your browser and go to `http://127.0.0.1:5000/` to start using the app.

## Files
- `app.py`: The main Flask application that handles the backend logic.
- `templates/`: Contains the HTML files (`index.html` and `result.html`) for rendering the pages.
- `static/`: Contains the CSS (`style.css`) and JavaScript (`script.js`) files for styling and client-side behavior.
