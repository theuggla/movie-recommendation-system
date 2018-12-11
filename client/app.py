# Serves the client files

# Imports
import os
from flask import Flask, render_template

app = Flask(__name__)

# Return index.html on root
@app.route("/")
def index():
    return render_template('index.html')

# Start server
if __name__ == "__main__":
    app.run(port=os.environ.get('PORT', 3000))
