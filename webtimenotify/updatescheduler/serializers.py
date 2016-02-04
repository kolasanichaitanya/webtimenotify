from updatescheduler.models import UpdateEvent
from rest_framework import serializers

class UpdateEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UpdateEvent
        fields = ('transaction_id', 'no_of_hours', 'job_number_choice')
