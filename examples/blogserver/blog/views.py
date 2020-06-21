from __future__ import absolute_import

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext

from blogserver.blog.models import Blogpost


def posts(request):
    posts = Blogpost.objects.all()

    return render_to_response("posts.html", {"posts": posts}, RequestContext(request))


def test_js(request):
    return render_to_response("test_js.html", {}, RequestContext(request))
