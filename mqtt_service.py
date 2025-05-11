#!/usr/bin/env python3

import paho.mqtt.client as mqtt
from datetime import datetime
import time
import ssl
import os
import json

# TODO replace TODO with the Thing name from AWS IoT Core
client_id = 'TODO'
# TODO replace the xxxxxx to match your certificate and private key names
cert_filename = 'certs/xxxxxxx-certificate.pem.crt'
private_key_filename = 'certs/xxxxxx-private.pem.key'
ca_filename = 'certs/AmazonRootCA1.pem'

def setup():
    # TODO        
 
def publish_message(payload=None, topic):
    # TODO    

