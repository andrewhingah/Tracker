from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/maintenances')
def get_all_maintenances_reqs():
  return jsonify(user_requests)


if __name__ == "__main__":
    app.run()