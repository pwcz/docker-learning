import flask

api = flask.Flask(__name__)


@api.route('/', methods=['GET'])
def home():
    return "<h1>Test API</h1>"


@api.route("/power/<int:number>")
def power(number):
    return str(number**2)
