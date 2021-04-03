import flask
import logging

import settings
from controlers.controler import SSDPredictModel

app = flask.Flask(__name__)

log_path = settings.BASE_DIR / "logfiles" / settings.logfile

fh = logging.FileHandler(log_path)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
app.logger.addHandler(fh)


@app.route("/api/predict", methods=["POST"])
def predict():
    app.logger.info({"page": "predict-api", "status": "start"})
    response = {
        "success": False,
        "Content-Type": "application/json"
    }
    # ensure an feature was properly uploaded to our endpoint
    if flask.request.method == "POST":
        if flask.request.get_json().get("body"):
            # read feature from json
            data = flask.request.get_json().get("body")

            app.logger.info({"page": "predict-api", "predict": "start"})
            ssd_model = SSDPredictModel(data.encode())
            app.logger.info({"page": "predict-api", "predict": "success"})
            response["body"] = ssd_model.predict.decode("utf-8")

            # indicate that the request was a success
            response["success"] = True

    # return the data dictionary as a JSON response
    app.logger.info({"page": "predict-api", "status": "success"})
    return flask.jsonify(response)


if __name__ == "__main__":
    app.run()
