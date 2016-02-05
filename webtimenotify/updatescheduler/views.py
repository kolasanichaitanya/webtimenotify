import json
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from updatescheduler.models import UpdateEvent
from updatescheduler.serializers import UpdateEventSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

def index(request):
	template = loader.get_template('entertask.html')
	return HttpResponse(template.render(request))

def submittask(request):
	transaction_id = request.GET['transid']
	no_of_hours = request.GET['hourscount']
	job_number_choice = request.GET['entryname']
	month_choice = request.GET['monthname']
	day_choice = request.GET['daynumber']

	event = UpdateEvent(transaction_id=transaction_id,no_of_hours=no_of_hours,job_number_choice=job_number_choice,month_choice=month_choice,day_choice=day_choice);
	event.save()
	return HttpResponse("transaction_id is "+transaction_id);

def deletetask(request):
	transaction_id = request.GET['transid']
	event = get_object_or_404(UpdateEvent,transaction_id__exact=transaction_id)
	event.delete()
	return HttpResponse("Delete Successful")

@api_view(['GET'])
def getpendingentries(request):
	queryset = UpdateEvent.objects.all()
	serializer_class = UpdateEventSerializer(queryset, many=True)
	return Response(serializer_class.data)

