import re

def extract_and_categorize_data(text):
    """
    Extracts and categorizes data (Emails, Phone Numbers, Credit Card Numbers)
    from a single string using regular expressions.

    Args:
        text (str): The input string to be processed.

    Returns:
        dict: A dictionary containing the categorized extracted data.
    """
    # Define the regex patterns
    patterns = {
        "Email Addresses": r'[\w.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
        "Phone Numbers": r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
        "Credit Card Numbers": r'\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}',
        "HTML tags": r'<([a-zA-Z0-9]+)\s*([^>]*?)>',
        "Time": r'\b(?:2[0-3]|[01]?[0-9]):[0-5][0-9]\b(?:\s*(?:AM|PM))?'
    }
    extracted_data = {}

    # Find all matches for each pattern
    for category, pattern in patterns.items():
        matches = re.findall(pattern, text)
        if matches:
            extracted_data[category] = matches

    return extracted_data

def print_categorized_data(data):
    """
    Prints the categorized data in a user-friendly format.
    """
    if not data:
        print("No valid patterns found in the text.")
        return

    for category, items in data.items():
        print(f"--- {category} ---")
        for item in items:
            print(f"- {item}")
        print()

# Example usage
test_text = """
For any inquiries, please contact us at support@example.com or reach out to our team lead, jane.doe-smith@company.co.uk. Our office hours are from 09:00 to 17:30. We'll also be hosting a Q&A session at 3:00 PM.

You can reach our main office at (123) 456-7890 or our secondary line at 987-654-3210. You may also dial 555.123.4567 for direct assistance. We accept all major credit cards. Please enter the number 1234 5678 9012 3456 or 9876-5432-1098-7654 at checkout.

The homepage features a <header> with a company logo. The content is inside a <div class="main-content"> tag. You will also see a <p> tag for the introductory paragraph and a list item using the <li> tag.
"""

found_data = extract_and_categorize_data(test_text)
print_categorized_data(found_data)
