from django.urls import path
from message.api.views import MessageListAPIView, MessageDetailAPIView, ConversationListAPIView, ConversationDetailAPIView

urlpatterns = [
    path("messages/", MessageListAPIView.as_view(), name="message-list"),
    path("messages/<int:pk>/", MessageDetailAPIView.as_view(), name="message-detail"),
    path("conversations/", ConversationListAPIView.as_view(), name="conversation-list"),
    path("conversations/<int:pk>/", ConversationDetailAPIView.as_view(), name="conversation-detail"),
]
