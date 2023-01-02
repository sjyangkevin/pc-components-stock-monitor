from pcstock.utils import parse_rating

def test_parse_rating():

    test_rate_1 : int = 4
    test_rate_2 : float = 4.0
    test_rate_3 : str = "4.0"
    test_rate_4 : str = " 4.0"
    test_rate_5 : str = "4.0 "
    test_rate_6 : str = " 4.0 "
    test_rate_7 : str = "   4      "
    
    assert parse_rating(test_rate_1) == 4.0
    assert parse_rating(test_rate_2) == 4.0
    assert parse_rating(test_rate_3) == 4.0
    assert parse_rating(test_rate_4) == 4.0
    assert parse_rating(test_rate_5) == 4.0
    assert parse_rating(test_rate_6) == 4.0
    assert parse_rating(test_rate_7) == 4.0