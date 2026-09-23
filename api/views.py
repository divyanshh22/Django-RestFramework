from django.http import JsonResponse

def apisvie(request):
    students={
        'student_id':1,
        'name':'Divyansh',
        'email':'divyansh222f@gmail.com',
        'branch':'CS'
    }

    return JsonResponse(students)


# Create your views here.
