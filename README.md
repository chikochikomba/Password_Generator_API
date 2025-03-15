# Password Generator Application

A secure password generator application built with Python and Flask. This application generates cryptographically secure passwords and exposes an API for integration with other systems.

## Features
- Generates passwords with customizable length and character sets.
- Uses the `secrets` module for secure random number generation.
- Exposes a REST API for easy integration.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/password-generator-app.git

2. Navigate to the project directory:
   cd password-generator-app

3. Install Dependencies :
   pip isntall -r requirements.txt

4. Run the Application:
   python app.py

--- USAGE ---

-> Send a post request to http://localhost:5000/generate-password with the following JSON input:
  
  {
  "length": 12,
  "use_uppercase": true,
  "use_lowercase": true,
  "use_digits": true,
  "use_special": true
  }

-> The API will return a JSON response withthe generated password:
{
  "password": "aB3$fG7@kL9!"
}




![api response with password](https://github.com/user-attachments/assets/b552dc74-3015-4139-a1f6-6f8f9e16d9ca)


![error handling](https://github.com/user-attachments/assets/7641c3e9-c65a-43ff-8f64-67ee9f5b8dd1)






![Python](https://img.shields.io/badge/python-3.10-blue)
![Flask](https://img.shields.io/badge/flask-2.0-green)
