from models import db, SpeedTestResult
from cfspeedtest import CloudflareSpeedtest
from apscheduler.schedulers.blocking import BlockingScheduler
from flask import Flask
from datetime import datetime
import schedule
import time

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///speedtest_results.db'
db.init_app(app)

def run_speedtest():
    suite = CloudflareSpeedtest()
    try:
        results = suite.run_all()
    except:
        print("ConnectionError: Speed test failed.")
        return False
    tests = results['tests']
    timestamp = datetime.utcfromtimestamp(tests['latency'][1])
    print(timestamp)
    speedtest_result = SpeedTestResult(
        latency=tests['latency'][0],
        jitter=tests['jitter'][0],
        down_100kbps=tests['100kB_down_bps'][0],
        down_1mbps=tests['1MB_down_bps'][0],
        down_10mbps=tests['10MB_down_bps'][0],
        down_25mbps=tests['25MB_down_bps'][0],
        up_100kbps=tests['100kB_up_bps'][0],
        up_1mbps=tests['1MB_up_bps'][0],
        up_10mbps=tests['10MB_up_bps'][0],
        percentile_down=tests['90th_percentile_down_bps'][0],
        percentile_up=tests['90th_percentile_up_bps'][0],
        timestamp=timestamp
    )

    with app.app_context():
        db.session.add(speedtest_result)
        db.session.commit()

schedule.every(1).minutes.do(run_speedtest)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # 初回実行時にテーブル作成

    while True:
        schedule.run_pending()
        time.sleep(1)
