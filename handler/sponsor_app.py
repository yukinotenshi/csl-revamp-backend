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
    name = request.form.get('name')
    email = request.form.get('email')
    position = request.form.get('position')
    company = request.form.get('company')
    phone = request.form.get('phone')

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

    sponsor_app.name = request.form.get('name')
    sponsor_app.email = request.form.get('email')
    sponsor_app.position = request.form.get('position')
    sponsor_app.company = request.form.get('company')
    sponsor_app.phone = request.form.get('phone')
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