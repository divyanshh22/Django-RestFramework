from django.http import HttpResponse

def apis(request):
    apis = [
        {'student_id':1,'name':'Divya','email':'divyansh222f@gmail.com','branch':'CS'}
    ]

    return HttpResponse(apis)



# Create your views here.
