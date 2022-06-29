Dummy Flask app sandbox
==================================


## Pre-requisites

* Git client;
* Python interpreter (3.7+) with pip and virtualenv;


## Development installation

* Clone the code:

  ```
  git clone https://github.com/fredericlam/FlaskDemo myproject
  python3 -m venv venv
  . venv/bin/activate
  ```

* Install API dependencies:

  ```
  #pip install -r api/requirements.txt
  pip install Flask
  ```


## Development server

Start development server:

```
export FLASK_ENV=development
flask run --port=5002
```

or 

```
export FLASK_ENV=development
python3 -m flask --port=5002
```


Your dev index page will be available at [http://127.0.0.1:5002](http://127.0.0.1:5002).
Client bundle rebuilds automatically upon changes in the source code.
