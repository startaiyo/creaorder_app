from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from datetime import date
from dateutil.relativedelta import relativedelta
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
# Create your views here.
def index(request):
  form=forms.HowmanyInfo(request.POST)
  sun=date.today()+relativedelta(days=1)
  sunt=sun.strftime("%#m月%#d日")
  day=sun.weekday()
  WEEKDAY = ('月','火','水','木','金','土','日')
  jaday = WEEKDAY[day]
  if form.is_valid():
    many=f"{form.cleaned_data['many']}"
    weight=f"{form.cleaned_data['many']*20}kg"
    subject = "マウス餌CE-2（京大薬システムバイオ）"
    context={'form':form, 'sunt':sunt, 'many':many, 'jaday':jaday, 'weight':weight}
    message = render_to_string('creaapp/mails.txt', context, request)
    from_email = settings.DEFAULT_FROM_EMAIL  # 送信者
    recipient_list = ["startaiyo0104@gmail.com"]  # 宛先リスト
    bcc =  [""]  # BCCリスト
    send_mail(subject, message, from_email, recipient_list, bcc)
    return render(
      request, "creaapp/ordered.html",context={'form':form}
    )
  return render(
    request, "creaapp/index.html",context={'form':form}
    )

def noorder(request):
  sun=date.today()+relativedelta(days=1)
  sunt=sun.strftime("%#m月%#d日")
  day=sun.weekday()
  WEEKDAY = ('月','火','水','木','金','土','日')
  jaday = WEEKDAY[day]
  subject = "マウス餌CE-2（京大薬システムバイオ）"
  context={'sunt':sunt, 'jaday':jaday}
  message = render_to_string('creaapp/mails2.txt', context, request)
  from_email = settings.DEFAULT_FROM_EMAIL  # 送信者
  recipient_list = ["startaiyo0104@gmail.com"]  # 宛先リスト
  bcc =  [""]  # BCCリスト
  send_mail(subject, message, from_email, recipient_list, bcc)
  return render(
      request, "creaapp/ordered.html"
    )