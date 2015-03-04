import os
import sys
import waitress

BASE_DIR = os.path.join(os.path.dirname(__file__), 'demo')
sys.path.append(BASE_DIR)

from demo.wsgi import application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.settings")

waitress.serve(
    application,
    host='0.0.0.0',
    port=os.environ.get("PORT"),
    cleanup_interval=os.getenv('CLEANUP_INTERVAL', 20),
    channel_timeout=os.getenv('CHANNEL_TIMEOUT', 20))
