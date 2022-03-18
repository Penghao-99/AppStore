from django.shortcuts import render, redirect
from django.db import connection

# Create your views here.
def Customers(request):
    """Shows the main page"""

    ## Delete customer
    if request.POST:
        if request.POST['action'] == 'delete':
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM customers WHERE email = %s", [request.POST['email']])

    ## Use raw query to get all objects
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM customers ORDER BY email")
        customers = cursor.fetchall()

    result_dict = {'records': customers}

    return render(request,'app/Customers.html',result_dict)

# Create your views here.
def view(request, id):
    """Shows the main page"""
    
    ## Use raw query to get a customer
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM customers WHERE email = %s", [id])
        customer = cursor.fetchone()
    result_dict = {'cust': customer}

    return render(request,'app/view.html',result_dict)

def view_Listings(request, id):
    """Shows the main page"""
    
    ## Use raw query to get a customer
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM listings WHERE owner = %s", [id])
        customer = cursor.fetchone()
    result_dict = {'cust': customer}

    return render(request,'app/view_Listings.html',result_dict)

# Create your views here.
def add(request):
    """Shows the main page"""
    context = {}
    status = ''

    if request.POST:
        ## Check if customerid is already in the table
        with connection.cursor() as cursor:

            cursor.execute("SELECT * FROM customers WHERE email = %s", [request.POST['email']])
            customer = cursor.fetchone()
            ## No customer with same id
            if customer == None:
                ##TODO: date validation
                cursor.execute("INSERT INTO customers VALUES (%s, %s, %s, %s, %s, %s, %s)"
                        , [request.POST['first_name'], request.POST['last_name'], request.POST['username'],
                           request.POST['dob'] , request.POST['password'], request.POST['confirmPassword'], request.POST['email'] ])
                return redirect('Customers')    #was return redirect('index')
            else:
                status = 'Customer with email %s already exists' % (request.POST['email'])


    context['status'] = status
 
    return render(request, "app/add.html", context)

# Create your views here.
def edit(request, id):
    """Shows the main page"""

    # dictionary for initial data with
    # field names as keys
    context ={}

    # fetch the object related to passed id
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM customers WHERE email = %s", [id])
        obj = cursor.fetchone()

    status = ''
    # save the data from the form

    if request.POST:
        ##TODO: date validation
        with connection.cursor() as cursor:
            cursor.execute("UPDATE customers SET first_name = %s, last_name = %s, username = %s, dob = %s, password = %s, confirmPassword = %s, email = %s WHERE email = %s"
                    , [request.POST['first_name'], request.POST['last_name'], request.POST['username'],
                        request.POST['dob'] , request.POST['password'], request.POST['confirmPassword'], request.POST['email'], id ])
            status = 'Customer edited successfully!'
            cursor.execute("SELECT * FROM customers WHERE email = %s", [id])
            obj = cursor.fetchone()


    context["obj"] = obj
    context["status"] = status
 
    return render(request, "app/edit.html", context)



def Listings(request):
    ## Use raw query to get all objects
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM listings ORDER BY owner")
        customers = cursor.fetchall()

    result_dict = {'records': customers}
    
    return render(request,'app/Listings.html',result_dict)

def Unavailable(request):
    ## Use raw query to get all objects
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM unavailable ORDER BY car_vin")
        customers = cursor.fetchall()

    result_dict = {'records': customers}
    
    return render(request,'app/Unavailable.html',result_dict)

def Rentals(request):
    ## Use raw query to get all objects
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM rentals ORDER BY car_vin")
        customers = cursor.fetchall()

    result_dict = {'records': customers}
    
    return render(request,'app/Rentals.html',result_dict)
