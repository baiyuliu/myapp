import connexion
import six
from prometheus_client import generate_latest, CollectorRegistry, CONTENT_TYPE_LATEST
from flask import Flask, Response

registry = CollectorRegistry()

def metrics():
    data = generate_latest(registry)
    return Response(data, mimetype=CONTENT_TYPE_LATEST)
