from flask import Flask,render_template,request,jsonify
import requests
from weatherApiCallout import getMethode,getUrl
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint


app = Flask(__name__)

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Api weather"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###



@app.route('/')
def index():
    api_url = getUrl('current','nice',None)
    return jsonify(getMethode(api_url))

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

@app.route('/api/v1/rs/current/city/<string:city>', methods=['GET'])
def getCurrentByCity(city):
    api_url = getUrl('current',city,None)
    return jsonify(getMethode(api_url))

@app.route('/api/v1/rs/forecast/city/<string:city>/<string:days>', methods=['GET'])
def getForecastByCity(city,days):
    api_url = getUrl('forecast',city,days)
    return jsonify(getMethode(api_url))

@app.route('/api/v1/rs/search/city/<string:city>/<string:days>', methods=['GET'])
def getSearchByCity(city,days):
    api_url = getUrl('search',city,None)
    return jsonify(getMethode(api_url))
    

@app.route("/spec")
def spec():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "My API"
    return jsonify(swag)

if __name__ == "__main__":
     app.run(debug=True)