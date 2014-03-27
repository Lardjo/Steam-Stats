#!/usr/bin/env python3

import logging

from tornado.gen import coroutine
from tornado.escape import json_decode
from tornado.httpclient import HTTPClient, HTTPError
from tornado.httputil import url_concat

from datetime import datetime


def converter(steamid):
    return int(steamid) - 76561197960265728


@coroutine
def get_user(key, steamid):
    user = None
    url = url_concat('https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/', {'key': key,
                                                                                           'steamids': steamid})
    client = HTTPClient()

    try:
        response = client.fetch(url)
        array = json_decode(response.body)['response']['players'][0]
        user = {'id': converter(steamid),
                'claimed_id': array['steamid'],
                'personaname': array['personaname'],
                'profileurl': array['profileurl'],
                'avatar': array['avatarfull'],
                'signup': datetime.now(),
                'update': datetime.now()}

        if 'realname' in array.keys():
            user['realname'] = array['realname']
        else:
            user['realname'] = None

    except HTTPError as e:
        logging.error('Error: %s' % e)

    client.close()
    return user