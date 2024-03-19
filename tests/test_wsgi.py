# tests/test_wsgi.py
from wsgi import app
def test_one_roll():
    app.testing = True
    client = app.test_client()
    roll = client.get('/').json['roll']
    assert type(roll) == int
    assert roll > 0
    assert roll < 7