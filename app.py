import random
from flask import (Flask, request)

app = Flask(__name__)


@app.route("/random/choice")
def _choice():
    values = request.args.getlist('value')

    if not values:
        return {
            'status': 400,
            'detail': "'value' parameters must be specified"
        }, 400

    return {'value': random.choice(values)}


@app.route("/swagger.yaml")
def _swagger():
    return app.send_static_file('swagger.yaml')


if __name__ == "__main__":
    app.run()
