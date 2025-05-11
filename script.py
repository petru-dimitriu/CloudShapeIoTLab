#!/usr/bin/env python3

import mqtt_service
import time
import datetime
import uuid
import json
import random

topic = 'connectedcar/telemetry'
# TODO update the no of messages to send
no_messages = 0
def execute(no_messages):
	mqtt_service.setup()
	for x in range(no_messages):
		payload = get_sample_data()
		# TODO use mqtt_service to publish messages

def get_sample_data():
	data = {
		"id": uuid.uuid4(),
		"vin": "3e69833f-e3c6-46a4-b068-054f0288ad19",
		"transmission_gear_position": random.uniform(0, 6),
		"vehicle_speed": random.uniform(0, 200),
		"timestamp": datetime.datetime.utcnow()
	}
	return str(data)

if __name__ == '__main__':
	try:
		execute(no_messages)
		time.sleep(1)
	except KeyboardInterrupt:
		destory()   
