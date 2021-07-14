
def main():
    
    fin = open("customers.dat", "r") #parameters: filename, mode("a","r","w")
    fout = open('bmi.dat', 'w')

    print("Name\tWeight\tHeight\tBMI")
    fout.write("Name\tWeight\tHeight\tBMI\n")
    for eachline in fin:
        name,wt,ht = eachline.split(",")
        # print(name)
        # print(wt)
        # print(ht)
        wt = float(wt)
        ht = float(ht)
        bmi = wt/(ht**2)
        fout.write(f"{name:7s}\t{wt:5.1f}\t{ht:5.1f}\t{bmi:.2f}\n")
        print(f"{name}\t{wt}\t{ht}\t{bmi:.2f}")
    #end for loop
    fin.close() #must always close file after use
    fout.close()

main()