import requests

import config
import data


def post_new_order(order_body):
    return requests.post(config.URL_SERVICE + config.CREATE_ORDER_PATH,
                         json=order_body)


def get_track_order():
    track = post_new_order(data.order_body)
    return track.json()["track"]


def check_status_order():
    return requests.get(config.URL_SERVICE + config.STATUS_ORDER_PATH,
                        json=data.order_body,
                        params={
                            't': get_track_order(),
                        })


def test_status_order():
    track = check_status_order()
    assert track.status_code == 200
