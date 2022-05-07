import orjson
from ninja.renderers import BaseRenderer
from ninja.parser import Parser


class JSONParser(Parser):
    def parse_body(self, request):
        return orjson.loads(request.body)


class JSONRenderer(BaseRenderer):
    media_type = "application/json"

    def render(self, request, data, *, response_status):
        return orjson.dumps(data)
