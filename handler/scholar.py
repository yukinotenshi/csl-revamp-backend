from flask import jsonify, request
from model import Scholar

from middleware.auth import AuthMiddleware


def all_scholar():
    scholars = Scholar.select()
    result = [s.to_dict() for s in scholars]

    return jsonify({
        'message': 'OK',
        'result': result
    })


def get_scholar(id):
    scholar = Scholar.get_or_none(Scholar.id == id)
    if scholar:
        return jsonify({
            'message': 'OK',
            'result': scholar.to_dict()
        })
    else:
        return jsonify({
            'message': 'ERROR',
            'result': None
        }), 404


def update_scholar(id):
    scholar = Scholar.get_or_none(Scholar.id == id)
    if not scholar:
        return jsonify({
            'message': 'ERROR',
            'result': None
        }), 404

    scholar.name = request.json.get('name')
    scholar.university = request.json.get('university')
    scholar.description = request.json.get('description')
    scholar.image = request.json.get('image')
    scholar.batch = request.json.get('batch')
    scholar.cv = request.json.get('cv')
    scholar.linkedin = request.json.get('linkedin')
    scholar.save()

    return jsonify({
        'message': 'OK',
        'result': scholar
    })


def delete_scholar(id):
    scholar = Scholar.get_or_none(Scholar.id == id)
    if not scholar:
        return jsonify({
            'message': 'ERROR',
            'result': None
        }), 404

    scholar.delete_instance()
    return jsonify({
        'message': 'OK',
        'result': None
    })


routes = {
    '/all': ('GET', all_scholar),
    '/<id>': ('GET', get_scholar),
    '/delete/<id>': ('POST', AuthMiddleware(delete_scholar)),
    '/update/<id>': ('POST', AuthMiddleware(update_scholar))
}