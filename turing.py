#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


def get_turing_reply(text):
    api = 'http://openapi.tuling123.com/openapi/api/v2'
    api_key = ''
    user_id = ''
    payload = {
        'reqType': 0,
        'perception': {
            'inputText': {
                'text': text
            }
        },
        'userInfo': {
            'apiKey': api_key,
            'userId': user_id
        }
    }
    response = requests.post(url=api, json=payload)
    response = response.json()
    reply = response['results'][0]['values']['text']
    return reply
