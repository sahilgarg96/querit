from __future__ import unicode_literals

from django.apps import AppConfig
from watson import search as watson


class PostsConfig(AppConfig):
    name = 'posts'

    def ready(self):
    	model = self.get_model("admission")
    	watson.register(model,fields=('title','tags','content'))
    	model2 = self.get_model("placement")
    	watson.register(model2,fields=('title','tags','content'))
