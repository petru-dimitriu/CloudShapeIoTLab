# CloudShapeIoT

The lab is about integrating an IoT device with AWS IoT and get notified by SMS of events coming from the device using Simple Notification Service. 

This is done by firstly creating a digital IoT Shadow of a physical connected device and then by adding an AWS IoT rule, using the AWS IoT Rule engine. This will subscribe to the message events coming from the device and forward them all to a SNS. This SNS topic will have a subscriber which will be an email or phone (reached using an SMS message).

The way to send the telemetry data to AWS is done through a custom that we are going to fill in. This will allow getting more knowledge about AWS IoT and the particularities of the IoT communication and processing, in general.
