from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('facebook.views',
    url(r'^channel.html$', 'channel', name='facebook_channel'),
)
