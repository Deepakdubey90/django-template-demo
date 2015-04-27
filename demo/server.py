import os
import sys
import waitress
from demo.wsgi import get_wsgi_application


BASE_DIR = os.path.join(os.path.dirname(__file__), 'demo')
sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.settings")
application = get_wsgi_application()

waitress.serve(
    application,
    host='0.0.0.0',
    port=os.environ.get("PORT"),
    cleanup_interval=os.getenv('CLEANUP_INTERVAL', 20),
    channel_timeout=os.getenv('CHANNEL_TIMEOUT', 20))
