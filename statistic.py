# Tamsin Rogers
# Fall 2019
# CS 152 
# Project 2: Extracting Information
# Part 6 - compute a statistic of your choice - average 
# Run the program from the Terminal by entering "python3 statistic.py"

# main function here
def main():
    """The main function opens the GoldieMLRCJuly.csv file and uses a while loop 
     to read through each line of data.  This function also contains the code 
     needed to calculate the average value for wind speed throughout the month of July."""
    newwindspeed = 0#initializes newwindspeed to 0
    windsum = 0#initializes windsum to 0
    counter = 0#initializes counter to 0
    fp = open( "GoldieMLRCJuly.csv", "r" )#opens GoldieMLRCJuly.csv
    #reads one line of the file
    line = fp.readline()#assigns the readline() function to the variable line 
    line = fp.readline()
    
    while len(line) > 0:#runs the loop through every line in the data set
        words = line.split(",")#separates the following values with a comma
        windspeed = float(words[6])#assigns the values in the seventh column of data to the variable windspeed
        counter = counter + 1#increases the value of counter by increments of 1
        windsum = windsum + windspeed#sets windsum to the current value of windsum plus the newly read windspeed
        line = fp.readline()
          
    avg = (windsum/counter) #divides the final value for windsum by the number of lines calculated by counter in order to determine the average value for windspeed
    print("Average wind speed: ", avg) #prints the average value for windspeed with a label
    fp.close() #closes GoldieMLRCJuly.csv
    
# only execute main if this file was executed
if __name__ == "__main__":
    main()
    