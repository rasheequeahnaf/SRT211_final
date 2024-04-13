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
 # prmtr = prmtreter
 # ql = quality
 # tmp = temporary

# variables

gd_tl = 0.00                        # variable to store grand total price for all items in cart                                                          => refer to line 
tl_srvc = 0                         # Total Services chosen by the customer                                                                              => refer to line 
booking_state = True                # Starts as if the booking is going on and helps end the program when booking done                                   => refer to line 
phase = 0                           # Phase variable is a way for the program to understand which dictionary will be shown to the user for interaction   => refer to line 
ql_srvc = 1.00                      # quality of service is set to Basic by default unless user decides to change it                                     => refer to line 66
v_sz = 1.00                         # vehicle size is set to Sedan by default unless changed by user                                                     => refer to line 69

#___________________________________# # temporary list to hold the services selected by customer                                                         => refer to line 
all_slt_srvc = []                   # this empty list will save the services chosen by customer until customer decides to checkout                       => refer to line 

# Defining dictionaries for services, additional options, and service tiers with their prices

#___________________________________# this dictionary holds the first choice list shown to customers. 'None' type values has been used to prevent misuse of the code making it harder to modify
dt_choices = {"Primary Services":None, "Additional Services":None, "Quality of Service":None, "Choose Your Vehicle Size":None, "Checkout!":None}

#___________________________________# this dictionary holds the primary servicing options as keys with their prices as values
dt_srvc = { # dt = dictionary , srvc = service
    "Oil Change": 70.00,  "Tire Rotation": 60.00,  "Brake Inspection": 40.00, 
    "Engine Tuning": 300.00, "Top-up Fluids": 20.00, "Allignment": 120.00,
    "Winter Tire Change": 75.00, "Body damage repair": 3200.00, "Insurance Claim++": 300.00,
    "Warranty Renewal": 335.00, "Vehicle Safety": 100.00, "General inspection": 135.00 }

#___________________________________# this dictionary holds additional services in same formation as dt_service                                         => refer to line 52
dt_ext = { # dt = dictionary , ext = extras
    "Car Wash": 20.00, "Interior Detailing": 30.00, "Engine bay Wash": 25.00, "Window Tint": 200.00,
    "Paint Protection": 2859.00, "Vehicle vinyl wrapping": 7800.00, "Paint Correction" : 400.00, 
    "Engine Check": 340.00, "Tow Hitch installation": 1200.00, "Camping extras for Summer": 3795.00}

#___________________________________# this dictionary holds quality of service and values are the multiplication factors. 
dt_quality = {"Basic": 1.00, "Standard": 1.38, "Premium": 3.47 } # if some one choses basic, price will remain normal. if they choose premium, price will increase 3.47 times

#___________________________________# this dictionary holds the size of cars customers have. the same logic is used as dt_quality. higher values increase prices
dt_vhcl_sz = { # dt = dictionary , vhcl = Vehicle, sz = Size 
    "Sedan": 1.00, "Mid-Size Sedan": 1.13, "Hatchback": 1.20,
    "Small SUV": 1.28, "Mid-Size SUV": 1.37, "Large SUV": 1.49,
    "Truck": 2.36, "Tow Truck": 3.99, "Small Bus": 4.78, "Large Bus": 7.45}

##################_Function_################## 

def wlc_msg():
    print (  "-----------------------------------") # this function is for decoration purposes only
    print (  "|        Phynix Auto Group        |")
    print (  "|                                 |")
    print (  "|  Welcome to our Booking system  |")
    print (  "|                                 |")
    print (  "-------~~~~~~~~~~~~~~~~~~~~--------")
    print (  "|      | Established 1946 |       |")
    print (  "-------~~~~~~~~~~~~~~~~~~~~--------")

##################_Function_##################

def fkbv(prmtr1, prmtr2): # fetch key by value function: This function will fetch the keys using the stored values in variables  => refer to line 41, 42
    
    for k, v in prmtr1.items(): # checking and sorting the correct key using the stored value to show in final_output() => refer to line 
        
        if v == prmtr2: # iterating and checking
                            
            return k
        
    return "" # avoiding 'None' output

##################_Function_##################
 
def gvbi(prmtr1, prmtr2): # get values by index function ( dictionary, index int. This function is a helper function. it is not needed but provided for better classification of code
    
    tmp_var = list(prmtr1.values())     # tmp_var is standard variable name used in this python file for temporary variables. values are being saves in a list format then returned 
    
    return tmp_var[prmtr2]              # returning according to positionin the temporary list

##################_Function_##################
 
def gkbi(prmtr1, prmtr2): # get key by index function
    
    keys_list = list(prmtr1.keys())     # similar to gvbi() => refer to line 100
    
    return str(keys_list[prmtr2])       # concatenation to avoid error while returning data from temporary list

##################_Function_##################
 
def pr_mn(prmtr): # pr = print , mn = menu. This function prints menu items from dictionaries relative to customers navigation requirements
    ret_var = "\n"                                          # str variable used for returning strings and keys as an string output of selected dictionary
    ret_var += "\n  Total items in Cart: " + str(tl_srvc)   # ret_var = return variable
    ret_var += "\n  Total price: " + str(gd_tl)
    ret_var += "\n  Please select from the Following\n"
    ret_var += "\n  Note: Select your vehicle size and desired quality of service"
    ret_var += "\n  Default vehicle size is Sedan and quality of service is Basic\n" # => refer to line 41, 42
    
    count = 1 # counter for loop
    
    for key in prmtr.keys():
        
        ret_var += "\n" + str(count) + "  " + str(key) # storing and printing the keys one by one using ret_vat 
        
        count += 1 # counter increment
    
    print (ret_var)
    
