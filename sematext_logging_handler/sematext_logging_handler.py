import logging
import logging.handlers
import json
import os
import traceback
from io import StringIO


class SematextHandler(logging.handlers.SocketHandler):
    def __init__(self, host: str, logsene_app_token) -> None:
        super().__init__(host, 12201)
        self.logsene_app_token = logsene_app_token

    def makePickle(self, record):
        record_dict = {
            "logsene-app-token": self.logsene_app_token,
            "severity": record.levelname,
            "message": record.getMessage(),
            "funcName": record.funcName,
            "pathname": record.pathname,
            "lineno": record.lineno,
            "logger": record.name,
            "thread": record.thread,
        }
        container = os.environ.get("DOCKER_CONTAINER", None)
        if container is not None:
            record_dict["container"] = container
        if record.exc_info:
            exception_str = StringIO()
            traceback.print_exception(
                type(e), e, e.__traceback__, file=exception_str)
            record_dict["exc_backtrace"] = exception_str.getvalue()
            record_dict["exc_name"] = type(e).__name__
        return (json.dumps(record_dict, default=str) + '\n').encode('utf-8')
