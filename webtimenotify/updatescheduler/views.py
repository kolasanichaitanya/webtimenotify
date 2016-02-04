import json
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from updatescheduler.models import UpdateEvent
from updatescheduler.serializers import UpdateEventSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view

def index(request):
	template = loader.get_template('entertask.html')
	return HttpResponse(template.render(request))

def submittask(request):
	transaction_id = request.GET['transid']
	no_of_hours = request.GET['hourscount']
	job_number_choice = request.GET['entryname']
	event = UpdateEvent(transaction_id=transaction_id,no_of_hours=no_of_hours,job_number_choice=job_number_choice);
	event.save()
	return HttpResponse("transaction_id is "+transaction_id);

@api_view(['GET'])
def getpendingentries(request):
	queryset = UpdateEvent.objects.all()
	serializer_class = UpdateEventSerializer(queryset, many=True)
	#return HttpResponse(JSONRenderer().render(serializer_class.data))
	return Response(serializer_class.data)
