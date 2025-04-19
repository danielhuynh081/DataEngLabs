from google.cloud import pubsub_v1
import json
import time

# Set up your topic info
project_id = "cs410-lab"
topic_id = "transport-lab"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

# Load bcsample.json
with open('bcsample.json', 'r') as f:
    data = json.load(f)

message_count = 0
start_time = time.time()

# Send each record (for each vehicle)
for vehicle_id, records in data.items():
    for record in records:
        message_json = json.dumps(record)
        message_bytes = message_json.encode('utf-8')

        publisher.publish(topic_path, data=message_bytes)
        message_count += 1

end_time = time.time()

print(f"\n Published {message_count} messages.")
print(f" Time taken to publish: {end_time - start_time:.2f} seconds")
