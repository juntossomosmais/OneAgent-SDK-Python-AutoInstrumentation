import oneagent


def get_messaging_type_by_queue_name(queue_name: str) -> int:
    """Helper function to get queue type by name. If 'VirtualTopic' exists in the destination name
    this queue is a TOPIC type.
    By default the type of queue is QUEUE.
    """
    if "VirtualTopic" in queue_name:
        return oneagent.common.MessagingDestinationType.TOPIC

    return oneagent.common.MessagingDestinationType.QUEUE
