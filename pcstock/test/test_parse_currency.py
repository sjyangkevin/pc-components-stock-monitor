from pcstock.utils import parse_currency

def test_parse_currency():

    test_price_1 : float = 549.99
    test_price_2 : int   = 549
    test_price_3 : str   = "549.99"
    test_price_4 : str   = "$549.99"
    test_price_5 : str   = "$549"
    test_price_6 : str   = "549"

    assert test_price_1 == parse_currency(test_price_1) and isinstance(parse_currency(test_price_1), float)
    assert parse_currency(test_price_2) == 549.0 and isinstance(parse_currency(test_price_2), float)
    assert parse_currency(test_price_3) == 549.99 and isinstance(parse_currency(test_price_3), float)
    assert parse_currency(test_price_4) == 549.99 and isinstance(parse_currency(test_price_4), float)
    assert parse_currency(test_price_5) == 549.0 and isinstance(parse_currency(test_price_5), float)
    assert parse_currency(test_price_6) == 549.0 and isinstance(parse_currency(test_price_6), float)