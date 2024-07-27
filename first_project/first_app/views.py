from django.shortcuts import render
from django.http import HttpResponse

course_dictionary = {
     "pyhton" : "Pyhton Course Page",
     "java" : "Java Course Page",
     "kotlin" : "Kotlin Course Page",
     "swift" : "Swift Course Page"
}

"""
# Bu da doğru
def course(request, item):
     return HttpResponse(course_dictionary[item])
"""

# Burada get metoduyla alınan item'a default bir değer atıyoruz. "Not Found"
def course(request, item):
     return HttpResponse(course_dictionary.get(item, "Not Found"))

def index(request):
    return HttpResponse("Bu benim ilk django mesajım")

"""
def pyhton_course(request):
    return HttpResponse("Pyhton Course Page")

def java_course(request):
        return HttpResponse("Java Course Page")
"""
def multiply_view(request, num1, num2):
     return HttpResponse(f"{num1}*{num2}={num1*num2}")
