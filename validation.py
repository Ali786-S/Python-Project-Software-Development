# validation.py
# I declare that my work contains no examples of misconduct, such  as plagarism, or collusion
# Any code taken from other sources is referenced within my code solution
# Student ID: w20457325
# Date: 23/11/2023
# Define a function to validate the credits entered
def validate_credits():
    while True:
            big_list = [] #Initialise an empty list to store the entered credits
            valid_ranges = ["0", "20", "40", "60", "80", "100", "120"] #These are the valid credit ranges

#Validate the input until it falls within the valid ranges
            p = (input("Enter the number of university credits that you have passed at: ")) #p is the input for the pass credits
            while p not in valid_ranges:
                 if p.isdigit() == False:
                      print ("Please enter integer") #these lines of code makes sure that the user enters an integer and that the input is within range
                 elif p not in valid_ranges:
                      print ("Out of Range")
                 p = (input("Enter the number of university credits that you have passed at: ")) # The user is required to input again if the conditions are not met 
            p = int(p)

#Validate the input until it falls within the valid ranges
            d = (input("Enter the number of university credits that you have deferred at: ")) #d is the input for the defer credits
            while d not in valid_ranges:
                 if d.isdigit() == False:
                      print ("Please enter integer") #these lines of code makes sure that the user enters an integer and that the input is within range
                 elif d not in valid_ranges:
                      print ("Out of Range")
                 d = (input("Enter the number of university credits that you have passed at: ")) # The user is required to input again if the conditions are not met 
            d = int(d)
#Validate the input until it falls within the valid ranges
            f = (input("Enter the number of university credits that you have failed at: ")) #f is the input for the fail credits
            while f not in valid_ranges:
                 if f.isdigit() == False:
                      print ("Please enter integer") #these lines of code makes sure that the user enters an integer and that the input is within range
                 elif f not in valid_ranges:
                      print ("Out of Range")
                 f = (input("Enter the number of university credits that you have passed at: ")) # The user is required to input again if the conditions are not met 
            f = int(f)
# The following makes sure that the total number of credits is 120, ensuring that the inputs by the user are valid
            if p + d + f == 120:
                print ("Total of credits is correct value")
                return [p, d, f]
            else:
                    print("Total Incorrect")
                    return False
                    #Total incorrect shall be displayed if the total credits is wrong and so it would be false
