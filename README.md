Project Overview

This project demonstrates the use of Regular Expressions (Regex) in Python to extract and categorize specific data types from a given string. The script is designed to handle various formats for email addresses, phone numbers, credit card numbers, time, and HTML tags, providing a foundational tool for data validation and parsing tasks.

Features

Email Address Validation: Matches standard email formats like user@example.com.

Phone Number Validation: Supports various formats like (123) 456-7890 and 123-456-7890.

Credit Card Number Validation: Recognizes common 16-digit credit card number formats.

Time Recognition: Matches both 24-hour and 12-hour time formats.

HTML Tag Extraction: Identifies HTML tags, including those with attributes.

Setup and Usage

Clone the Repository:

Bash:
git clone https://github.com/Ikennaonugha/alu_regex-data-extraction-Ikennaonugha.git
cd alu_regex-data-extraction-Ikennaonugha
Run the Script:
The script requires Python 3.x. No external libraries are needed, as the re module is built-in.
python main.py
Expected Output:
The script will print the categorized data found in the sample text.

--- Email Addresses ---
- support@example.com
- user.name@company.co.uk
...

Code Documentation:
extract_and_categorize_data(text): A function that takes a string and returns a dictionary of extracted data. It uses a dictionary of regular expressions to define the search patterns.
