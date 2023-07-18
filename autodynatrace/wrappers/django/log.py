import os
import logging
from ...sdk import sdk

auto_log_correlation = os.environ.get("AUTODYNATRACE_AUTOMATIC_LOG_CORRELATION", "False").strip().lower() in (
"true", "1")

def instrument_log():
    old_factory = logging.getLogRecordFactory()

    def record_factory(*args, **kwargs):
        record = old_factory(*args, **kwargs)
        if sdk:
            trace_info = sdk.tracecontext_get_current()
            span_id, trace_id = trace_info.span_id, trace_info.trace_id
            record.span_id = span_id
            record.trace_id = trace_id

        return record

    if auto_log_correlation:
        logging.setLogRecordFactory(record_factory)