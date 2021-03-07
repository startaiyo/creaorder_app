from django import forms

class HowmanyInfo(forms.Form):
  many=forms.IntegerField()