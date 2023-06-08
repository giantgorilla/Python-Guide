from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

course_dict = {
    "python": "Python Course Page",
    "java" : "Java Course Page",
    "kotlin" : "Kotlin Course Page",
    "swift" :  "Swift Course Page"
}

def index(request):
    return HttpResponse("This is my first Django Project Index")

def course (request, item):
    try:
        course = course_dict[item]
        return HttpResponse(course)
    except:
        return HttpResponseNotFound("Not Found! Please Look For Another Course")
        #raise Http404("Not Found! Please Look For Another Course")
        #return HttpResponse(course_dict.get(item, "Not Found!"))

def multiply_view(request, num1, num2):
    return HttpResponse(f"{num1} * {num2} = {num1 * num2}")

#--------------------------REDIRECT---------------------------------------

def course_number_view(request, num1):

    course_list = list(course_dict.keys())
    try:
        course = course_list[num1]
        page_to_go = reverse("course", args = [course])
        return HttpResponseRedirect(page_to_go)
    except:
        return HttpResponseNotFound("Not Found! Please Look For Another Course")


