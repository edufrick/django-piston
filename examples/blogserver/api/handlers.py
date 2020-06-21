from __future__ import absolute_import

from blogserver.blog.models import Blogpost
from piston.handler import AnonymousBaseHandler
from piston.handler import BaseHandler
from piston.utils import rc
from piston.utils import require_extended
from piston.utils import require_mime


class BlogpostHandler(BaseHandler):
    """
    Authenticated entrypoint for blogposts.
    """

    model = Blogpost
    anonymous = "AnonymousBlogpostHandler"
    fields = (
        "title",
        "content",
        ("author", ("username",)),
        "created_on",
        "content_length",
    )

    @classmethod
    def content_length(cls, blogpost):
        return len(blogpost.content)

    @classmethod
    def resource_uri(cls, blogpost):
        return ("blogposts", ["json",])

    def read(self, request, title=None):
        """
        Returns a blogpost, if `title` is given,
        otherwise all the posts.
        
        Parameters:
         - `title`: The title of the post to retrieve.
        """
        base = Blogpost.objects

        if title:
            return base.get(title=title)
        else:
            return base.all()

    def create(self, request):
        """
        Creates a new blogpost.
        """
        attrs = self.flatten_dict(request.POST)

        if self.exists(**attrs):
            return rc.DUPLICATE_ENTRY
        else:
            post = Blogpost(
                title=attrs["title"], content=attrs["content"], author=request.user
            )
            post.save()

            return post


class AnonymousBlogpostHandler(BlogpostHandler, AnonymousBaseHandler):
    """
    Anonymous entrypoint for blogposts.
    """

    fields = ("id", "title", "content", "created_on")
