project_id = "n2b-brasil-production"
subscription_name = "test-topic-subscription"
topic_name = "test-topic"

from pubsub_queue import QueueConsumer

q = QueueConsumer(project_id, subscription_name, topic_name)

def my_worker(message):
    print(list(message))

q.work(my_worker, acknowledge_before=False)