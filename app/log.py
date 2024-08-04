import pendulum
import logging
from pythonjsonlogger import jsonlogger

logger = logging.getLogger(__name__)


# Same as avalon sdk
class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        for col in [
            "name",
            "processName",
            "filename",
            "funcName",
            "lineno",
            "module",
            "threadName",
        ]:
            log_record[col] = getattr(record, col)
        if not log_record.get("timestamp"):
            # this doesn't use record.created, so it is slightly off
            now = pendulum.now("Asia/Bangkok").isoformat()
            log_record["timestamp"] = now
        if log_record.get("level"):
            log_record["level"] = log_record["level"].upper()
        else:
            log_record["level"] = record.levelname
        # Mapping to GCP logging keywords
        log_record["time"] = log_record["timestamp"]
        log_record["severity"] = log_record["level"]


def log_request(request: str):
    logger.info({"message": "user_query", "query": request})

