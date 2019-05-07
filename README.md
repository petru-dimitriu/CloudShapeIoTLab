# CloudShapeIoT
The workshop is about developing an analytics application based on IoT data. 

This is done by firstly creating a digital IoT Shadow of a physical connected device and then by adding an AWS IoT rule which will forward all the messages to a AWS Lambda that will put the data into Elasticsearch. Based on the data indexed in Elasticsearch, Kibana can be used to search and display the data in dashboard.

The way to send the telemetry data to AWS is done through a custom script at the beginning. Later in the lab this is replaced by employing an existing IoT simulator solution which will be deployed as a prerequisite.
