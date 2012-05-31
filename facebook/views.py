# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
import logging
import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from facebook.canvas import get_post_data

logger = logging.getLogger(__name__)

@csrf_exempt
def canvas_example(request):
    facebook_signed_request = request.POST.get('signed_request', None)
    if facebook_signed_request:
        facebook_data = get_post_data(facebook_signed_request)
        logger.debug("Facebook data: " + json.dumps(facebook_data, indent=4))

def channel(request):
    """ Returns the channel.html file as described in http://developers.facebook.com/docs/reference/javascript/FB.init/"""
    response = HttpResponse('<script src="//connect.facebook.net/sv_SE/all.js"></script>')
    t = datetime.now() + timedelta(weeks=500)
    response['Expires'] = t.ctime()
    return response
