#!/usr/bin/env python3

import connexion
from swagger_server import encoder
from prometheus_client import generate_latest, CollectorRegistry, CONTENT_TYPE_LATEST
import signal
import sys
import logging
from flask import Flask, request




def main():
    logging.basicConfig(filename='app.log', level=logging.INFO)
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.logger.setLevel(logging.INFO)
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Interview challenge'}, pythonic_params=True)
    
    app.app.before_request(lambda: log_access_info(app.app))

    app.run(port=3000)


def log_access_info(app):
    ip = request.remote_addr
    method = request.method
    url = request.url
    app.logger.info(f"IP: {ip}, Method: {method}, URL: {url}")


def shutdown_handler(signal, frame):
    # Perform cleanup tasks here (if any)
    logging.info("Shutting down gracefully...")
    sys.exit(0)


if __name__ == '__main__':
    signal.signal(signal.SIGTERM, shutdown_handler)
    main()
