from flask import Flask, jsonify
from flask_cors import CORS  # flask-corsをインポート
from models import db, SpeedTestResult

app = Flask(__name__)
CORS(app)  # CORSをFlaskアプリケーションに適用

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///speedtest_results.db'
db.init_app(app)

@app.route('/results', methods=['GET'])
def get_speedtest_results():
    results = SpeedTestResult.query.all()
    return jsonify([{
        'id': result.id,
        'latency': result.latency,
        'jitter': result.jitter,
        'down_100kbps': result.down_100kbps,
        'down_1mbps': result.down_1mbps,
        'down_10mbps': result.down_10mbps,
        'down_25mbps': result.down_25mbps,
        'up_100kbps': result.up_100kbps,
        'up_1mbps': result.up_1mbps,
        'up_10mbps': result.up_10mbps,
        'percentile_down': result.percentile_down,
        'percentile_up': result.percentile_up,
        'timestamp': result.timestamp
    } for result in results])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # 初回実行時にテーブル作成
    app.run(debug=True)
