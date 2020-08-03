import json
from rest_framework.renderers import JSONRenderer


class CallRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        return json.dumps({'call': data})


class CallsRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        return json.dumps({'calls': data})
