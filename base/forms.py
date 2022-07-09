
from django.forms import ModelForm
from .models import *

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['Host' , 'participants','roomType']

class messageForm(ModelForm):
    class Meta:
        model = message
        fields = ['body']