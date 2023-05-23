from flask import Flask, request, jsonify
from reward_calculator import RewardCalculator
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, resources={r"/calculate_rewards": {"origins": "*"}})

@app.route('/')
def index():
    return 'Welcome to the Capital One Rewards API'

@app.route('/calculate_rewards', methods=['POST'])
def calculate_rewards():
    transactions = request.json.get('transactions', [])
    result = RewardCalculator(transactions).max_points_for_month()

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
