from flask import Flask, request, jsonify
from password_generator import PasswordGenerator

app = Flask(__name__)

@app.route('/generate-password', methods=['POST'])
def generate_password():
    """
    API endpoint for generating a password.
    
    Expected JSON input:
    {
        "length": 12,
        "use_uppercase": true,
        "use_lowercase": true,
        "use_digits": true,
        "use_special": true
    }
    
    :return: JSON response containing the generated password or an error message.
    """
    data = request.get_json()

    try:
        # Create a PasswordGenerator instance with user input
        generator = PasswordGenerator(
            length=data.get('length', 12),
            use_uppercase=data.get('use_uppercase', True),
            use_lowercase=data.get('use_lowercase', True),
            use_digits=data.get('use_digits', True),
            use_special=data.get('use_special', True)
        )

        # Validate input
        if not generator.validate_input():
            return jsonify({"error": "Invalid input. Password length must be between 8 and 64, and at least one character set must be selected."}), 400

        # Generate password
        password = generator.generate_password()
        return jsonify({"password": password}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)