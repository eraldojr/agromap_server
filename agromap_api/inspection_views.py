"""
Views da API rest
"""
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.shortcuts import render
from django.utils.six import BytesIO
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
import json
import numpy

from agromap_api.models.inspection import Inspection
from agromap_api.models.event import Event
from agromap_api.serializers import InspectionSerializer
from agromap_api.serializers import EventSerializer


# View para index
@csrf_exempt
def index(request):
    return JsonResponse({"Error":"Agromap: Not found"}, status=404, safe=False)

# TODO
# Header Authorization
@csrf_exempt
def create(request):
    if request.method == 'POST':
        __data = json.loads(request.POST['inspection'])
        serializer = InspectionSerializer(data=__data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(True, status=201, safe=False)
        return JsonResponse(serializer.errors, status=400, safe=False)
    else:
        return JsonResponse({"Error":"Agromap: HTTP method not allowed"}, status=405, safe=False)

# TODO
# Header Authorization
@csrf_exempt
def update(request):
    if request.method == 'POST':
        try:
            __data = json.loads(request.POST['inspection'])
            __inspection = Inspection.get_by_id_obj(__data['id'])
            serializer = InspectionSerializer(__inspection, data=__data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(True, status=201, safe=False)
            return JsonResponse(serializer.errors, status=400, safe=False)
        except Exception as e:
            print(e)
            return JsonResponse({"Error":"Agromap: Bad request"}, status=400, safe=False)
    else:
        return JsonResponse({"Error":"Agromap: HTTP method not allowed"}, status=405, safe=False)


# TODO
# Header Authorization e delete via GET
#
@csrf_exempt
def delete(request):
    if request.method == 'POST':
        __data = json.loads(request.POST['inspection'])
        __inspection = Inspection.get_by_id(__data['id'])
        if(__inspection != None):
            __inspection.delete()
            return JsonResponse(True, status=200, safe=False)
        return JsonResponse({"Error":"Inspection not found"}, status=405, safe=False)
    else:
        return JsonResponse({"Error":"Agromap: HTTP method not allowed"}, status=405, safe=False)

# TODO
# Header Authorization
@csrf_exempt
def get_by_id(request, id=None):
    if request.method == 'GET':
        try:
            __inspection = Inspection.get_by_id_json(id)
            if(__inspection != None):
                return JsonResponse(json.dumps(__inspection), status=200, safe=False)
            return JsonResponse({"Error":"Inspection not found"}, status=400, safe=False)
        except Exception as e:
            return JsonResponse({"Error":"Agromap: Bad request"}, status=400, safe=False)
    return JsonResponse({"Error":"Agromap: HTTP method not allowed"}, status=405, safe=False)

# TODO
# Header Authorization
@csrf_exempt
def get_by_supervisor(request, id=None):
    if request.method == 'GET':
        try:
            __inspections = Inspection.get_by_supervisor(id)
            if(__inspections != None):
                data = serializers.serialize('json', __inspections)
                return JsonResponse(data, status=200, safe=False)
            return JsonResponse({"Error":"Inspection not found"}, status=400, safe=False)
        except Exception as e:
            return JsonResponse({"Error":"Agromap: Bad request"}, status=400, safe=False)
    return JsonResponse({"Error":"Agromap: HTTP method not allowed"}, status=405, safe=False)


@csrf_exempt
def create_event(request):
    if request.method == 'POST':
        __data = json.loads(request.POST['event'])
        serializer = EventSerializer(data=__data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(True, status=201, safe=False)
        return JsonResponse(serializer.errors, status=400, safe=False)
    else:
        return JsonResponse({"Error":"Agromap: HTTP method not allowed"}, status=405, safe=False)


@csrf_exempt
def update_event(request):
    if request.method == 'POST':
        __data = json.loads(request.POST['event'])
        __event = Event.get_by_id_obj(__data['id'])
        serializer = EventSerializer(__event, data=__data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(True, status=201, safe=False)
        return JsonResponse(serializer.errors, status=400, safe=False)
    else:
        return JsonResponse({"Error":"Agromap: HTTP method not allowed"}, status=405, safe=False)

# TODO
# Header Authorization e delete via GET
#
@csrf_exempt
def delete_event(request):
    if request.method == 'POST':
        __data = json.loads(request.POST['event'])
        __event = Event.get_by_id(__data['id'])
        if(__event != None):
            __event.delete()
            return JsonResponse(True, status=200, safe=False)
        return JsonResponse({"Error":"Inspection not found"}, status=405, safe=False)
    else:
        return JsonResponse({"Error":"Agromap: HTTP method not allowed"}, status=405, safe=False)

# TODO
# Header Authorization
#
@csrf_exempt
def get_event_by_id(request, id=None):
    if request.method == 'GET':
        try:
            __event = Event.get_by_id_json(id)
            if(__event != None):
                return JsonResponse(json.dumps(__event), status=200, safe=False)
            return JsonResponse({"Error":"Event not found"}, status=400, safe=False)
        except Exception as e:
            return JsonResponse({"Error":"Agromap: Bad request"}, status=400, safe=False)
    return JsonResponse({"Error":"Agromap: HTTP method not allowed"}, status=405, safe=False)

# TODO
# Header Authorization
#
@csrf_exempt
def get_event_by_inspection(request, id=None):
    if request.method == 'GET':
        try:
            __events = Event.get_by_inspection(id)
            if(__events != None):
                data = serializers.serialize('json', __events)
                return JsonResponse(data, status=200, safe=False)
            return JsonResponse({"Error":"None event from inspection"}, status=400, safe=False)
        except Exception as e:
            return JsonResponse({"Error":"Agromap: Bad request"}, status=400, safe=False)
    return JsonResponse({"Error":"Agromap: HTTP method not allowed"}, status=405, safe=False)

# TODO
# Header Authorization
#
@csrf_exempt
def get_event_by_user(request, id=None):
        if request.method == 'GET':
            try:
                __events = Event.get_by_user(id)
                if(__events != None):
                    data = serializers.serialize('json', __events)
                    return JsonResponse(data, status=200, safe=False)
                return JsonResponse({"Error":"None event from user"}, status=400, safe=False)
            except Exception as e:
                return JsonResponse({"Error":"Agromap: Bad request"}, status=400, safe=False)
        return JsonResponse({"Error":"Agromap: HTTP method not allowed"}, status=405, safe=False)
