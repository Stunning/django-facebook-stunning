""" P3P Cookie header

Required to make IE accept cookies from sites served loaded through an iframe like Facebook

http://djangosnippets.org/snippets/1084/
"""
P3P_COMPACT = 'CP="IDC DSP COR ADM DEVi TAIi PSA PSD IVAi IVDi CONi HIS OUR IND CNT"'
# eg. P3P_COMPACT='CP="CAO DSP CURa ADMa DEVa TAIa CONa OUR DELa BUS IND PHY ONL UNI PUR COM NAV DEM STA"'

class MiddlewareResponseInjectP3P(object):
    def __init__(self):
        self.process_response = self.inject

    def inject(self, request, response):
        response['P3P'] = P3P_COMPACT
        return response