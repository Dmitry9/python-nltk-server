from flask import Flask, jsonify, request
import subprocess
import json

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter

app = Flask(__name__)

@app.route('/')
def index():
    return 'ok'

@app.route('/postag')
def postag():
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

@app.route('/transcript')
def transcript():
    videoid = request.args.get('videoid', '')
    formatter = JSONFormatter()
    transcript = YouTubeTranscriptApi.get_transcript(videoid, proxies={"https": "https://brd-customer-hl_9f5a0152-zone-data_center:i23vcr837xxg@brd.superproxy.io:22225"})
    return formatter.format_transcript(transcript)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
