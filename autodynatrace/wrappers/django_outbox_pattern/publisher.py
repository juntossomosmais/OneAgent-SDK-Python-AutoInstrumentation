import oneagent
import wrapt

from ...log import logger
from ...sdk import sdk
from django.conf import settings
from django_outbox_pattern.producers import Producer


def instrument_publisher():
    def on_send_message(wrapped, instance, args, kwargs):
        try:
            host, port = settings.DJANGO_OUTBOX_PATTERN["DEFAULT_STOMP_HOST_AND_PORTS"][0]
            destination = kwargs.get("destination")
            headers = kwargs.get("headers", {})

        except Exception as e:
            logger.warn("autodynatrace - Could not trace Publisher.send: {}".format(e))
            return wrapped(**kwargs)

        messaging_system = sdk.create_messaging_system_info(
            oneagent.common.MessagingVendor.RABBIT_MQ,
            destination,
            oneagent.common.MessagingDestinationType.QUEUE,
            oneagent.sdk.Channel(oneagent.sdk.ChannelType.TCP_IP, "{}:{}".format(host, port)),
        )

        with messaging_system:
            with sdk.trace_outgoing_message(messaging_system) as outgoing_message:
                outgoing_message.set_correlation_id(headers.get("correlation-id"))
                tag = outgoing_message.outgoing_dynatrace_string_tag.decode("utf-8")
                headers[oneagent.common.DYNATRACE_MESSAGE_PROPERTY_NAME] = tag
                logger.debug(
                    f"autodynatrace - Tracing Outgoing RabbitMQ host={host}, port={port}, routing_key={destination}, "
                    f"tag={tag}, headers={headers}"
                )
                return wrapped(**kwargs)

    wrapt.wrap_function_wrapper(Producer, "_send_with_retry", on_send_message)
