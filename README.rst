A small Locust test for load testing of Rasa NLU
=================================================
to run install Locust:

``pip install locustio``

and run:

``locust --host=http://206.189.52.11:5005 --locustfile locustrunner.py --port=80``

The server will be available for testing at http://localhost

On REST API load testing with Locust `read more here <https://shekhargulati.com/2018/12/06/locust-load-testing-your-rest-api/>`_.
