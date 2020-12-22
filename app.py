from flask import Flask
from flask_apscheduler import APScheduler


# config scheduling class
from statuschecker import get_health_status


class Config(object):
    JOBS = [
        {
            'id': 'check_health',
            'func': 'app:check_health',
            'trigger': 'interval',
            'seconds': 1800
        }
    ]

    SCHEDULER_API_ENABLED = True


# function triggered every 30 minutes
def check_health():
    return get_health_status();


# flask startup
app = Flask(__name__)
app.config.from_object(Config())


# initiate scheduler
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

if __name__ == '__main__':
    app.run(host='0.0.0.0')



