from flask import Flask, make_response,jsonify

#Local imports
from api.v1.views import api_views

app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(api_views)

@app.errorhandler(404)
def bad_request(error):
    return make_response(jsonify(error="Page not found :)"))

@app.route('/')
def index():
    return make_response('Brainwave backend API endpoint')
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)