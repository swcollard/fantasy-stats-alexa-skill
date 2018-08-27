"""
Helper class to get the current week of the season for the API call
"""
from datetime import datetime


def get_week():
    today = datetime.now()
    if today > datetime(2018, 12, 29):
        return {"year": 2018, "week": 17}
    elif today > datetime(2018, 12, 22):
        return {"year": 2018, "week": 16}
    elif today > datetime(2018, 12, 12):
        return {"year": 2018, "week": 15}
    elif today > datetime(2018, 12, 5):
        return {"year": 2018, "week": 14}
    elif today > datetime(2018, 11, 28):
        return {"year": 2018, "week": 13}
    elif today > datetime(2018, 11, 21):
        return {"year": 2018, "week": 12}
    elif today > datetime(2018, 11, 14):
        return {"year": 2018, "week": 11}
    elif today > datetime(2018, 11, 7):
        return {"year": 2018, "week": 10}
    elif today > datetime(2018, 10, 31):
        return {"year": 2018, "week": 9}
    elif today > datetime(2018, 10, 24):
        return {"year": 2018, "week": 8}
    elif today > datetime(2018, 10, 17):
        return {"year": 2018, "week": 7}
    elif today > datetime(2018, 10, 10):
        return {"year": 2018, "week": 6}
    elif today > datetime(2018, 10, 3):
        return {"year": 2018, "week": 5}
    elif today > datetime(2018, 9, 26):
        return {"year": 2018, "week": 4}
    elif today > datetime(2018, 9, 19):
        return {"year": 2018, "week": 3}
    elif today > datetime(2018, 9, 12):
        return {"year": 2018, "week": 2}
    elif today > datetime(2018, 9, 5):
        return {"year": 2018, "week": 1}
    return {"year": 2017, "week": 6}  # Test Data as the fallback
