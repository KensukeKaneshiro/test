import json
from urllib.parse import urlencode
from urllib.request import Request
from urllib.request import urlopen
from urllib.error import HTTPError
import re

config = {'Auth_key': '58662917-f976-503c-bc16-78b1de0b1d4e:fx',
          'Translate_ep': 'https://api-free.deepl.com/v2/translate',
          'Usage_ep': 'https://api-free.deepl.com/v2/usage'}


def translate(text, t_lang):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; utf-8'
    }

    params = {
        'auth_key': config['Auth_key'],
        'text': text,        
        'target_lang': t_lang
    }

    req = Request(
        config['Translate_ep'],
        method='POST',
        data=urlencode(params).encode('utf-8'),
        headers=headers
    )

    try:
        with urlopen(req) as res:
            trans_result = json.loads(res.read().decode('utf-8'))            
            return trans_result['translations'][0]['text']            
    except HTTPError as e:
        print(e)


def char_cnt():
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; utf-8'
    }

    params = {
        'auth_key': config['Auth_key'],
    }

    req = Request(
        config['Usage_ep'],
        method='POST',
        data=urlencode(params).encode('utf-8'),
        headers=headers
    )
    try:
        with urlopen(req) as res:
            cnt_result = json.loads(res.read().decode('utf-8'))
            return cnt_result

    except HTTPError as e:
        print(e)

def lang_set(text):
    # default setting
    t_lang = "JA"
    if re.search(r'[ぁ-んァ-ン]', text):
        t_lang = "EN"

    return t_lang
