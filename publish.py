from pubsub_queue import QueuePublisher

project_id = "n2b-brasil-production"
topic_name = "test-topic"

q = QueuePublisher(project_id, topic_name)

messages = []

for i in range(10):
    messages.append("message {}".format(i))

q.publish(messages)