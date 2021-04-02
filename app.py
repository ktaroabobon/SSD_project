import flask

from src.controlers.controler import SSDPredictModel

app = flask.Flask(__name__)


@app.route("/api/predict", methods=["POST"])
def handler():
    response = {
        "success": False,
        "Content-Type": "application/json"
    }
    # ensure an feature was properly uploaded to our endpoint
    if flask.request.method == "POST":
        if flask.request.get_json().get("body"):
            # read feature from json
            data = flask.request.get_json().get("body")

            ssd_model = SSDPredictModel(data.encode())
            response["body"] = ssd_model.predict.decode("utf-8")

            # indicate that the request was a success
            response["success"] = True

    # return the data dictionary as a JSON response
    return flask.jsonify(response)


if __name__ == "__main__":
    app.run()
