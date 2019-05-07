#!/usr/bin/env python

import mqtt_service
import time
import json

def execute(no_messages):
	mqtt_service.setup()
	for x in range(no_messages):
  		send_sample_data()
	

def send_sample_data():	
	# TODO	
	# mqtt_service.publish_message(payload, topic)
		
if __name__ == '__main__':
	try:        
		execute(10);
		time.sleep(1)
	except KeyboardInterrupt:
		destory()   
