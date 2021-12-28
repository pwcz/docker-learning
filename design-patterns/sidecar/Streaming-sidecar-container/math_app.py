import flask
import logging
from flask import has_request_context, request

LOGS_PATH = "flask.log"
api = flask.Flask(__name__)


class RequestFormatter(logging.Formatter):
    def format(self, record):
        if has_request_context():
            record.url = request.url
            record.remote_addr = request.remote_addr
        else:
            record.url = None
            record.remote_addr = None

        return super().format(record)


@api.before_first_request
def configure_logger():
    handler = logging.FileHandler(LOGS_PATH)
    handler.setLevel(logging.DEBUG)
    formatter = RequestFormatter(
        '[%(asctime)s] %(remote_addr)s requested %(url)s '
        '%(levelname)s in %(module)s: %(message)s'
    )
    handler.setFormatter(formatter)
    api.logger.setLevel(logging.DEBUG)
    api.logger.handlers = []
    api.logger.propagate = False
    api.logger.addHandler(handler)


@api.route('/', methods=['GET'])
def home():
    api.logger.info("Main page")
    return "<h1>Test API</h1>"


@api.route("/power/<int:number>")
def power(number):
    api.logger.info(f"call:  power({number})")
    return str(number**2)


@api.errorhandler(404)
def page_not_found(exc):
    api.logger.info(exc)
    return "Page not found."
