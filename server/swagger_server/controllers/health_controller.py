import connexion
import six


def health_check():
    """Check health status

    Check the health status of the application
    """
    return 'application health!'
