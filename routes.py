from handler.scholar import routes as scholar_routes
from handler.scholar_app import routes as scholar_app_routes
from handler.sponsor_app import routes as sponsor_app_routes

from core.router import Router
from flask import Flask


app = Flask(__name__)
router = Router(app)

router.get('/', lambda: 'Hello World!')
router.group('/scholar', scholar_routes)
router.group('/scholar_app', scholar_app_routes)
router.group('/sponsor_app', sponsor_app_routes)


if __name__ == '__main__':
    router.execute()
    app.run(port=8888)
