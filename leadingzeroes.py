def addzero(mrns):
    """Adds leading Zeros to MRNS less than 8 digits"""
    new_mrn = []
    for number in mrns:
        length = 8 - len(number) #Determines len of given MRN
        
        if length != 0: #If lengh < 8 adds zeros until length equals 8
            temp = ("0"*length) + number
            new_mrn.append(temp)
        else:
            new_mrn.append(number)

    return new_mrn


def main():
    myfile = open("MRNS_FROM_REDFORMS.txt","r")
    myfile2 = open("CORRECTED_MRNS_FROM_REDFORMS.txt","w")
    mrns = []

    for line in myfile:
        if line.startswith('|') and line.find("MRN") == -1:
            temp = line.rstrip("\n").replace('|',"").replace(" ","")
            mrns.append(temp)

    new_mrn = addzero(mrns)
    

    for number in new_mrn:
        myfile2.write(number + "\n")

    myfile.close()
    myfile2.close()

def addzeroes():
    """Adds Zeros To Files Exported from Paired Access Database"""
    myfile = open("MRNS_FROM_REDFORMS.txt","r") #Input File Redforms MRNS
    myfile2 = open("CORRECTED_MRNS_FROM_REDFORMS.txt","w")#Output File
    mrns = []
    for line in myfile:
        #only look at lines that contain numbers
        if line.startswith('|') and line.find("MRN") == -1:
            temp = line.rstrip("\n").replace('|',"").replace(" ","")
            mrns.append(temp)
    new_mrn = addzero(mrns)    

    for number in new_mrn:#Write MRNS with leading zeroes to output File
        myfile2.write(number + "\n")
    myfile.close()
    myfile2.close()

if __name__ =='__main__':
    main()
        
        
