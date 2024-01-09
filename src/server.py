from flask import Flask, jsonify, request
import subprocess
import json

app = Flask(__name__)

@app.route('/')
def index():
    # Get the 'input_string' query parameter from the request
    input_string = request.args.get('input_string', '')

    # Run your Python script with the input string and capture its output
    script_output = subprocess.check_output(['python', './pos.py', input_string], text=True)

    # Convert the list of tuples to JSON
    # 1. Remove extra quotes (if present) around keys and values
    clean_string = script_output.replace("\n", "").replace("'", '"')  # Replace single quotes with double quotes

    # 2. Parse the string as a list of dictionaries
    data = json.loads(clean_string)

    # Return the JSON response
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
