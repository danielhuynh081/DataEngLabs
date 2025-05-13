from google.cloud import pubsub_v1
from concurrent.futures import TimeoutError
import time

project_id = "cs410-lab"
subscription_id = "transport-sub"
timeout = 60.0

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(project_id, subscription_id)

message_counter = 0
start_time = time.time()

def callback(message: pubsub_v1.subscriber.message.Message) -> None:
    global message_counter
    message.ack()
    message_counter += 1

    if message_counter % 10000 == 0:
        print(f" Received {message_counter} messages so far...")

streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
print(f"👂 Listening for messages on {subscription_path}...\n")

with subscriber:
    try:
        streaming_pull_future.result(timeout=timeout)
    except TimeoutError:
        end_time = time.time()
        streaming_pull_future.cancel()

        print(f"\n Finished receiving messages.")
        print(f" Total messages received: {message_counter}")
        print(f" Time taken to receive: {end_time - start_time:.2f} seconds")
