'''

Marilu D
CS 1114

This program gets averages of the rain fall per city per month.
'''


# Part A
def clean_data(complete_weather_filename, cleaned_weather_filename):    
    # Complete this function to clean the CSV.
    # It should create a new file as specified in the assignment specs.
    file = open(complete_weather_filename,'r')#opens and reads the file
    fileRead = file.readline()#reads a line
    #makes new file
    newFile = open(cleaned_weather_filename,'w')
    newFile.write("City,Date,High,Low,Precipitation\n")#writes in file
    #while loop for extra line to remove
    while file.readline() != None:
        lineInfo = file.readline().rstrip().split(",")#splits commas
        if lineInfo == ['']:
            break
        if lineInfo[8] == "T":#for ever index 8 that is T replace with 0
            lineInfo[8] = "0"
        newFile.write(lineInfo[0]+","+lineInfo[1]+","+lineInfo[2]+","+lineInfo[3]+","+lineInfo[8]+"\n")

    file.close()
    newFile.close()   
#closes

# Part B
def f_to_c(f_temperature):
    '''calculates from f to c'''
    celcius = 5/9 *(int(f_temperature) - 32)
    return celcius #return celcius

def in_to_cm(inches):
    '''calculates from in to cm'''
    centim = float(inches) * 2.54
    return centim #return centimeter

def convert_data_to_metric(imperial_weather_filename, metric_weather_filename):
   file = open(imperial_weather_filename,'r')#opens file
   fileRead = file.readline()#reads
    #new file
   newFile = open(metric_weather_filename,'w')
   newFile.write("City,Date,High,Low,Precipitation\n")#write with new line
    #while loop for extra line to remove
   while True:
        lineInfo = file.readline().rstrip().split(",")#splits comma in line
        if lineInfo == ['']:
            break
        lineInfo[2] = f_to_c(lineInfo[2])#puts new info into new file in new space
        lineInfo[3] = f_to_c(lineInfo[3])
        lineInfo[4] = in_to_cm(lineInfo[4])
        newFile.write(lineInfo[0]+","+lineInfo[1]+","+str(lineInfo[2])+","+str(lineInfo[3])+","+str(lineInfo[4])+"\n")
        
 #  file.close()
 #  newFile.close()

# Part C
def print_average_temps_per_month(city, weather_filename, unit_type):
    # prints average highs and lows in each month for the given city
    f_to_c = False
    if "imperial" in weather_filename:
        if unit_type == "metric":
            f_to_c = True
            
    totalHighTemps = [0] * 12       # [0, 0, 0, 0, 0, 0, 0 ...]index*12
    totalLowTemps = [0] * 12#same as above
    counterForEachMonth = [0] * 12#same but for counter
    
    file = open(weather_filename,'r')#reads file
    fileRead = file.readline()
    while True:
        lineInfo = file.readline().rstrip().split(",")#splits
        if lineInfo == ['']:
            break
        if lineInfo[0] == city:     # City we are looking for
            date = lineInfo[1]      # Get the date in 10/1/2010 form
            month = date.split("/")[0] # Split to list [10, 1, 2010], get first index
            totalHighTemps[int(month) - 1] += float(lineInfo[2])#indexing with month
            totalLowTemps[int(month) - 1] += float(lineInfo[3])
            counterForEachMonth[int(month) - 1] += 1
            
    file.close()#close files
    for i in range(12): # Get Average for 12 months
        totalHighTemps[i] /= counterForEachMonth[i]
        totalLowTemps[i] /= counterForEachMonth[i] #counts the low tmeps index for each month
    print("Average Temperature of: ",city)
    print("January:", totalHighTemps[0], "F High", totalLowTemps[0], "F low")#lists all the months and their highs/lows
    print("February:", totalHighTemps[1], "F High", totalLowTemps[1], "F low")
    print("March:", totalHighTemps[2], "F High", totalLowTemps[2], "F low")
    print("April:", totalHighTemps[3], "F High", totalLowTemps[3], "F low")
    print("May:", totalHighTemps[4], "F High", totalLowTemps[4], "F low")
    print("June:", totalHighTemps[5], "F High", totalLowTemps[5], "F low")
    print("July:", totalHighTemps[6], "F High", totalLowTemps[6], "F low")
    print("August", totalHighTemps[7], "F High", totalLowTemps[7], "F low")
    print("September:", totalHighTemps[8], "F High", totalLowTemps[8], "F low")
    print("October:", totalHighTemps[9], "F High", totalLowTemps[9], "F low")
    print("November:", totalHighTemps[10], "F High", totalLowTemps[10], "F low")
    print("December:", totalHighTemps[11], "F High", totalLowTemps[11], "F low")

# Part D
# What is the city with the higher rain fall?
def higher_rainfall_avg(cityOne,cityTwo,weather_filename):#answers question
    '''Gets the city with the highest rain fall through avereaging.'''
    openFile = open(weather_filename,"r")#opens file
#counters here
    cityOneTotal = 0
    cityTwoTotal = 0
    counter1 = 0
    counter2 = 0
    for i in openFile:#loop to clean
        split = i.rstrip().split(",")#splits commas
        citySplit = split[0]
        if citySplit == cityOne:
            cityOneTotal = cityOneTotal + float(split[4]) #cleans the file

            counter1 += 1
        
        if citySplit == cityTwo:
            cityTwoTotal += float(split[4])
            counter2 += 1

    avgCity1 = cityOneTotal / counter1#this is the avg for city1
    avgCity2 = cityTwoTotal / counter2#avg for city 2

    if avgCity1 > avgCity2:#prints results
        print(cityOne,"has the higher rain fall average of the two cities.")
    elif avgCity1 == avgCity2:
        print("Both cities have the same rain fall average")
    else:
        print(cityTwo,"has the higher rain fall average of the two cities.")
    
    


def main():
    '''compiles all the functions to print out/run'''
    print ("Running Part A")
    clean_data("weather.csv", "weather in imperial.csv")#runsA
    
    print ("Running Part B")
    convert_data_to_metric("weather in imperial.csv", "weather in metric.csv")#runs B
    
    print ("Running Part C")
    print_average_temps_per_month("San Francisco", "weather in imperial.csv", "imperial")#runs C
    print_average_temps_per_month("New York", "weather in metric.csv", "metric")
    print_average_temps_per_month("San Jose", "weather in imperial.csv", "imperial")

    print ("Running Part D")
#runs D
    higher_rainfall_avg("San Jose","San Francisco","weather in imperial.csv" )
    
    
main()
