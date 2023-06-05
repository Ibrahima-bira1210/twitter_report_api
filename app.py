import tweepy
from flask import Flask
from flask import request
from twitter_auth import auth_twitter
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

## Swagger specification

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "twitter data extract"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


### end swagger specific ###


@app.route('/reportUser', methods=['POST'])
def scrapToPostgres(report_count=1):
    # get request data
    data = request.get_json()

    # authorize the API Key
    auth = auth_twitter(api_key=data['api_key'], api_secret_key=data['api_secret_key'],
                        access_token=data['access_token'],
                        access_token_secret=data['access_token_secret']).auth
    # call the api
    api = tweepy.API(auth)

    # the account to be reported
    screen_name = data['screen_name']

    # the number of times the account has been reported
    report_count = data['report_count']

    # reporting the account
    while report_count > 0:
        report_count -= 1
        api.report_spam(screen_name=screen_name)

    return f"Le compte {screen_name} a été signalé {data['report_count']} fois pour publication de messages à caractère haineux.", 200


if __name__ == '__main__':
    app.run()
