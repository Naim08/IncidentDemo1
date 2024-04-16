from flask import Flask, jsonify, render_template, redirect, url_for
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://6da94bd27d7616efad7249447dee97b5@o4507090108284928.ingest.us.sentry.io/4507090114183168",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/error')
def trigger_error():
    # This line will intentionally raise a division by zero error
    division_by_zero = 1 / 0
    return str(division_by_zero)

if __name__ == '__main__':
    app.run(debug=False)

