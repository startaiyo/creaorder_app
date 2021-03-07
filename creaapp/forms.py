from django import forms

class HowmanyInfo(forms.Form):
  def __init__(self, *args, **kwargs):
    super(HowmanyInfo, self).__init__(*args, **kwargs)
    for field in self.fields.values():
        field.widget.attrs["class"] = "form-control"
  
  many=forms.IntegerField(label='個数')
