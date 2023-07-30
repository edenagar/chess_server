from flask import Flask, request, jsonify
import chess_engine

app = Flask(__name__)


@app.route('/chess/next_move', methods=['POST'])
def next_move():
    data = request.get_json()
    board_state = data['board']
    next_move = chess_engine.calculate_next_move(board_state)
    return jsonify({'nextMove': next_move})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
