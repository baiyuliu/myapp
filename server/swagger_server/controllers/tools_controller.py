import ipaddress
import logging
import os
import connexion
import socket
import mysql.connector
from flask import jsonify, request
from swagger_server.models.handler_validate_ip_request import HandlerValidateIPRequest  # noqa: E501
#import six
#from swagger_server.models.handler_validate_ip_response import HandlerValidateIPResponse  # noqa: E501
#from swagger_server.models.model_query import ModelQuery  # noqa: E501
#from swagger_server.models.utils_http_error import UtilsHTTPError  # noqa: E501
#from swagger_server import util






logging.basicConfig(filename='app.log', level=logging.INFO)


# MySQL configuration
mysql_host = os.getenv('MYSQL_HOST', 'database-service')
mysql_port = os.getenv('MYSQL_PORT', 3306)
mysql_user = os.getenv('MYSQL_USER')
mysql_password = os.getenv('MYSQL_PASSWORD')
mysql_database = os.getenv('MYSQL_DATABASE', 'lookup_db')


def lookup_domain(domain):  # noqa: E501
    """Lookup domain

    Lookup domain and return all IPv4 addresses # noqa: E501

    :param domain: Domain name
    :type domain: str

    :rtype: ModelQuery
    """
    

    domain = request.args.get('domain')


    # Perform the logic to resolve IPv4 addresses for the domain

    # Log the successful query and result in the MySQL database
    try:
        # Resolve IPv4 addresses for the domain
        ipv4_addresses = resolve_ipv4_addresses(domain)
        logging.info("resolve domain: %s", domain)
        # Log the successful query and result in the MySQL database
        log_query_result(domain, ipv4_addresses)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify({'ipv4_addresses': ipv4_addresses})  # Replace ipv4_addresses with your resolved IPv4 addresses




def resolve_ipv4_addresses(domain):
    # Use socket.getaddrinfo to resolve the domain's IP addresses
    # Filter the results to include only IPv4 addresses
    results = socket.getaddrinfo(domain, None, socket.AF_INET)
    ipv4_addresses = [result[4][0] for result in results if result[0] == socket.AF_INET]
    return ipv4_addresses

def log_query_result(domain, ipv4_addresses):
    try:
        connection = mysql.connector.connect(
            host=mysql_host,
            port=mysql_port,
            user=mysql_user,
            password=mysql_password,
            database=mysql_database
        )
        cursor = connection.cursor()
        insert_query = "INSERT INTO lookup_logs (domain, result) VALUES (%s, %s)"
        data = (domain, ', '.join(ipv4_addresses))
        cursor.execute(insert_query, data)
        connection.commit()
        cursor.close()
        connection.close()
        logging.info("log domain query to DB: %s %s", domain,ipv4_addresses)
    except mysql.connector.Error as error:
        raise Exception("Error logging query result in MySQL: " + str(error))




def validate_ip(body):  # noqa: E501
    """Simple IP validation

    Simple IP valication # noqa: E501

    :param body: IP to validate
    :type body: dict | bytes

    :rtype: HandlerValidateIPResponse
    """

    if connexion.request.is_json:
        body = HandlerValidateIPRequest.from_dict(connexion.request.get_json())  # noqa: E501
        
    address = request.json.get('address')
    try:
        ipaddress.IPv4Address(address)
        is_valid = True
        logging.info("ipaddress is validated: %s", address)
    except ipaddress.AddressValueError:
        is_valid = False
        logging.error("error ipaddress: %s", address)

    return jsonify({'valid': is_valid})
    #return 'do some magic!'



def get_latest_queries():
    
    # Connect to MySQL database
    try:
        #print("!!!!!!!!mysql:",mysql_host,mysql_port,mysql_user,mysql_password,mysql_database)
        connection = mysql.connector.connect(
            host=mysql_host,
            port=mysql_port,
            user=mysql_user,
            password=mysql_password,
            database=mysql_database
        )
        cursor = connection.cursor()
        query = "SELECT domain, result FROM lookup_logs ORDER BY created_at DESC LIMIT 20"
        #query = "SELECT * FROM lookup_logs ORDER BY created_at DESC LIMIT 20"
        cursor.execute(query)

        # Fetch all rows
        rows = cursor.fetchall()
        cursor.close()
        connection.close()
    except mysql.connector.Error as error:
        logging.error("Error logging query result in MySQL: %s", str(error))
        raise Exception("Error logging query result in MySQL: " + str(error))
    for query in rows:
        logging.info("Query: %s", query)
    
    # Return the retrieved queries
    return rows

