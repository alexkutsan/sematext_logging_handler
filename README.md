# Sematext Logging Handler

## SematextHandler

`SematextHandler` is a Python logging handler for sending logs to Sematext Cloud(https://sematext.com). 
It extends the `SocketHandler` from the `logging.handlers` module.
It utilizes sematext Socket Protocols input sources. 

### Installation

You can install the package using pip:

```bash
pip install sematext_logging_handler
```


### Usage

```python
import logging
from sematext_logging_handler import SematextHandler


# Create an instance of SematextHandler
handler = SematextHandler(host='logsene-receiver.sematext.com', logsene_app_token='your_logsene_app_token')

# Create a logger
logger = logging.getLogger('my_logger')
logger.addHandler(handler)

# Log a message
logger.error('This is an error message!')
```

### Configuration

- `host`: The hostname of the Sematext Logsene receiver (european or american cluster)
- `logsene_app_token`: Your Sematext Logsene App Token.


### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Make sure to replace `'your_logsene_app_token'` with your actual Sematext Logsene App Token.

This README provides a brief overview of your package, how to install it, use the `SematextHandler`, and mentions the license. Feel free to expand it further based on your package's features and use cases.