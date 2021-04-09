import json
from django.core.serializers import serialize
from django.views.generic import View
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from .models import Update 
from everspecsadmin.mixins import JsonResponseMixin
# Create your views here.
def json_example(request):
    data = {
        "count": 1000,
        "content": "asdfasdf"
    }
    json_data = json.dumps(data)
    #return HttpResponse(json_data, content_type='applicaton/json')
    return HttpResponse(json_data)

class jsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "asdfasdf"
        }
        return JsonResponse(data)



    
class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=2)
        data = {
            'username':obj.user.username,
            'content':obj.content
        }
        return self.render_to_json_response(data)

class SerializedDetailView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=3)
        #data = serialize("json", [obj,], fields=('user', 'content'))
        json_data = obj.serialize()
        #json_data = data 
        # data = {
        #     'username':obj.user.username,
        #     'content':obj.content
        # }
        #json_data = json.dumps(data)
        return HttpResponse(json_data, content_type='application/json')

# python manage.py dumpdata --format json --indent 3
class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        qs = Update.objects.all()
        json_data = Update.objects.all().serialize()
        #json_data = serialize('json', qs)#, fields=('User', 'content'))
        # data = {
        #     'username':obj.user.username,
        #     'content':obj.content
        # }
        #json_data = json.dumps(json_data)
        return HttpResponse(json_data, content_type='application/json')