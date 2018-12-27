from django import forms
from django.core import validators
from topics.models import newsletter_subscriber,website_recommendation



class form_data(forms.ModelForm):
    first_name = forms.CharField()
    last_name  = forms.CharField()
    email = forms.EmailField()
    botcatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])

    class Meta():
        model = newsletter_subscriber
        fields = '__all__'

class form_data2(forms.ModelForm):
    website = forms.CharField()
    reason = forms.CharField()
    email = forms.EmailField()
    botcatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])

    class Meta():
        model = website_recommendation
        fields = '__all__'
