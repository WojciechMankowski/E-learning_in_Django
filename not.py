# https://docs.kony.com/konylibrary/konyfabric/kony_fabric_manual_install_guide/Content/Install_Memcached_Server.htm
# manage.py check --deploy
# set DJANGO_SETTINGS_MODULE=educa.settings
# export DJANGO_SETTINGS_MODULE=mysites.settings
from django.core.cache import cache

from courses.models import Subject

subcjects = Subject.objects.all()
cache.set("wszystkie_dzienniny", subcjects)
print(cache.get("wszystkie_dzienniny"))