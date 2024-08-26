from django.contrib import admin
from message.models import Message, Conversation

admin.site.register(Message)
admin.site.register(Conversation)