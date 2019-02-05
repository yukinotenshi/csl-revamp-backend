from flask import jsonify, request
from model import SponsorApp

from middleware.auth import AuthMiddleware

'''
name = pw.CharField()
email = pw.CharField()
position = pw.CharField()
company = pw.CharField()
phone = pw.CharField()
'''

def submit_sponsor_app():
    name = request.json.get('name')
    email = request.json.get('email')
    position = request.json.get('position')
    company = request.json.get('company')
    phone = request.json.get('phone')

    sponsor_app = SponsorApp(
        name=name,
        email=email,
        position=position,
        company=company,
        phone=phone
    )

    try:
        sponsor_app.save()
    except Exception as e:
        return jsonify({
            'message': 'ERROR',
            'result': e
        }), 404

    return jsonify({
        'message': 'OK',
        'result': sponsor_app.to_dict()
    })


def all_sponsor_app():
    sponsor_apps = SponsorApp.select()
    result = [s.to_dict() for s in sponsor_apps]

    return jsonify({
        'message': 'OK',
        'result': result
    })


def get_sponsor_app(id):
    sponsor_app = SponsorApp.get_or_none(SponsorApp.id == id)
    if sponsor_app:
        return jsonify({
            'message': 'OK',
            'result': sponsor_app.to_dict()
        })
    else:
        return jsonify({
            'message': 'ERROR',
            'result': None
        }), 404


def update_sponsor_app(id):
    sponsor_app = SponsorApp.get_or_none(SponsorApp.id == id)
    if not sponsor_app:
        return jsonify({
            'message': 'ERROR',
            'result': None
        }), 404

    sponsor_app.name = request.json.get('name')
    sponsor_app.email = request.json.get('email')
    sponsor_app.position = request.json.get('position')
    sponsor_app.company = request.json.get('company')
    sponsor_app.phone = request.json.get('phone')
    sponsor_app.save()

    return jsonify({
        'message': 'OK',
        'result': sponsor_app
    })


def delete_sponsor_app(id):
    sponsor_app = SponsorApp.get_or_none(SponsorApp.id == id)
    if not sponsor_app:
        return jsonify({
            'message': 'ERROR',
            'result': None
        }), 404

    sponsor_app.delete_instance()
    return jsonify({
        'message': 'OK',
        'result': None
    })


routes = {
    '/': ('POST', submit_sponsor_app),
    '/all': ('GET', AuthMiddleware(all_sponsor_app)),
    '/<id>': ('GET', AuthMiddleware(get_sponsor_app)),
    '/delete/<id>': ('POST', AuthMiddleware(delete_sponsor_app)),
    '/update/<id>': ('POST', AuthMiddleware(update_sponsor_app))
}