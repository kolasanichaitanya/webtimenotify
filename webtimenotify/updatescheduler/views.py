from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from updatescheduler.models import UpdateEvent

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
