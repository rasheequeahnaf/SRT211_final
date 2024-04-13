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
 # vl = value
 # ret = return
 # var = variable
 #


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
dt_quality = {"Basic": 0.00, "Standard": 15.00, "Premium": 30.00 } # dt = dictionary 

#___________________________________#
dt_vhcl_sz = { # dt = dictionary , vhcl = Vehicle, sz = Size
    "Sedan": 1.00, "Mid-Size Sedan": 1.13, "Hatchback": 1.20,
    "Small SUV": 1.28, "Mid-Size SUV": 1.37, "Large SUV": 1.49,
    "Truck": 2.36, "Tow Truck": 3.99, "Small Bus": 4.78, "Large Bus": 7.45}


##################_Function_##################
 
def pr_mn(): # pr = print , mn = menu
    ret_var = "" # str variable used for returning keys as an string output of selected dictionary
    
    return ret_var

##################_Function_##################
 
def slt_srvc():
    ret_var = 0.0 # float variable used for returning price of the selected item
    
    return ret_var

##################_Function_##################
 

