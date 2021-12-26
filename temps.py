# Tamsin Rogers
# Fall 2019
# CS 152 
# Project 2: Extracting Information
# Part 4 - calculate max/min statistics
# Run the program from the Terminal by entering "python3 temps.py"

# main function here
def main():
    """The main function opens the GoldieMLRCJuly.csv file, and contains a
    while loop, and an if statement to search for data points of air temperature 
    and water temperature and calculate their high and low values."""
    # main code here
    hiairtemp = -100000#initializes hiairtemp to a large negative integer
    hiwatertemp = -100000#initializes hiwatertemp to a large negative integer
    lowairtemp = 100000#initializes lowairtemp to a large positive integer
    lowwatertemp = 100000#initializes lowwatertemp to a large positive integer
    
    hiairdate = (",")
    lowairdate = (",")
    hiwaterdate = (",")
    lowwaterdate = (",")
    
    fp = open( "GoldieMLRCJuly.csv", "r" )#opens GoldieMLRCJuly.csv
    #reads one line of the file
    line = fp.readline()#assigns the readline() function to the variable line 
    line = fp.readline()
    
    while len(line) > 0:#runs the loop through every line in the data set
        words = line.split(",")#separates the following values with a comma
        
        temp3 = float(words[1])#assigns the values in the second column of data to the variable temp3 and casts them to floats
        airtemp = float(words[5])#assigns the values in the sixth column of data to the variable airtemp and casts them to floats
        
        line = fp.readline()  
        
        if airtemp > hiairtemp:#checks if airtemp is greater than hiairtemp
            hiairtemp = airtemp#sets hiairtemp to the current airtemp value if true

        if airtemp < lowairtemp:#checks if airtemp is less than lowairtemp
            lowairtemp = airtemp#sets lowairtemp to the current airtemp value if true
            
        if temp3 > hiwatertemp:#checks if temp3 is greater than hiwatertemp
            hiwatertemp = temp3#sets hiwatertemp to the current temp3 value if true

        if temp3 < lowwatertemp:#checks if temp3 is less than lowwatertemp
            lowwatertemp = temp3#sets lowwatertemp to the current temp3 value if true
    
    print("High air temperature: ", hiairtemp)#prints the hiairtemp value with a label
    print("Low air temperature: ", lowairtemp)#prints the lowairtemp value with a label
    print("High water temperature: ", hiwatertemp)#prints the hiwatertemp value with a label
    print("Low water temperature: ", lowwatertemp)#prints the lowwatertemp value with a label
    fp.close()#closes GoldieMLRCJuly.csv
    
# only execute main if this file was executed
if __name__ == "__main__":
    main()