from flask import Flask
from statuschecker import get_health_status



app = Flask(__name__)


@app.route('/health')
def check_health():
    return get_health_status();


if __name__ == '__main__':
    app.run(host='0.0.0.0')

