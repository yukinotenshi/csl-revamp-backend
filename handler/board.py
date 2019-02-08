from flask import jsonify, request
from model import Board

from middleware.auth import AuthMiddleware


def all_board():
    boards = Board.select()
    result = [s.to_dict() for s in boards]

    return jsonify({
        'message': 'OK',
        'result': result
    })


def get_board(id):
    board = Board.get_or_none(Board.id == id)
    if board:
        return jsonify({
            'message': 'OK',
            'result': board.to_dict()
        })
    else:
        return jsonify({
            'message': 'ERROR',
            'result': None
        }), 404


def update_board(id):
    board = Board.get_or_none(Board.id == id)
    if not board:
        return jsonify({
            'message': 'ERROR',
            'result': None
        }), 404

    board.name = request.json.get('name')
    board.description = request.json.get('description')
    board.image = request.json.get('image')
    board.linkedin = request.json.get('linkedin')
    board.position = request.json.get('position')
    board.save()

    return jsonify({
        'message': 'OK',
        'result': board
    })


def delete_board(id):
    board = Board.get_or_none(Board.id == id)
    if not board:
        return jsonify({
            'message': 'ERROR',
            'result': None
        }), 404

    board.delete_instance()
    return jsonify({
        'message': 'OK',
        'result': None
    })


routes = {
    '/all': ('GET', all_board),
    '/<id>': ('GET', get_board),
    '/delete/<id>': ('POST', AuthMiddleware(delete_board)),
    '/update/<id>': ('POST', AuthMiddleware(update_board))
}