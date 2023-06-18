import time
from flask import Flask, jsonify

app = Flask(__name__)


def get_root_info():
    version = "0.1.0"
    current_date = int(time.time())
    is_kubernetes = False  # Set this value based on your Kubernetes environment

    response = {
        "version": version,
        "date": current_date,
        "kubernetes": is_kubernetes
    }

    return jsonify(response)
