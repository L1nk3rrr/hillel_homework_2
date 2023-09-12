import logging

from flask import Flask, make_response, render_template, request

import utils

app = Flask(__name__)
logger = logging.Logger(__name__)


@app.route("/requrements")
def get_requirements():
    return make_response('</br>'.join(utils.get_data_from_requirements()))


@app.route("/requrements_beauty")
def get_requirements_beauty():
    return render_template('requirements.html', requirements=utils.get_data_from_requirements())


@app.route("/generate-users/")
def generate_users():
    try:
        qty_of_users = int(request.args.get('qty', 100))
    except TypeError as e:
        logger.error("Bad type for qty was passed")
        return make_response('', 404)
    return make_response('</br>'.join(utils.get_fake_users(qty_of_users)))


@app.route("/mean/")
def get_measurements_csv():
    rounding_factor_str = request.args.get('rounding', '2')
    try:
        rounding_factor = int(rounding_factor_str)
        if rounding_factor < 0:
            raise ValueError("Rounding factor must be a non-negative integer.")
    except ValueError as e:
        logger.error(e)
        return make_response("Invalid rounding factor. Please provide a non-negative integer.")

    avg_height, avg_weight = utils.get_avg_data_from_csv('hw.csv')
    return make_response(
        f"Average Height - {avg_height:.{rounding_factor}f}</br>"
        f"Average Weight - {avg_weight:.{rounding_factor}f}"
    )


if __name__ == "__main__":
    app.run()
