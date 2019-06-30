from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.views import View


def login(request):
    return render(request, "login.html")

class home(View):

    def get(self, request):
        return HttpResponse('Hello, World!get')

    def post(self, request):
        name = str(request.POST["username"])
        pwd = str(request.POST["passwd"])
        if name != None and not name.__eq__(""):
            if name == "admin" and pwd == "admin":
                return render(request, "home.html", {"test":"test"})
            else:
                return HttpResponse("0")
        else:
            return HttpResponse('0')
