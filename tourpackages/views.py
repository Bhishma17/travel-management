from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
from .models import *
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from datetime import datetime

# Create your views here.
def homepage(request):
    user_email = request.session.get('user_email')
    user = Register.objects.filter(email=user_email).first()
    return render(request, 'Homepage.html', {'user': user})
    # return render(request, 'Homepage.html')

def flights(request):
    return render(request, 'Flights.html')
def travelpackages(request):
    return render(request, 'Travelpackages.html')
def myregisterpage(request):
    return render(request, "myregisterpage.html")

from django.contrib.auth.decorators import login_required
@login_required(login_url='home1')
def rentcar(request):
    return render(request, "Rentcar.html")

def renthatchback(request):
    return render(request, "renthatchback.html")

def alllink(request):
    return render(request, "Alllink.html")

import datetime, time, calendar
@login_required(login_url='home1')
def date1(request):
    datetime_object = datetime.datetime.now()
    s2 = calendar.month(2023, 4)
    s1 = calendar.isleap(2005)

    context = {
        'datetime_object': datetime_object,
        's2': s2,
        's1': s1,
    }
    return render(request, "Datetime123.html", context)

def randomotp(request):
    return render(request, "Randomotp.html")

import random, string
def randomotp1(request):
    if request.method == 'POST':
        input1 = request.POST['input1']
        input2 = int(input1)
        result_str = ''.join(random.sample(string.digits, input2))
        print(result_str)
        context = {'result_str': result_str}
    return render(request, "Randomotp.html", context)

def getdate1(request):
    return render(request,'get_date.html')

def getdate2(request):
    return render(request,'result.html')

def get_date(request):
    if request.method == 'POST':
        form = IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value = form.cleaned_data['integer_value']
            date_value = form.cleaned_data['date_value']
            updated_date = date_value + datetime.timedelta(days=integer_value)

            return render(request, 'get_date.html', {'updated_date': updated_date})
        else:
            form = IntegerDateForm()
        return render(request, 'get_date.html', {'form': form})

def print1(request):
    return render(request, 'print_to_console.html')
def print_to_console(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        print(f'User input: {user_input}')
    # return HttpResponse('Form submitted successfully')
    a1= {'user_input':user_input}
    return render(request,'print_to_console.html',a1)

def my_view(request):
    # Your view logic here
    show_alert = True  # Set this based on your condition
    return render(request, 'my_template.html', {'show_alert': show_alert})

from .forms import *
import matplotlib.pyplot as plt
import numpy as np
def pie_chart(request):
    if request.method == 'POST':
        form = PieChartForm(request.POST)
        if form.is_valid():
            # Process user input
            y_values = [int(val) for val in form.cleaned_data['y_values'].split(',')]
            labels = [label.strip() for label in form.cleaned_data['labels'].split(',')]

            # Create pie chart
            plt.pie(y_values, labels=labels, startangle=90)
            plt.savefig('static/images/pie_chart.png')  # Save the chart image
            img1={'chart_image': '/static/images/pie_chart.png'}
            return render(request, 'chart_form.html', img1)
    else:
        form = PieChartForm()
    return render(request, 'chart_form.html', {'form': form})
def contactform(request):
    return render(request, 'Contact.html')

from django.core.mail import send_mail
def contactmail(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        comment = request.POST['comment']
        tosend= comment + '-------------------- This is just the copy of comment what you have posted in MMS System'
        data = contactus(firstname=firstname, lastname=lastname, email=email, comments=comment)
        data.save()
        send_mail(
            'Thank You for Contacting Deepaks Travel Tourism and Management  System',
            tosend,
            'justw9090@gmail.com',
            [email],
            fail_silently=False,
        )
        return HttpResponse("<h1><center>Mail Sent</center></h1>")
        # return render(request, 'Homepage.html')
    else:
        HttpResponse("<h1>error</h1>")



def rentcarlogic(request):
    global Total_Fare
    total_date_difference_message = ""
    # Total_Fare=10 # Define Total_Fare before the conditional block

    if request.method == 'POST':
        location1 = request.POST.get('location1')
        from_date_value = request.POST.get('from_date_value')
        to_date_value = request.POST.get('to_date_value')
        # Convert the date strings to datetime objects
        button_type = request.POST.get('button_type')
        from_date = datetime.strptime(from_date_value, "%Y-%m-%d")
        to_date = datetime.strptime(to_date_value, "%Y-%m-%d")

        # Calculate the date difference
        date_difference = (to_date - from_date).days + 1
        print(date_difference)
        total_date_difference_message = f"The date difference is {date_difference} days."
        Base_Price = 2000 * date_difference
        Driver_Allowance = 2000
        GST = (Base_Price * 5) / 100
        Total_Fare = Base_Price + Driver_Allowance + GST
        data = {'Base_Price': Base_Price, 'Driver_Allowance': Driver_Allowance, 'GST': GST, 'Total_Fare': Total_Fare}
        print(Total_Fare)
        request.session['Total_Fare'] = Total_Fare
        if button_type == 'rent_now':
            return render(request, 'renthatchback.html', data)
        elif button_type == 'proceed_to_payment':
            # request.session['Total_Fare'] = Total_Fare
            # print(Total_Fare)
            return redirect('generate_qr_code')
            # return generate_qr_code(request,Total_Fare)
    # request.session['Total_Fare'] = Total_Fare
    return render(request, 'renthatchback.html')


from django.shortcuts import render
import qrcode
from PIL import Image

def generate_qr_code(request):
    Total_Fare = request.GET.get('Total_Fare', '')
    print(f"Total Fare: {Total_Fare}")
    print(Total_Fare)
    print(request.GET)
    upi_id = 'vd@paytm'
    amount = Total_Fare

    # Format the payment URL with UPI ID and amount
    # payment_url = f'upi://pay?pa={upi_id}&mc=your_merchant_code&tid=your_transaction_id&tr=your_transaction_reference_id&tn=Payment&am={amount}&cu=INR&url=your_url'

    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(upi_id+amount)
    qr.make(fit=True)
    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    # Save the image or use it in the response
    img.save('static/images/KLU1.png')
    print('image created')

    # Add context data if needed
    context = {
        'upi_id': upi_id,
        'amount': amount,
        # 'payment_url': payment_url,
    }

    return render(request, 'generate_qr_code.html', context)

def Bookroom(request):
    return render(request, 'Bookroom.html')

import requests
def weatherpagecall(request):
    return render(request, 'weatherappinput.html')

def weatherlogic(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = '98c9fe0696484df631f05ef073b66aa4'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1= round(temperature - 273.15,2)
            return render(request, 'weatherappinput.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'weatherappinput.html', {'error_message': error_message})


from django.shortcuts import render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
def login1(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password']
        user=auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            return render(request,'Homepage.html')
        else:
            messages.info(request,'Invalid credentials')
            return render(request,'login.html')
    else:
        return render(request,'login.html')
def signup1(request):
 if request.method=="POST":
    username=request.POST['username']
    pass1=request.POST['password']
    pass2=request.POST['password1']
    if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'OOPS! Usename already taken')
                return render(request,'signup.html')
            else:
                user=User.objects.create_user(username=username,password=pass1)
                user.save()
                messages.info(request,'Account created successfully!!')
                return render(request,'login.html')
    else:
            messages.info(request,'Password do not match')
            return render(request,'signup.html')
def logout(request):
    auth.logout(request)
    return render (request,'Homepage.html')