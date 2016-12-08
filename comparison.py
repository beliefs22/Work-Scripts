import csv
from leadingzeroes import addzeroes

def match(pds,redform):
    """Compares all MRNS from PDS and REDFORM data to determine which MRNS
    don't have a paired match. 

    Args:
        pds (list): list of strings representing MRNS from PDS File
        redform (list): list of strings representing MRNS from REDFORM file

    Returns:
        pds_final (list): PDS MRNS marked as found or missing
        redform_final (list): redform MRNS marked as found or missing

    """  

    pds.sort()#Sort so they are both in numerical order
    redform.sort()
    pds_mrn = pds.pop(0)#First PDS MRN to compare
    redform_mrn = redform.pop(0)#First redform MRN to compare
    pds_final = []#If a match is found the MRN will be placed here
    redform_final = []#If a match is found the MRN will be placed here
    #While loop runs until each MRNS has looped through
    #Since both list are in numerical order search through the list by value
    while pds != [] and redform != []:        
        if pds_mrn == redform_mrn:#Found a match
            pds_final.append(pds_mrn)
            redform_final.append(redform_mrn)
            pds_mrn = pds.pop(0)
            redform_mrn = redform.pop(0)
        elif pds_mrn < redform_mrn:#MRN missing in RedFormData
            pds_final.append(pds_mrn)
            redform_final.append("missing")
            pds_mrn = pds.pop(0)
        else:#MRN missing in PDS Data
            redform_final.append(redform_mrn)
            pds_final.append("missing")
            redform_mrn = redform.pop(0)  
    
    
    #Which ever empty list did not cause the loop to break
    #Will have values that need to be addes as missing from the other list
    if pds == [] and redform == []:
        pass
    elif pds == []:
        if pds_mrn == redform_mrn:
            pds_final.append(pds_mrn)
            redform_final.append(redform_mrn)
            redform.pop(0)
        elif pds_mrn < redform_mrn:
            pds_final.append(pds_mrn)
            redform_final.append("missing")
            redform.pop(0)
        else:
            pds_final.append('missing')
            redform_final.append(redform_mrn)
            redform.pop(0)
        
        for i in redform:
            if i > pds_final[len(pds_final) - 1]:
                pds_final.append("missing")
                redform_final.append(i)
            else:
                pds_final.insert(len(pds_final)-1,"missing")
                redform_final.insert(len(redform_final) - 1,i)
    elif redform == []:
        if pds_mrn == redform_mrn:
            pds_final.append(pds_mrn)
            redform_final.append(redform_mrn)
            pds.pop(0)
        elif pds_mrn < redform_mrn:
            pds_final.append(pds_mrn)
            redform_final.append("missing")
            pds.pop(0)
        else:
            pds_final.append('missing')
            redform_final.append(redform_mrn)
            pds.pop(0)
        
        for i in pds:
            if i > redform_final[len(redform_final) - 1]:
                redform_final.append("missing")
                pds_final.append(i)
            else:
                redform_final.insert(len(redform_final) - 1,"missing")
                pds_final.insert(len(pds_final) - 1,i)   

    return pds_final,redform_final

def main():
    addzeroes()#Adds leading zeroes to REDFORM mrns
    pds_file = open("MRNS_FROM_PDS.txt","r")#File with PDS MRNS
    red_file = open("CORRECTED_MRNS_FROM_REDFORMS.txt","r")#File with REDFORM
    pds = []#Container for PDS MRNS
    redform = []#Container for Redform MRNS

    csvout = open('Final_Comparison.csv','wb')
    csvwriter = csv.writer(csvout)
    headers = ['PDS_MRNS','REDFORMS_MRNS']
    csvwriter.writerow(headers)

    for line in pds_file:
        if line.startswith('|') and line.find("MRN") == -1:
            temp = line.rstrip("\n").replace('|',"").replace(" ","")
            pds.append(temp)
    for line in red_file:
        temp = line.rstrip("\n")
        redform.append(temp)

    c,d = match(pds,redform)

    for i in range(len(c)):
        csvwriter.writerow([c[i],d[i]])
    pds_file.close()
    red_file.close()
    csvout.close()

main()

        