##################_Function_##################

def choice(prmtr):
    global phase            # accessing phase to edit later
    
    pr_mn(prmtr)            # printing menu using provided prmtr = parameter
    
    tmp_var1 = None         # initiate empty variable
    
                            # Validate user input
    while tmp_var1 is None:
        
        tmp_var1 = input("\n  What option? Ans: ") # taking user input.
        
        if not tmp_var1.isdigit() or not (1 <= int(tmp_var1) <= len(prmtr)): # checking if variable is a valid digit of in range to be considered valid
            
            print("\n  Invalid input - Try Again") # error message: same as => refer to line 209
            
            tmp_var1 = None # keeping variable unchanged
    
    # Convert the validated input to an integer
    tmp_var2 = int(tmp_var1)
    
    # Check the current phase and execute the corresponding function
    if phase == 0:              # program launches with phase 0 = default landing menu page => refer to line 40, 50. (phase resets to zero by user demands)
        if tmp_var2 == 1:
            phase = 1           # setting phase to 1 to make sure the next screen is forwarded to curresponding dictionary menu output
        elif tmp_var2 == 2:
            phase = 2           # => refer to line 160
        elif tmp_var2 == 3:
            phase = 3           # => refer to line 160
            set_ql_srvc()       # running this function to select and store the desired service quality preferred by customer
            phase = 0           # resetting phase to show => refer to line 158
        elif tmp_var2 == 4:
            phase = 4           # => refer to line 160
            set_v_sz()          # => refer to line 165 this function is for vehicle size selection
            phase = 0           # => refer to line 170
        elif tmp_var2 == 5:
            phase = 5
            return tmp_var2     # returning 5 to close while loop in "__main__"
    elif phase in [1, 2]:       # if the phase is 1 or 2, user input will be forwarded to select desired service for the user
        slt_srvc(tmp_var2, prmtr)   
        phase = 0               # => refer to line 158

    return tmp_var2
    
##################_Function_##################

def set_v_sz(): # this function sets the vehicle size variable according to users wish
    global v_sz, phase

    tmp_var = choice(dt_vhcl_sz) # provides users with their choice of dictionary keys
    
    # Check if the return value from choice is valid
    if tmp_var is not None and isinstance(tmp_var, int):
        
        # Update vehicle size using the selected index
        v_sz = float(gvbi(dt_vhcl_sz, tmp_var - 1))
    
    # Reset the phase to 0 after vehicle selection is done
    phase = 0 
    
##################_Function_##################

def set_ql_srvc(): # this function store quality of service  => refer to line 182
    global ql_srvc, phase
    
    # Perform the choice function to get user selection
    tmp_var = choice(dt_quality)
    
    # Validate the selection
    # Verify that the user's selection is valid: it must be an integer and fall within the range of available quality options.

    if tmp_var is not None and isinstance(tmp_var, int) and 1 <= tmp_var <= len(dt_quality):
        
        # Update quality of service using the selected index
        ql_srvc = float(gvbi(dt_quality, tmp_var - 1))
        
    else:
        print("\n  Invalid input - Try Again")
        # Prompt the user again if the choice is invalid
        
        set_ql_srvc()
    
    # Reset the phase to 0 in either case (whether choice was valid or invalid)
    phase = 0


##################_Function_##################
 
def slt_srvc(prmtr1, prmtr2): # selected service price will be fetched and recorded
    
    global all_slt_srvc, phase, tl_srvc # => refer to line 137
    
    tmp_var = gkbi(prmtr2, prmtr1-1) # using get keys by index from user desired input to store selected service in the temporary list in line 45
    
    all_slt_srvc.append(tmp_var)
    
    tmp_var2 = float(gvbi(prmtr2, prmtr1-1))
    
    rec_tl_prc(tmp_var2)
    
    print( "|===================================================================================")
    print(f"|=> You have added '{tmp_var}' service to your cart successfully! <=")
    print( "|===================================================================================")
    
    tl_srvc += 1
    
    phase = 0

##################_Function_##################
 
def rec_tl_prc(var): # Adding total price as we move forward
    
    global gd_tl
    
    gd_tl += var
 
##################_Function_##################
 
def checkout():
    global phase, booking_state
    
    print(        "\n|---------------------------------------------------->|")
    
    tmp_var = input("| Would you like to book more services? Ans [Y/N]: ")
    
    print(          "|---------------------------------------------------->|")
    
    if tmp_var == "Y" or tmp_var == "y":
        
        phase = 0
        
        booking_state = True
        
    elif tmp_var == "N" or tmp_var == "n":
        
        booking_state = False
        
        Final_Output()
        print(      "  ___________________________________________________________________________")
        
        exit()
    
    return ""

##################_Function_##################

def Final_Output():
    
    ret_var = "" # str variable used for returning keys as a string output of selected dictionary
    
    tmp_var1 = fkbv(dt_vhcl_sz, v_sz)
    tmp_var2 = fkbv(dt_quality, ql_srvc)
    tmp_var3 = gd_tl * v_sz * ql_srvc
    
    decor = 0
    for p in all_slt_srvc:
        
        if decor == len(all_slt_srvc) -1:
            ret_var+="| "+p
        else:
            ret_var+="| "+p+"\n"
        decor += 1    
        
    
        
    print ("\n  You have selected the following services")
    print ("\n|=================================|")
    print (ret_var)
    print ("|=================================|")
    print (f"\n  Total Cost of {tmp_var2} quality service(s) for your {tmp_var1} will be: ${tmp_var3:.2f}")
    
##################_Function_##################

##################_Function_##################

if __name__ == "__main__":
    
    tmp_var = None
    
    wlc_msg()
    
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
        
            choice(tmp_var)
        
        
        
    
    