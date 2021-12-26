# Tamsin Rogers
# Fall 2019
# CS 152 
# Project 2: Extracting Information
# Part 5 - calculate the number of sunny/cloudy days
# Run the program from the Terminal by entering "python3 sunny.py"

# main function here
def main():
    """The main function opens the GoldieMLRCJuly.csv file and uses a while loop 
     to read through each line of data.  This function also contains an if statement
     that determines whether or not a given day is sunny or cloudy, depending on its
     PAR value, and prints the average number of each of these types of days throughout the month of July."""
    # main code here
    sunnydays = 0
    #initializes sunnydays to 0
    cloudydays = 0
    #initializes cloudydays to 0
    sunnysum = 0
    #initializes sunnysum to 0
    cloudysum = 0
    #initializes cloudysum to 0
    avgsunny = 0
    #initializes avgsunny to 0
    avgcloudy = 0
    #initializes avgcloudy to 0

    fp = open( "GoldieMLRCJuly.csv", "r" )
    #opens GoldieMLRCJuly.csv
    #reads one line of the file
    line = fp.readline()#assigns the readline() function to the variable line 
    line = fp.readline()
    
    while len(line) > 0:#runs the loop through every line in the data set
        #print("in while loop")
        words = line.split(",")#separates the following values with a comma
        time = "12:03"
        #sets the string variable time to 12:03
        datetime = words[0]#assigns the values in the first column of data to the variable datetime
        #print("datetime:",datetime)
        line = fp.readline()
        
        if time in datetime:#checks to see if the time 12:03 is contained in the original data set,
            #print("time is in datetime")
            par = float(words[4])#assigns the values in the fifth column of data to the variable par and casts them to floats
            #print("par" , par)
            if (par>800):
            #checks to see if the given par value is greater than 800
                #only runs if the above condition is true
                sunnydays = (sunnydays + 1)#increases sunnydays by an increment of one
                sunnysum = (sunnysum + par)#adds the new par value to sunnysum
                
            else:
                cloudydays = cloudydays + 1#increases cloudydays by an increment of one
                cloudysum = cloudysum + par#adds the new para value to cloudysum
                
    avgsunny = (sunnysum/sunnydays)#calculates the average number of sunny days
    avgcloudy = (cloudysum/cloudydays)#calculates the average number of cloudy days
    #print("sunnydays",sunnydays)
    #print("sunnysum",sunnysum)
    #print("cloudydays",cloudydays)
    #print("cloudysum",cloudysum)
    print("Average number of sunny days: %.3f" % (avgsunny))#prints avgsunny with a label and rounds the value to 3 decimal places
    print("Average number of cloudy days: %.3f" % (avgcloudy))#prints avgcloudy with a label and rounds the value to 3 decimal places
    
    fp.close()#closes GoldieMLRCJuly.csv
    
# only execute main if this file was executed
if __name__ == "__main__":
    main()