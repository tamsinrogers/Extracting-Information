# Tamsin Rogers
# Fall 2019
# CS 152
# Lab 2: Searching and Splitting
# Practice with the unix tools grep, cut, and paste, and python string function split to manipulate data
# Run the program from the Terminal by entering "python3 hightemp.py"


# main function here
def main():
    """The main function opens the blend.csv file, contains variable assignments for the corresponding columns of data in the files, a while loop, and an if statement to search for the high temperature data point and print this value."""
    hitemp = -100000
    #sets the variable hitemp to a large negative integer value 
    hidate = (",")
    #separates the following values with a comma
    fp = open( "blend.csv", "r" )
    #opens the blend.csv file for reading
    line = fp.readline()
    #reads one line of the file
    line = fp.readline()
    
    while len(line) > 0:    #runs the loop through every line in the data set
        print(line) #prints the lines of the file to the terminal
        words = line.split(",")
        print(words)
        temp = float(words[3]) #assigns the values in the fourth column of data to the variable windspeed and casts them to floats
        date = (words[0])   #assigns the values in the first column of data to the variable datetime
        line = fp.readline()
        
        if temp > hitemp:   #checks if temp is greater than the initial hitemp value
            hitemp = temp   #sets hitemp to the most recently checked high temperature value in the data
            hidate = date   #sets the date of the highest temperature to the variable date

    print(hitemp)   #prints the hitemp value
    print(hidate)   #prints the hidatevalue
    print("The highest temperature of %.3f occurred on %s" % (hitemp, hidate))
    fp.close()  #closes blend.csv
    
# only execute main if this file was executed
if __name__ == "__main__":
    main()