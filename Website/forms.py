from django import forms

CARRIER_CHOICES= [ ("@mms.att.net","AT&T"),
    ("@tmomail.net","T-Mobile"),
    ("@vtext.com","Verizon"),
    ("@messaging.sprintpcs.com","Sprint")]

class AlarmForm(forms.Form):
    temperature_alarm= forms.CharField(label="Temperature Alarm Level")
    nutrients_alarm= forms.CharField(label="Nutrients Alarm Level")
    cellphone=forms.CharField(label="Cellphone Number")
    cellphone_carrier = forms.CharField(label="Celphone Carrier", required=False, widget=forms.Select(choices=CARRIER_CHOICES))