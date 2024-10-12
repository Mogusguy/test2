from flask import Flask, render_template, request, redirect, jsonify
import random
import json
import os

app = Flask(test)

# Function to load names from the JSON file
def load_names():
    if os.path.exists("names.json"):
        with open("names.json", "r") as f:
            return json.load(f)
    return reset_names()  # Reset if the file doesn't exist

# Function to save names to the JSON file
def save_names(names):
    with open("names.json", "w") as f:
        json.dump(names, f)

# Function to reset names to the default list
def reset_names():
    default_names = ["Liam", "Noah", "Oliver", "Elijah", "James",
                     "William", "Benjamin", "Lucas", "Henry", "Alexander"]
    save_names(default_names)
    return default_names

# Route to render the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route to generate a random name
@app.route('/generate', methods=['POST'])
def generate_name():
    names = load_names()
    if names:
        return jsonify({"name": random.choice(names)})
    else:
        return jsonify({"error": "No names available!"})

# Route to add a new name
@app.route('/add', methods=['POST'])
def add_name():
    new_name = request.form['name'].strip()
    if new_name:
        names = load_names()
        if new_name not in names:
            names.append(new_name)
            save_names(names)
            return redirect('/')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
