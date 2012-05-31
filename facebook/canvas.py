import logging
from base64 import urlsafe_b64decode, b64encode
import hmac
import hashlib

from django.utils import simplejson as json
from django.conf import settings

logger = logging.getLogger(__name__)

def get_post_data(signed_request):
    sig_encoded, data_encoded = str(signed_request).split('.', 1)
    sig = decode(sig_encoded)
    sig_valid = hmac.new(settings.FACEBOOK_APP_SECRET, data_encoded, hashlib.sha256).digest()
    data = json.loads(decode(data_encoded))
    if sig != sig_valid:
        raise Exception("Facebook signed request is invalid")
    return data

def decode(x):
    last_group_len = len(x) % 4
    if last_group_len:
        x += '=' * (4 - last_group_len)
    return urlsafe_b64decode(x)
