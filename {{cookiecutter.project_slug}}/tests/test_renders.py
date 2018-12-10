import datetime as dt
from decimal import Decimal
from {{cookiecutter.project_slug}}.common import ExtJSONRenderer


def test_extended_encoder_date_parsing():
    json_renderer = ExtJSONRenderer()
    test_date = dt.datetime(2017, 5, 10)
    assert test_date.isoformat() == json_renderer.default(test_date)


def test_extended_encoder_decimal_casting():
    json_renderer = ExtJSONRenderer()
    test_decimal = Decimal('1.0')
    assert 1.0 == json_renderer.default(test_decimal)
