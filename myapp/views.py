from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html") 
def login(request):
    print(request.method)
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get('username')
        pwd = request.POST.get('password')
        if name == "jomol" and pwd =="jo123":
            return render(request,'home.html')
        else:
            print("please login")
            return render(request,'login.html',{'status':'invalid'})
                
    return render(request,"login.html")   
def username(request):
    return render(request,"username.html")   
def goal(request):
    return render(request,"goal.html")            