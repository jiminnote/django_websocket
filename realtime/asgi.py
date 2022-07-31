import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter
from channels.auth import AuthMiddlewareStack

from integers.routing import ws_urlpatterns

os.environ.setdefault('DJANGO_SETTING_MODULE','realtime.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    'http': django_asgi_app, #http://
    'websocket': AuthMiddlewareStack(URLRouter(ws_urlpatterns)) #ws://
})

