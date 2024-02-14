from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .models import Patient, Doctor, Appointment, Vitals
from django.contrib import messages
# Create your views here.


#
#patients = [
#    {"id" : 1, "name" : "Aliaan"},
#    {"id" : 2, "name" : "Jonathan"},
#    {"id" : 3, "name" : "Sondre"},
#
#]


def home(request):
    patients  = Patient.objects.all()
    context = {"patients" : patients}
    return render(request, 'base/home.html', context)

def patient(request, pk):
    patient = Patient.objects.get(id=pk)
    context = {'patient':patient}
    return render(request, 'base/patient.html', context)

def about(request):
    return render(request, "base/about.html")

def contact(request):
    return render(request, "base/contact.html")



# Function for logging in a user
def loginPage(request):
    
    # sets the variable page to specify that this is a login page, it is passed into the context variable, and used in the html to run the correct code.
    page = 'login'
    
    # If the user is already logged in and tries to click on the login button again, they will just get redirected to home instead. 
    if request.user.is_authenticated:
        return redirect('home')
    
    # Checks if a POST request was sent. 
    if request.method == 'POST':
        # Get the username and password from the data sent in the POST request. 
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        
        # Checks if the user exists with a try catch block. 
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        
        # Gets user object based on username and password.
        # Authenticate method will either give us an error or return back a user that matches the credentials (username and password).
        user = authenticate(request, username=username, password=password)
        
        # Logs the user in if there is one, and returns home. 
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exist')
                
    
    context = {'page' : page}
    return render(request, 'base/login_register.html', context)    

# Function for logging out a user. 
def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    # else is used in the html, so no need for a page variable here. 
    form = UserCreationForm()
    
    # Check if method is a POST request
    if request.method == 'POST':
        form = UserCreationForm(request.POST) # passes in the data: username and password into user creation form
        # Checks if the form is valid
        if form.is_valid():
            user = form.save(commit=False) # saving the form, freezing it in time. If the form is valid, the user is created and we want to be able to access it right away. This is why we set commit = False
            user.username = user.username.lower() # Now that the user is created, we can access their credentials, like username and password. We lowercase the username of the user. 
            user.save() # saves the user. 
            login(request, user) # logs the user in.
            return redirect('home') # sends the user back to the home page.
        else: 
            messages.error(request, 'An error occurred during registration')
            
    context = {'form' : form}
    return render(request,'base/login_register.html', context)


def viewDoctor(request):
    
    doctors = Doctor.objects.all()
    
    context = {'doctors' : doctors}
    return render(request,'base/view_doctor.html', context)
    

def viewPatient(request):
    
    patients = Patient.objects.all()
    
    context = {'patients' : patients}
    return render(request,'base/view_patient.html', context)
    

def viewAppointment(request):
    
    appointments = Appointment.objects.all()
    
    context = {'appointments' : appointments}
    return render(request,'base/view_appointment.html', context)
    

def viewVitals(request):
    
    vitals = Vitals.objects.all()

    context = {'vitals' : vitals}
    return render(request,'base/view_vitals.html', context)


def addDoctor(request):
    
    if request.method == "POST":
        name = request.POST['name']
        contact = request.POST['contact']
        specialization = request.POST['specialization']
        
        Doctor.objects.create(name=name, mobile=contact, specialization = specialization)
        return redirect("home")
    
    return render(request, 'base/add_doctor.html')


def addPatient(request):
    
    if request.method == "POST":
        name = request.POST['name']
        gender = request.POST['gender']
        address = request.POST['address']
        mobile = request.POST['mobile']
        
        Patient.objects.create(name=name, gender=gender, address=address, mobile=mobile)
        return redirect("home")
    
    return render(request, 'base/add_patient.html')


def addAppointment(request):
    
    if request.method == "POST":
        name = request.POST['name']
        gender = request.POST['gender']
        address = request.POST['address']
        mobile = request.POST['mobile']
        
        Patient.objects.create(name=name, gender=gender, address=address, mobile=mobile)
        return redirect("home")
    
    return render(request, 'base/add_patient.html')
