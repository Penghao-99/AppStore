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

def view_Unavailable(request, id):
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM unavailable WHERE car_vin = %s", [id])
        car_vin = cursor.fetchone()
    result_dict = {'cust': car_vin}
    
    return render(request,'app/view_Unavailable.html',result_dict)

def view_Rentals(request, id):
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM rentals WHERE car_vin = %s", [id])
        car_vin = cursor.fetchone()
    result_dict = {'cust': car_vin}
    
    return render(request,'app/view_Rentals.html',result_dict)

# Create your views here.
def add(request): #can delete
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

def add_newcustomer(request):
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
                return redirect('Customers')   
            else:
                status = 'Customer with email %s already exists' % (request.POST['email'])


    context['status'] = status
 
    return render(request, "app/add_Listing.html", context)

def add_newlisting(request):
    """Shows the main page"""
    context = {}
    status = ''

    if request.POST:
        ## Check if customerid is already in the table
        with connection.cursor() as cursor:

            cursor.execute("SELECT * FROM listings WHERE owner = %s", [request.POST['owner']])
            customer = cursor.fetchone()
            ## No customer with same id
            if customer == None:
                ##TODO: date validation
                cursor.execute("INSERT INTO customers VALUES (%s, %s, %s, %s, %s, %s, %s)"
                        , [request.POST['car_vin'], request.POST['carmake'], request.POST['model'],
                           request.POST['year'] , request.POST['mileage'], request.POST['rate'], request.POST['owner'] ])
                return redirect('Listings')    #was return redirect('index')
            else:
                status = 'Listing with owner %s and model %s already exists' % (request.POST['owner'],request.POST['model'])


    context['status'] = status
 
    return render(request, "app/add_Listing.html", context)

def add_newunavailable(request):
    """Shows the main page"""
    context = {}
    status = ''

    if request.POST:
        ## Check if customerid is already in the table
        with connection.cursor() as cursor:

            cursor.execute("SELECT * FROM unavailable WHERE car_vin = %s", [request.POST['car_vin']])
            customer = cursor.fetchone()
            ## No customer with same id
            if customer == None:
                ##TODO: date validation
                cursor.execute("INSERT INTO car_vin VALUES (%s, %s, %s)"
                        , [request.POST['car_vin'], request.POST['owner'], request.POST['unavailable'] ])
                return redirect('Unavailable')    #was return redirect('index')
            else:
                status = 'Unavailablity of owner %s and date %s already exists' % (request.POST['owner'],request.POST['unavailable'])


    context['status'] = status
 
    return render(request, "app/add_Unavailable.html", context)


def add_newrental(request):
    """Shows the main page"""
    context = {}
    status = ''

    if request.POST:
        ## Check if customerid is already in the table
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM rentals WHERE car_vin = %s AND pick_up = %s", [request.POST['car_vin'], request.POST['pick_up']])
         #   cursor.execute("SELECT * FROM rentals WHERE car_vin = %s", [request.POST['car_vin']])
            customer = cursor.fetchone()
            ## No customer with same id
            if customer == None:
                ##TODO: date validation
                cursor.execute("INSERT INTO rentals VALUES (%s, %s, %s, %s, %s, %s )"
                        , [request.POST.get('owner'), request.POST['renter'], request.POST['car_vin'],
                          request.POST['pick_up'], request.POST['drop_off'], request.POST['rental_fee']])
                return redirect('Rentals')    #was return redirect('index')
            else:
                status = 'Rental data of car VIN %s and pick-up date %s already exists' % (request.POST['car_vin'], request.POST['pick_up'])


    context['status'] = status
 
    return render(request, "app/add_Rental.html", context)

# Create your views here.
def edit_Customers(request, id):
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
 
    return render(request, "app/edit_Customers.html", context)

def edit_Listings(request, id):
    """Shows the main page"""

    # dictionary for initial data with
    # field names as keys
    context ={}

    # fetch the object related to passed id
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM listings WHERE owner = %s", [id])
        obj = cursor.fetchone()

    status = ''
    # save the data from the form

    if request.POST:
        ##TODO: date validation
        with connection.cursor() as cursor:
            cursor.execute("UPDATE listings SET car_vin = %s, carmake = %s, model = %s, year = %s, mileage = %s, rate = %s, owner = %s WHERE owner = %s"
                    , [request.POST['car_vin'], request.POST['carmake'], request.POST['model'],
                        request.POST['year'] , request.POST['mileage'], request.POST['rate'], request.POST['owner'], id ])
            status = 'Listing edited successfully!'
            cursor.execute("SELECT * FROM listings WHERE owner = %s", [id])
            obj = cursor.fetchone()


    context["obj"] = obj
    context["status"] = status
 
    return render(request, "app/edit_Listings.html", context)

def edit_Unavailable(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}

    # fetch the object related to passed id
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM unavailable WHERE car_vin = %s", [id])
        obj = cursor.fetchone()

    status = ''
    # save the data from the form

    if request.POST:
        ##TODO: date validation
        with connection.cursor() as cursor:
            cursor.execute("UPDATE unavailable SET car_vin = %s, owner = %s, unavailable = %s WHERE car_vin = %s"
                    , [request.POST['car_vin'], request.POST['owner'], request.POST['unavailable'], id ])
            status = 'Unavailable edited successfully!'
            cursor.execute("SELECT * FROM unavailable WHERE car_vin = %s", [id])
            obj = cursor.fetchone()


    context["obj"] = obj
    context["status"] = status
    return render(request, "app/edit_Unavailable.html", context)

def edit_Rentals(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}

    # fetch the object related to passed id
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM rentals WHERE car_vin = %s", [id])
        obj = cursor.fetchone()

    status = ''
    # save the data from the form

    if request.POST:
        ##TODO: date validation
        with connection.cursor() as cursor:
            cursor.execute("UPDATE rentals SET owner = %s, renter = %s, car_vin = %s, pick_up = %s, drop_off = %s, rental_fee = %s WHERE car_vin = %s"
                    , [request.POST['car_vin'], request.POST['owner'], request.POST['unavailable'], id ])
            status = 'Rental edited successfully!'
            cursor.execute("SELECT * FROM rentals WHERE car_vin = %s", [id])
            obj = cursor.fetchone()


    context["obj"] = obj
    context["status"] = status
    return render(request, "app/edit_Rentals.html", context)

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
