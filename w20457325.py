# I declare that my work contains no examples of misconduct, such  as plagarism, or collusion
# Any code taken from other sources is referenced within my code solution
# Student ID: w20457325
# Date: 23/11/2023
from validation import validate_credits #import the function from the file validation.py
from graphics import * # import * from the file graphics
from histogram_function import histogram_bars #import histogram_bars function from the histogram_function.py file

# Initialize counts for different progression outcomes and the number of run times
run_count = 0 
progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0 

# This will save data to a text file.
#Parameters:
  #filename (str): The name of the file to save the data.
  #data (list): The list of data to be saved.
#The function opens the specified file in write mode ('w') and writes each item in the data list as a comma-separated string on a new line.
def save_to_txt(filename, data):
    with open(filename, 'w') as file:
        for item in data:
            file.write(','.join(map(str, item)) + '\n')
#This loads the data from a text file.

    #Parameters:
    #filename (str): The name of the file to load data from.
    #Returns:
   #data (list): The loaded data as a list of lists.

    #The function tries to open the specified file in read mode ('r') and reads each line, converting comma-separated values to integers and creating a list of lists.
    #If the file is not found, an empty list is returned.
def load_from_txt(filename):
    data = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                data.append(list(map(int, line.strip().split(','))))
    except FileNotFoundError:
        pass
    return data

#Loads existing data from the text file "student_data.txt"
big_list = load_from_txt("student_data.txt")

#Creating the main histograms, firstly establishing main and global so that those variables are global and creating a graphics window

def main():
    global run_count, progress_count, trailer_count, retriever_count, exclude_count
    win = GraphWin("Histogram", 800, 600)
    win.setBackground("azure")
    #Create and display the heading text
    heading = Text(Point(350, 30), "Students Progression Outcomes")
    heading.draw(win)
    #Customise the heading text with specific customisations - font style and size

    heading.setSize(22)
    heading.setStyle("italic")
    heading.setFace("helvetica")
    #Display histogram bars for each different progression outcomes
    histogram_bars(win, 56, progress_count, "green", "Progress")
    histogram_bars(win, 156, trailer_count, "blue", "Module Trailer")
    histogram_bars(win, 306, retriever_count, "black", "Module Retriever")
    histogram_bars(win, 456, exclude_count, "red", "Exclude")
    #Display text labels for each progression outcome with the actual progression outcome
    progress_text = Text(Point(70, 460), f"Progress: {progress_count}")
    progress_text.setSize(10)
    progress_text.draw(win)
    
    trailer_text = Text(Point(170, 460), f"Trailer: {trailer_count}")
    trailer_text.setSize(10)
    trailer_text.draw(win)
    
    retriever_text = Text(Point(320, 460), f"Retriever: {retriever_count}")
    retriever_text.setSize(10)
    retriever_text.draw(win)
    
    exclude_text = Text(Point(470, 460), f"Exclude: {exclude_count}")
    exclude_text.setSize(10)
    exclude_text.draw(win)
    #Display text showing the total number of outcomes
    run_text = Text(Point(420, 560), f"The total number of outcomes is {run_count}")
    run_text.setSize (20)
    run_text.draw(win)


    win.getMouse() #This is for the window to continue running
#start an empty set which can be used to store the lists of outcomes
big_list = []


while True:
    print ("Hello Welcome to the University Progression Programme") #Introduction for users
    print ("Please enter your university credits at each level to get your progression outcome, making sure that each credit is an integer: ")
    mini_list = validate_credits() #This is to import the function and use the validate function
    
    # The following outcomes are stored as variables to be easily used for when the if statements conditions are met, therefore when the variables meet a certain condition only then
    outcome_1 = ("Progress") 
    outcome_2 = ("Progress (module trailer)")
    outcome_3 = ("Did not progress - Module Retriever")
    outcome_4 = ("Exclude")
    #Check if the entered credits are valid 
    if mini_list != False:
        big_list.append (mini_list) #Determine progression outcomes based on the entered credits
        if mini_list[0] == 120: 
            print ("Your progression outcome is: " + outcome_1)
            progress_count += 1
            run_count += 1
        elif mini_list[0] == 100:
            print ("Your progression is: " + outcome_2)
            trailer_count += 1
            run_count += 1
        elif mini_list[2] >= 80:
            print("Your progression is: " + outcome_4)
            exclude_count += 1 
            run_count +=1 
        else: 
            print ("Your progression outcome is: " + outcome_3)
            retriever_count += 1
            run_count += 1


    user_input = input("Do you want to continue? (y - yes /q - quit): ") # if only the user clicks q then program will exit and data will be saved
    if user_input == "q":
        print ("Exiting the program")
        print (run_count, "is the number of students you have entered data for") #Shows the total number of outcomes/ times the program was run
        save_to_txt("student_data.txt", big_list) # Saves data to the text file before exiting
        for i in big_list:
            print (i)
        break
if __name__ == "__main__":
    main()
# This is to ensure that only after the program has been the main program directly has been run only then will the program run
