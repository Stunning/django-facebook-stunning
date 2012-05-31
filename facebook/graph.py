import logging
from urllib import urlencode, urlopen

from django.utils import simplejson as json
from django.conf import settings

logger = logging.getLogger(__name__)

def get_token(app_id, app_secret):
    url = 'https://graph.facebook.com/oauth/access_token'
    data = {
        'client_id': app_id,
        'client_secret': app_secret,
        'grant_type': 'client_credentials',
    }
    f = urlopen(url, urlencode(data))
    return f.read().split('=', 1)[-1]

def get_testusers(app_id, token):
    url = 'https://graph.facebook.com/%s/accounts/test-users' % app_id
    data = {
        'access_token': token,
    }
    f = urlopen(url + '?' + urlencode(data))
    data = json.load(f)
    return data['data']
    
def add_testuser(app_id, token, installed=False, name=None, permissions=[]):
    url = 'https://graph.facebook.com/%s/accounts/test-users' % app_id
    data = {
        'installed': 'true' if installed else 'false',
        'permissions': ','.join(permissions),
        'method': 'post',
        'access_token': token,
    }
    if name:
        data['name'] = str(name)
    f = urlopen(url, urlencode(data))
    data = json.load(f)
    return [data]

