import logging
import connexion
#import six

#from swagger_server.models.model_query import ModelQuery  # noqa: E501
#from swagger_server.models.utils_http_error import UtilsHTTPError  # noqa: E501
#from swagger_server import util
from swagger_server.controllers.tools_controller import get_latest_queries


def queries_history():  # noqa: E501
    """List queries

    List queries # noqa: E501


    :rtype: List[ModelQuery]
    """
    # Call the function to get the latest queries
    logging.basicConfig(filename='queries_history.log', level=logging.INFO)
    latest_queries = get_latest_queries()

    # Print the retrieved queries
    for query in latest_queries:
        logging.info("data: %s", query)
        #domain, ipv4_addresses = query
        domain = query[0]
        ipv4_addresses = query[1]
        logging.info("Domain: %s", domain)
        logging.info("IPv4 Addresses: %s", ipv4_addresses)
        logging.info("---")
    #return domain, ipv4_addresses
    return latest_queries