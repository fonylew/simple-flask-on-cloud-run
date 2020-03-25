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



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
