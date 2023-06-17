#!/usr/bin/env python3

import connexion
from flask import Flask



from swagger_server import encoder

app = Flask(__name__)
#app.add_url_rule('/health', 'health', health)  # Add the health endpoint
@app.route('/health')
def health():
    # Check the health status of your application here
    # Example:
    health_status = 'healthy'
    return f'Application is {health_status}'

app.run(port=8080)