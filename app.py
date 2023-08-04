from flask import Flask

# Create a Flask app
app = Flask(__name__)

# Define a route to handle incoming HTTP requests
@app.route('/')
def hello():
    return 'Hello, World! Azure Web App'

# Start the Flask development server listening on port 8000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
