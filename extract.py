# Tamsin Rogers
# Fall 2019
# CS 152 
# Project 2: Extracting Information
# Part 7: write a csv file with extracted data and plot it
# Run the program from the Terminal by entering "python3 extract.py"

# main function here

def main():
"""The main function opens the GoldieMLRCJuly.csv file, writes and opens the extract.csv file, and 
writes headers for date/time,and air temperature to the new file.  This function
contains variable assignments for the corresponding columns of data in the files,
a while loop, and an if statement to search for data points of air temperature and write them to the new file."""
    fp = open( "GoldieMLRCJuly.csv", "r" ) #opens GoldieMLRCJuly.csv
    fp2 = open( 'extract.csv', 'w' )	#writes the new file extract.csv
    fp2.write("Date/Time" + "," + "Air Temperature" + "\n")	#writes headers for date/time and air temperature onto extract.csv
    
    # main code here
    #reads one line of the file
    line = fp.readline()	#assigns the readline() function to the variable line 
    line = fp.readline()
    
    #extracts the data for airtemp at 3pm
    while len(line) > 0:	#runs the loop through every line in the data set
        
        words = line.split(",")	#separates the following values with a comma
        time = "15:03"	#assigns the string time value 15:03 to the variable time
        datetime = words[0]	#assigns the values in the first column of data to the variable datetime
        airtemp = float(words[5])	#assigns the values in the sixth column of data to the variable airtemp and casts them to floats
        line = fp.readline()
        
        if time in datetime: #checks to see if the time 15:03 is contained in the original data set, and extracts the date/time and airtemp values if it is
            #fp = open( 'extract.csv', 'a' )
            fp2.write(datetime + "," + str(airtemp) + "\n")
            
    fp.close()	#closes GoldieMLRCJuly.csv
    fp2.close()	#closes extract.csv
    
# only execute main if this file was executed
if __name__ == "__main__":
    main()