from __future__ import absolute_import

from django.conf.urls.defaults import *

from blogserver.api.handlers import BlogpostHandler
from piston.authentication import HttpBasicAuthentication
from piston.doc import documentation_view
from piston.resource import Resource

auth = HttpBasicAuthentication(realm="My sample API")

blogposts = Resource(handler=BlogpostHandler, authentication=auth)

urlpatterns = patterns(
    "",
    url(r"^posts/$", blogposts),
    url(r"^posts/(?P<emitter_format>.+)/$", blogposts),
    url(r"^posts\.(?P<emitter_format>.+)", blogposts, name="blogposts"),
    # automated documentation
    url(r"^$", documentation_view),
)
