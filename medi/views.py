from django.shortcuts import render , HttpResponse
from appointment.models import Appointment 
from DoctorFind.models import Doctor
from Contactus.models import Contact
from products.models import Product
from Blogs.models import BlogPost
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from Precaution.models import Disease 

def disease_info(request):
    # Initialize the disease variable
    disease = None
    
    if request.method == 'POST':
        # Get the search query from the POST data
        query = request.POST.get('q')
        
        if query:
            # Try to find a disease that matches the query
            disease = Disease.objects.filter(name__icontains=query).first()
    
    # Render the 'disease_info.html' template with the disease information
    return render(request, "information.html", {'disease': disease})


@login_required(login_url='LoginPage')
def information(requests):
    return render(requests, "information.html")

def healthcare_centre(requests):
    if requests.method == 'POST':
        name = requests.POST.get('name')
        email = requests.POST.get('email')
        password1 = requests.POST.get('password1')
        password2 = requests.POST.get('password2')
        
        if password1 != password2:
            return HttpResponse("Your password and conform password are not same ")
        else:
            my_user = User.objects.create_user(name , email , password1)
            my_user.save()
            return redirect("LoginPage")
    
    return render(requests, "signup.html")
        

def LoginPage(requests):
    if requests.method == "POST":
        name = requests.POST.get('username')
        password = requests.POST.get('password')
        user = authenticate(username=name, password=password)
        if user is not None:
            login(requests , user)
            return redirect("information")
        
        else:
            return HttpResponse("Your Password is incorrect !!!")
        
        
    return render(requests, "login.html")

def LogoutPage(requests):
    logout(requests)
    return redirect('LoginPage')


def index(requests):
    return render(requests , "index.html" ) 

def about(requests):
    return render(requests , "about.html")


def saveform(requests):
    if requests.method == 'POST':
        department = requests.POST.get('department')
        doctor = requests.POST.get('doctor')
        name = requests.POST.get('name')
        email = requests.POST.get('email')
        appointment_date = requests.POST.get('appointment_date')
        appointment_time = requests.POST.get('appointment_time')
        
        ap = Appointment(department = department , doctor = doctor , name = name , email = email , appointment_date = appointment_date , appointment_time = appointment_time)
        ap.save()
        
    return render(requests , "information.html")


def blog(requests):
    blog_posts = BlogPost.objects.all()
    return render(requests, 'blog.html', {'blog_posts': blog_posts})

def contact(requests):
    return render(requests , "contact.html") 

def contact_view(requests):
    if requests.method == "POST":
        name = requests.POST.get('name')
        email = requests.POST.get('email')
        subject = requests.POST.get('subject')
        message = requests.POST.get('message')

        # Create a new Contact object and save it to the database
        ap = Contact(name=name, email=email, subject=subject, message=message)
        ap.save()
    
    return render(requests, "contact.html")

def price(requests):

    return render(requests , "price.html" ) 

def search(requests):
    return render(requests , "search.html") 


def doctorsearch(request):
    doctors = Doctor.objects.all()
    speciality = request.POST.get('speciality')
    city = request.POST.get('city')

    if speciality and speciality != "Select Specialty":
        doctors = doctors.filter(speciality=speciality)
    if city:
        doctors = doctors.filter(city__icontains=city)

    return render(request, "search.html", {'doctors': doctors})


def service(requests):
    return render(requests , "service.html") 

    
def team(requests):
    products = Product.objects.all()  # Fetch all products from the database
    return render(requests, "team.html", {'products': products})

def testimonial(requests):
    return render(requests , "testimonial.html") 