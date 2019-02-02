from handler.scholar import routes as scholar_routes

from core.router import Router
from flask import Flask


app = Flask(__name__)
router = Router(app)

router.get('/', lambda: 'Hello World!')
router.group('/scholar', scholar_routes)


if __name__ == '__main__':
    router.execute()
    app.run(port=8888)
