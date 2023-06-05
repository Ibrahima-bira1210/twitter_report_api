# Twitter Report API
The Twitter Report API is a Flask-based application that allows users to report 
Twitter accounts for posting hate speech messages. This repository provides the necessary 
code and configurations to run the API as a standalone service.

## Prerequisites
Before running the Twitter Report API, ensure that you have the following dependencies installed:
- Python (version 3.10 or higher)
- pip package manager

## Installation
1. Clone this repository to your local machine or server:

``
   git clone https://github.com/Ibrahina-bira1210twitter-report-api.git ``
2. Navigate to the project directory:

``
    cd twitter-report-api ``
3. Install the required Python packages:

``
    pip install -r requirements.txt``

## Configuration
The Twitter Report API requires a Twitter developer account to access the Twitter API.
1. Obtain Twitter API credentials:
- Create a Twitter Developer account at https://developer.twitter.com/.
- Create a new application and generate the API key, API secret key, access token, and access token secret.
- Copy the credentials and keep them secure.

## Usage
To run the Twitter Report API, execute the following command from the project directory:

``
    python app.py'''
The API will start running on [http://localhost:5000/swagger](http://localhost:5000/swagger)

## API Endpoint
The API provides a single endpoint:

`POST /reportUser`: Allows you to report a Twitter user for posting hate speech messages. 
The request should include a JSON payload containing the Twitter API credentials and the screen name of the user to be reported.

Example request payload:
```json
{
  "api_key": "YOUR_API_KEY",
  "api_secret_key": "YOUR_API_SECRET_KEY",
  "access_token": "YOUR_ACCESS_TOKEN",
  "access_token_secret": "YOUR_ACCESS_TOKEN_SECRET",
  "screen_name": "target_user",
  "report_count": 1
}

```
The API will respond with a success message indicating that the user has been reported.

## Contributing
Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please submit an issue or a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](https://opensource.org/license/mit/) file for details.

## Disclaimer
Please note that the use of this API to report Twitter accounts should comply with Twitter's policies and guidelines. 
Ensure that you have a valid reason to report a user and that your usage of the API is within the permitted limits. 
The developers of this API are not responsible for any misuse or violation of Twitter's terms of service.
