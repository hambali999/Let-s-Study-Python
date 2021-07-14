


def main():
    
    fin = open("customers.dat", "r") #parameters: filename, mode("a","r","w")
    print("Name\tWeight\tHeight\tBMI")
    for eachline in fin:
        name,wt,ht = eachline.split(",")
        # print(name)
        # print(wt)
        # print(ht)
        wt = float(wt)
        ht = float(ht)
        bmi = wt/(ht**2)
        print(f"{name}\t{wt}\t{ht}\t{bmi:.2f}")
    #end for loop
    fin.close() #must always close file after use

main()