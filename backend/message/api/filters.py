import django_filters
from django.contrib.auth.models import User
from message.models import Message, Conversation

class MessageFilter(django_filters.FilterSet):
    sender = django_filters.ModelChoiceFilter(queryset=User.objects.all())
    recipient = django_filters.ModelChoiceFilter(queryset=User.objects.all())
    timestamp = django_filters.DateTimeFromToRangeFilter()

    class Meta:
        model = Message
        fields = ["sender", "recipient", "timestamp"]


class ConversationFilter(django_filters.FilterSet):
    participants = django_filters.ModelMultipleChoiceFilter(
        queryset=User.objects.all(),
        conjoined=True
    )
    last_message = django_filters.CharFilter(field_name="last_message__content", lookup_expr="icontains")

    class Meta:
        model = Conversation
        fields = ["participants", "last_message"]
