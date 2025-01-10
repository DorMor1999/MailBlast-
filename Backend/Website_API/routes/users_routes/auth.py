from flask_restful import Resource
from flask import request
from utils.errors.input.error_input_string import create_error_string

class Auth(Resource):
    def post(self):
        """
        Handle both user signup and login depending on the 'action' query parameter,
        with 'username' and 'password' provided in the request body.

        Supported actions:
        - 'signup': Registers a new user.
        - 'login': Authenticates an existing user.

        Returns:
        - 201: If signup is successful, returns a success message with user details.
        - 200: If login is successful, returns a success message with user details.
        - 400: If the 'action' parameter is missing or invalid, or if the required input fields are missing or invalid.
        - 500: If an unexpected error occurs during the process.
        """
        
        try:
            # Retrieve and validate the 'action' query parameter
            action = request.args.get("action")
            if not action:
                return {"message": "Missing 'action' query parameter."}, 400

            # Parse JSON data from the body and validate
            data = request.get_json()
            if not data:
                return {"message": "Invalid data. Data is required!"}, 400

            # Handle the appropriate action
            if action == "signup":
                return self.handle_signup(data)
            elif action == "login":
                return self.handle_login(data)
            else:
                return {"message": "Invalid action. Use 'signup' or 'login'."}, 400

        except Exception as e:
            # Return a generic 500 Internal Server Error response
            return {"message": "An unexpected error occurred. Please try again later."}, 500


    def validate_inputs(self, fields):
        """Helper method to validate user inputs."""
        return create_error_string(fields)


    def handle_signup(self, data):
        """Handle user signup logic."""
        fields = [
            {"input_type": "first name", "input": data.get("first_name")},
            {"input_type": "last name", "input": data.get("last_name")},
            {"input_type": "email", "input": data.get("email")},
            {"input_type": "password", "input": data.get("password")}
        ]
        
        inputs_error = self.validate_inputs(fields)
        if inputs_error:
            return {"message": inputs_error}, 400
        
        # Placeholder for saving the user to the database
        return {"message": "User signed up", "user": {"email": data["email"]}}, 201


    def handle_login(self, data):
        """Handle user login logic."""
        fields = [
            {"input_type": "email", "input": data.get("email")},
            {"input_type": "password", "input": data.get("password")}
        ]
        
        inputs_error = self.validate_inputs(fields)
        if inputs_error:
            return {"message": inputs_error}, 400
        
        # Placeholder for verifying user credentials
        return {"message": "User logged in", "user": {"email": data["email"]}}, 200