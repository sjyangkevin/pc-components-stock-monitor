import re

def parse_currency(value) -> float:
    return float(re.sub(r'[^\d.]', '', value)) if isinstance(value, str) else value

def parse_rating(value) -> float:
    return float(value.strip()) if isinstance(value, str) else value
