import csv
import requests
import ceirstokens

def getReport(reportid, TOKEN, outfile):
    #Hopkins REDCap URL
    URL = 'https://mrprcbcw.hosts.jhmi.edu/redcap/api/'
    #API to pull reports
    payload = {'token': TOKEN, 'format': 'csv', 'content': 'report',
               'report_id' : reportid, 'rawOrLabelHeaders' : 'label',
               'rawOrLabel' : 'label', 'exportCheckboxLabel': True}

    response = requests.post(URL, data=payload, verify=True)
    print response.status_code
    #Sucessful call
    if response.status_code == 200:
        with open(outfile,'rb') as myfile:
            output = open(outfile, 'wb')
            outputwriter = csv.writer(output)
            #CSV of the report
            data = csv.reader(response.text.encode('ascii','ignore').split("\n"))
            count = -1
            for row in data:
                if row == []:
                    print 'Done, pulled %d records' % count
                    break
                outputwriter.writerow(row)
                count += 1
    else:
        print "Failed"
        raise RuntimeError

def main():


if __name__ == "__main__":
    main()
    
