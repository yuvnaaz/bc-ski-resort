from flask import Flask, render_template_string
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # This enables CORS for your app

@app.route('/')
def index():
    # Read the combined data from the JSON file
    combined_data = read_combined_data_from_json("ski_resorts.json")
    return render_template_string("<pre>{{ combined_data }}</pre>", combined_data=combined_data)

def read_combined_data_from_json(file_path):
    combined_data = ""
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            combined_data = json.dumps(data, indent=4)
    except FileNotFoundError:
        combined_data = "JSON data file not found."
    return combined_data

if __name__ == '__main__':
    app.run(debug=True)
