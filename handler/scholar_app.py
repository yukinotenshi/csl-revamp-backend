from flask import jsonify, request
from model import ScholarApp

from middleware.auth import AuthMiddleware


def submit_scholar_app():
    name = request.json.get('name')
    email = request.json.get('email')
    university = request.json.get('university')
    address = request.json.get('address')

    scholar_app = ScholarApp(
        name=name,
        email=email,
        university=university,
        address=address
    )

    try:
        scholar_app.save()
    except Exception as e:
        return jsonify({
            'message': 'ERROR',
            'result': str(e)
        }), 404

    return jsonify({
        'message': 'OK',
        'result': scholar_app.to_dict()
    })


def all_scholar_app():
    scholar_apps = ScholarApp.select()
    result = [s.to_dict() for s in scholar_apps]

    return jsonify({
        'message': 'OK',
        'result': result
    })


def get_scholar_app(id):
    scholar_app = ScholarApp.get_or_none(ScholarApp.id == id)
    if scholar_app:
        return jsonify({
            'message': 'OK',
            'result': scholar_app.to_dict()
        })
    else:
        return jsonify({
            'message': 'ERROR',
            'result': None
        }), 404


def update_scholar_app(id):
    scholar_app = ScholarApp.get_or_none(ScholarApp.id == id)
    if not scholar_app:
        return jsonify({
            'message': 'ERROR',
            'result': None
        }), 404

    scholar_app.name = request.json.get('name')
    scholar_app.email = request.json.get('email')
    scholar_app.university = request.json.get('university')
    scholar_app.address = request.json.get('address')
    scholar_app.save()

    return jsonify({
        'message': 'OK',
        'result': scholar_app
    })


def delete_scholar_app(id):
    scholar_app = ScholarApp.get_or_none(ScholarApp.id == id)
    if not scholar_app:
        return jsonify({
            'message': 'ERROR',
            'result': None
        }), 404

    scholar_app.delete_instance()
    return jsonify({
        'message': 'OK',
        'result': None
    })


routes = {
    '/': ('POST', submit_scholar_app),
    '/all': ('GET', AuthMiddleware(all_scholar_app)),
    '/<id>': ('GET', AuthMiddleware(get_scholar_app)),
    '/delete/<id>': ('POST', AuthMiddleware(delete_scholar_app)),
    '/update/<id>': ('POST', AuthMiddleware(update_scholar_app))
}