import os
from flask import Flask, request, jsonify
import datetime
import pandas as pd

app = Flask(__name__)

dateparse = lambda x: pd.datetime.strptime(x, '%d/%m/%Y')
df = pd.read_csv('conversion.csv', header=0, index_col=0, parse_dates=['Date'], date_parser=dateparse)


@app.errorhandler(400)
def bad_request(e):
    return jsonify({"error": "Bad request in parameter. Please provide at least a valid year or a valid month with year."}), 400


@app.route('/currency_gbp/all')
def currency_all():
    return df.to_json(date_format='iso')


# @app.route('/currency_gbp')
# def currency():
#     query_parameters = request.args
#
#     date = query_parameters.get('date')
#     month = query_parameters.get('month')
#     year = query_parameters.get('year')
#
#
#     if year is None or (month is None and year is None):
#         return bad_request(400)
#
#     if not 2018 <= int(year) <= 2020 and not 1 <= int(month) <= 12:
#         return bad_request(400)
#
#
#
#     if not 2018 <= int(year) <= 2020 and not 1 <= int(month) <= 12 and not 1 <= int(date) <= 31:
#         return bad_request(400)
#
#     if year and month and date:
#         return df[int(datetime.datetime(int(year), int(month), int(date), 0, 0).timestamp())].to_json(date_format='iso')
#     else:
#         return df.to_json(date_format='iso')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
