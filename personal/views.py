from django.shortcuts import render
from account.models import Account
# Create your views here.

def home_screen_view(request):
    accounts=Account.objects.all()
    context={'accounts':accounts}
    return render(request,'personal/home.html',context)