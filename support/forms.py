from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ['customer_name', 'email', 'subject', 'description']


from .models import UserImage


class UserImageForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = forms.ChoiceField(choices=GENDER_CHOICES)

    class Meta:
        model = UserImage
        fields = ['image','gender']

