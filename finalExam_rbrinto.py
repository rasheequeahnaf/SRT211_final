#!/usr/bin/env python3

# Author: Rasheeque Ahnaf Brinto
# Student ID: 154***600
# Topic: Final Exam
# Course: SRT211
#
# Description: Python program for a local vehicle maintenance shop that wants to digitize their service booking system
# to improve service efficiency and customer experience. This program is menu-driven, allowing customers to select 
# from a range of vehicle services, additional options, and service tiers, each affecting the total price of the booking.
#
# Usage: ./<filename>.py

# Following keywords are universal throughout the whole code
# Keywords have been shortened to avoid plagiarism

 # dt = dictionary
 # srvc = service
 # ext = extras 
 # sz = size
 # mn = menu
 # slt = select
 # pr = print
 # prc = price
 # vl = value
 # ret = return
 # var = variable
 # tl = total
 # rec = record
 # gd = grand
 # prmtr = parameter
 # ql = quality
 # tmp = temporary

# variables

gd_tl = 0.00 # variable to store grand total
tl_srvc = 0 # Total Services chosen
booking_state = True # Starts as if the booking is going on and helps end the program when booking done
phase = 0
ql_srvc = 3.47 # quality of service
v_sz = 1.28 # vehicle size

#temporary list to hold the services selected by customer
#___________________________________#
all_slt_srvc = []


# Defining dictionaries for services, additional options, and service tiers with their prices

#___________________________________#
dt_choices = {"Primary Services":None, "Additional Services":None, "Quality of Service":None, "Choose Your Vehicle Size":None, "Checkout!":None}

#___________________________________#
dt_srvc = { # dt = dictionary , srvc = service
    "Oil Change": 70.00,  "Tire Rotation": 60.00,  "Brake Inspection": 40.00, 
    "Engine Tuning": 300.00, "Top-up Fluids": 20.00, "Allignment": 120.00,
    "Winter Tire Change": 75.00, "Body damage repair": 3200.00, "Insurance Claim Service+": 300.00,
    "Warranty Renewal": 335.00, "Vehicle Safety": 100.00, "General inspection": 135.00 }

#___________________________________#
dt_ext = { # dt = dictionary , ext = extras
    "Car Wash": 20.00, "Interior Detailing": 30.00, "Engine bay Wash": 25.00, "Window Tint": 200.00,
    "Paint Protection": 2859.00, "Vehicle vinyl wrapping": 7800.00, "Paint Correction" : 400.00, 
    "Engine Check": 340.00, "Tow Hitch installation": 1200.00, "Camping extras for Summer": 3795.00}

#___________________________________#
dt_quality = {"Basic": 1.00, "Standard": 1.38, "Premium": 3.47 } # dt = dictionary 

#___________________________________#
dt_vhcl_sz = { # dt = dictionary , vhcl = Vehicle, sz = Size
    "Sedan": 1.00, "Mid-Size Sedan": 1.13, "Hatchback": 1.20,
    "Small SUV": 1.28, "Mid-Size SUV": 1.37, "Large SUV": 1.49,
    "Truck": 2.36, "Tow Truck": 3.99, "Small Bus": 4.78, "Large Bus": 7.45}

##################_Function_##################

def wlc_msg():
    print (  " ---------------------------------")
    print (  "|        Phynix Auto Group        |")
    print (  "|                                 |")
    print (  "|  Welcome to our Booking system  |")
    print (  "|                                 |")
    print (  " ------~~~~~~~~~~~~~~~~~~~~--------")
    print (  "|      | Established 1946 |       |")
    print (  " ------~~~~~~~~~~~~~~~~~~~~--------")

##################_Function_##################

def fkbv(prmtr1, prmtr2): # fetch key by value function
    for k, v in prmtr1.items():
        if v == prmtr2:
            return k
    return "" 

##################_Function_##################
 
def gvbi(param1, param2): # get values by index function
    # This function is a helper function. it is not needed but provided for better classification of code
    tmp_var = list(param1.values())
    return tmp_var[param2]

##################_Function_##################
 
def gkbi(param1, param2): # get key by index
    keys_list = list(param1.keys())
    return str(keys_list[param2])

##################_Function_##################
 
def pr_mn(prmtr): # pr = print , mn = menu
    ret_var = "\n" # str variable used for returning keys as an string output of selected dictionary
    ret_var += "\n  Total items in Cart: " + str(tl_srvc)
    ret_var += "\n  Total price: " + str(gd_tl)
    ret_var += "\n  Please select from the Following\n"
    ret_var += "\n  Note: Select your vehicle size and desired quality of service"
    ret_var += "\n  Default vehicle size is Sedan and quality of service is Basic\n"
    
    count = 1
    for key in prmtr.keys():
        ret_var += "\n" + str(count) + "  " + str(key)
        count += 1
    
    print (ret_var)
    choice(prmtr)
    
##################_Function_##################

def choice(prmtr):
    
    tmp_var = 0
    
    while int(tmp_var) <= 0 or int(tmp_var) >= len(prmtr):
        
        tmp_var = input("\n  What option? Ans: ")
    
##################_Function_##################
 
def slt_srvc(param1, param2): # selected service price will be fetched and recorded
    
    global all_slt_srvc
    
    all_slt_srvc.append(gkbi(param2, param1-1))
    
    tmp_var = float(gvbi(param2, param1-1))
    
    rec_tl_prc(tmp_var)

##################_Function_##################
 
def rec_tl_prc(var): # Adding total price as we move forward
    
    global gd_tl
    
    gd_tl += var
    
    pass # Nothing is returned
 
##################_Function_##################
 
def checkout():
    global phase, booking_state
    
    ret_var = "" # str variable used for returning keys as a string output of selected dictionary
    
    tmp_var = input("\n  Would you like to book more services? Ans [Y/N]: ")
    
    if tmp_var == "Y" or tmp_var == "y":
        
        phase = 0
        
        booking_state = True
        
    elif tmp_var == "N" or tmp_var == "n":
        
        booking_state = False
        
        Final_Output()
        exit()
    
    return ret_var

##################_Function_##################

def Final_Output():
    
    ret_var = "" # str variable used for returning keys as a string output of selected dictionary
    
    tmp_var1 = fkbv(dt_vhcl_sz, v_sz)
    tmp_var2 = fkbv(dt_quality, ql_srvc)
    tmp_var3 = gd_tl * v_sz * ql_srvc
    
    for p in all_slt_srvc:
        ret_var+="\n  "+p
        
        
    print ("\n  You have selected the following services")
    print (ret_var)
    print (f"\n  Total Cost of '{tmp_var2}' quality service(s) for your '{tmp_var1}' will be: '{tmp_var3:.2f}'")
    
##################_Function_##################

def isInt(prmtr):
    try:
        # Attempt to convert the string to an integer
        int(prmtr)
        # If successful, return True
        return True
    except ValueError:
        # If a ValueError occurs, return False
        return False

##################_Function_##################

if __name__ == "__main__":
    
    wlc_msg()
    
    tmp_var = None
    
    while booking_state != False:
        if phase == 0:
            tmp_var = dt_choices
        elif phase == 1:
            tmp_var = dt_srvc
        elif phase == 2:
            tmp_var = dt_ext
        elif phase == 3:
            tmp_var = dt_quality
        elif phase == 4:
            tmp_var = dt_vhcl_sz
        elif phase == 5:
            checkout()
        
        if phase >= 0 or phase <= 4:
            pr_mn(tmp_var)
    
    