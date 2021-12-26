# Tamsin Rogers
# Fall 2019
# CS 152 
# Project 2: Extracting Information
# Part 8 - extract two other variables to plot
# Run the program from the Terminal by entering "python3 extract2.py"

#main function here

def main():
    """The main function opens the GoldieMLRCJuly.csv file, writes and opens the extract2.csv file, and 
    writes headers for date/time, wind direction, and wind speed to the new file.  This function
    contains variable assignments for the corresponding columns of data in the files,
    a while loop, and multiple if statements to search for data points of wind direction
    and speed and write them to the new file."""
    fp = open( "GoldieMLRCJuly.csv", "r" )
    #opens GoldieMLRCJuly.csv
    fp2 = open( 'extract2.csv', 'w' )
    #writes the new file extract2.csv
    fp2.write("Date/Time" + "," + "Wind Direction" + "," + "Wind Speed" + "\n")
    #writes headers for date/time, wind direction, and wind speed onto extract2.csv
    
    # main code here
    #reads one line of the file
    line = fp.readline()    #assigns the readline() function to the variable line 
    line = fp.readline()
    
    while len(line) > 0:    #runs the loop through every line in the data set
        
        words = line.split(",") #separates the following values with a comma
        time0 = "0:03"      #assigns the string value time 0:03 to the variable time0
        time4 = "4:03"      #assigns the string value time 4:03 to the variable time4
        time8 = "8:03"      #assigns the string value time 8:03 to the variable time8
        time12 = "12:03"    #assigns the string value time 12:03 to the variable time12
        time16 = "16:03"    #assigns the string value time 16:03 to the variable time16
        time20 = "20:03"    #assigns the string value time 20:03 to the variable time20
        time24 = "24:03"    #assigns the string value time 24:03 to the variable time24
    
        datetime = words[0] #assigns the values in the first column of data to the variable datetime
        windspeed = float(words[6]) #assigns the values in the seventh column of data to the variable windspeed and casts them to floats
        winddirection = float(words[7]) #assigns the values in the eighth column of data to the variable winddirection and casts them to floats
        line = fp.readline()
        
        #checks to see if each time interval is contained in the original data set, and extracts the date/time, wind speed, and wind direction values if it is
        if time0 in datetime:
            fp2.write(datetime + "," + str(windspeed) + "," + str(winddirection) + "\n")
        if time4 in datetime:
            fp2.write(datetime + "," + str(windspeed) + "," + str(winddirection) + "\n")
        if time8 in datetime:
            fp2.write(datetime + "," + str(windspeed) + "," + str(winddirection) + "\n")
        if time12 in datetime:
            fp2.write(datetime + "," + str(windspeed) + "," + str(winddirection) + "\n")
        if time16 in datetime:
            fp2.write(datetime + "," + str(windspeed) + "," + str(winddirection) + "\n")
        if time20 in datetime:
            fp2.write(datetime + "," + str(windspeed) + "," + str(winddirection) + "\n")
        if time24 in datetime:
            fp2.write(datetime + "," + str(windspeed) + "," + str(winddirection) + "\n")
            
    fp.close()  #closes GoldieMLRCJuly.csv
    fp2.close() #closes extract2.csv
    
# only execute main if this file was executed
if __name__ == "__main__":
    main()