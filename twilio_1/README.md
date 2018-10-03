# twilio_1

Send a SMS with Flask and Twilio.

## Installation

On MacOS, install Pipenv with Homebrew:

```
$ brew install pipenv
```

Install Python dependencies:

```
$ cd twilio_1
$ pipenv install
```

## Getting started

You need to provide all credentials and configurations in a `config.py` file. These include `ACCOUNT_SID`, `AUTH_TOKEN`, `TO`, `FROM_`, `BODY`.

Start the server with:

```
pipenv run python application.py
```

Send a SMS by calling http://127.0.0.1:5000/.