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


# Defining dictionaries for services, additional options, and service tiers with their prices

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

gd_tl = 0.00 # variable to store grand total
tl_srvc = 0 # Total Services chosen
booking_state = True # Starts as if the booking is going on and helps end the program when booking done
phase = 1
ql = 1.00 # quality of service
v_sz = 1.00 # vehicle size


print (  " ---------------------------------")
print (  "|        Phynix Auto Group        |")
print (  "|                                 |")
print (  "|  Welcome to our Booking system  |")
print (  "|                                 |")
print (  " ------~~~~~~~~~~~~~~~~~~~~--------")
print (  "|      | Established 1946 |       |")
print (  " ------~~~~~~~~~~~~~~~~~~~~--------")

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
dt_quality = {"Basic": 0.00, "Standard": 1.38, "Premium": 3.47 } # dt = dictionary 

#___________________________________#
dt_vhcl_sz = { # dt = dictionary , vhcl = Vehicle, sz = Size
    "Sedan": 1.00, "Mid-Size Sedan": 1.13, "Hatchback": 1.20,
    "Small SUV": 1.28, "Mid-Size SUV": 1.37, "Large SUV": 1.49,
    "Truck": 2.36, "Tow Truck": 3.99, "Small Bus": 4.78, "Large Bus": 7.45}


##################_Function_##################
 
def pr_mn(prmtr): # pr = print , mn = menu
    ret_var = "\n" # str variable used for returning keys as an string output of selected dictionary
    ret_var += "\n  Total items in Cart: " + str(tl_srvc)
    ret_var += "\n  Total price: " + str(gd_tl)
    ret_var += "\n  Please select from the Following\n"
    ret_var += "\n  Note: Select your vehicle size and desired quality of service\n"
    
    # print(ret_var)
    
    # count = 1
    
    # for i in range(len(prmtr)):
    #     # count = len(prmtr)
        
    #     ret_var += "\n" + str(count) + "  " + list(prmtr.keys())[int(i)]
    #     count += 1
    
    count = 1
    for key in prmtr.keys():
        ret_var += "\n" + str(count) + "  " + str(key)
        count += 1
    
    print (ret_var)
    choice(prmtr)
    

##################_Function_##################
 
def slt_srvc():
    ret_var = 0.0 # float variable used for returning price of the selected item
    
    return ret_var

##################_Function_##################
 
def rec_tl_prc(var): # Adding total price as we move forward
    global gd_tl
    gd_tl += var
    pass # Nothing is returned
 
##################_Function_##################
 
def checkout():
    ret_var = "" # str variable used for returning keys as an string output of selected dictionary
    
    print("Would you like to book more services?")
    # input = 
    
    return ret_var
 
 
##################_Function_##################

def Final_Output():
    
    exit
 
##################_Function_##################

def choice(prmtr):
    
    choice = 0
    while int(choice) <= 0 or int(choice) >= len(prmtr):
        choice = input("\n  What option? Zero for main menu. Ans: ")
    

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
    
    tmp_var = None
    
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
        Final_Output()
        
    if phase >= 0 or phase <= 4:
        pr_mn(tmp_var)