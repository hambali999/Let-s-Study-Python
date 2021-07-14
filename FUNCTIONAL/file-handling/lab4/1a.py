def main():

    totalRainfall = 0
    noOfRainfall = 0
    averageRainfall = 0
    noRains = 0
    highestRainfall = 0
    values =[]

    # def highestRainfall(x):
    #     highestRainfaill = 0
    #     if float(x) > highestRainfaill:
    #         highestRainfaill = x
    #     print(f"highest rainfall: {x}")
    #     return x

    f = open('rainfall.dat', 'r')
    for line in f:
        stripped_line = line.strip() #Then, call str.strip() to strip the end-line break from each line.
        # print(stripped_line)
        values.append(float(stripped_line))
        # highestRainfall(stripped_line)
        noOfRainfall += 1
        totalRainfall += float(stripped_line) #convert to float since in rainfall.data, there is a float. int('str') would not work
        if stripped_line == '0':
            noRains += 1

    # print(values)
    # print(max(values))
    highestRainfall = max(values)
        
    averageRainfall = totalRainfall/noOfRainfall
    print(f"Rainfall Summary")    
    print(f"Average rainfall {averageRainfall:.2f}mm")
    print(f"No of days with no rain {noRains} days")
    print(f"Highest rainfall recorded {highestRainfall}mm")

# main()


#BETTER & CLEANER
#ALTERNATIVE METHOD BY LECTURER

import random
def writeFile():
    
    fout = open("rainfall.dat", "r") #parameters: filename, mode("a","r","w")
    values = []
    for eachline in fout:
        num = float(eachline) #turns eachline of 'string' to 'float' as it contains decimal points
        values.append(num)
        #end loop
    largest=max(values)
    average=(sum(values)/len(values))
    noRf = values.count(0)
            
    print("Rainfall Summary")
    print(f"Average rainfall {average:.2f}mm")
    print(f"No of days with no rain {noRf} days")
    print(f"Highest rainfall recorded {largest:.1f}mm")
        
    #end for loop
    fout.close()

writeFile()