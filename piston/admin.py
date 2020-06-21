from __future__ import absolute_import

from django.contrib import admin

from piston.models import Consumer
from piston.models import Nonce
from piston.models import Token


class ConsumerAdmin(admin.ModelAdmin):
    raw_id_fields = ("user",)


admin.site.register(Nonce)
admin.site.register(Consumer, ConsumerAdmin)
admin.site.register(Token)
