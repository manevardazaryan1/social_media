from rest_framework import generics
from .serializers import MessageSerializer, ConversationSerializer
from .filters import MessageFilter, ConversationFilter
from .permissions import IsAdminOrReadOnly
from message.models import Message, Conversation


class MessageListAPIView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filterset_class = MessageFilter
    permission_classes = [IsAdminOrReadOnly]


class MessageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAdminOrReadOnly]


class ConversationListAPIView(generics.ListCreateAPIView):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    filterset_class = ConversationFilter
    permission_classes = [IsAdminOrReadOnly]


class ConversationDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAdminOrReadOnly]