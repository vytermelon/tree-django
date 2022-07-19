from django.urls import re_path, path

from . import consumers

websocket_urlpatterns = [
    #re_path(r'^ws/read_tree/(?P<node_id>[\d\D]+)/(?P<book_id>\d+)/$', consumers.ChatRoomConsumer),
    path('ws/read_tree/<str:node_id>/<int:book_id>', consumers.ChatRoomConsumer.as_asgi()),
]