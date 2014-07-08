import csv
import sys
import urllib, urllib2                                                          
import json


def outputCsv(data):
    with open('output.csv', 'w') as fp:
        a = csv.writer(fp, delimiter=',')
        a.writerows(data)

f = open(sys.argv[1], 'rt')
outputRows = []
try:
    reader = csv.reader(f)
    rows = list(reader)
    print len(rows)
    count = 0
    for row in rows:
        latitude = row[2]
        longitude = row[3]
        location = row[6]
        identification = row[8]
        searchStr = 'null'
        if(location != 'null' and identification != 'null'):
            searchStr = location + ', ' + identification
        elif(location != 'null'):
            searchStr = location
        else:
            searchStr = identification
        if((latitude == 'null' or longitude == 'null') and searchStr != 'null'):
            count=count+1
            print 'params=[',params,']'
            params = {'address': searchStr + ', '+sys.argv[2], 'sensor': 'false'} 
            url = 'http://maps.googleapis.com/maps/api/geocode/json?' + urllib.urlencode(params)

            rawreply = urllib2.urlopen(url).read()                                          
            reply = json.loads(rawreply)                                                    
            
            lat = reply['results'][0]['geometry']['location']['lat']                        
            lng = reply['results'][0]['geometry']['location']['lng']                        
            
            print '[%f; %f]' % (lat, lng)
            row[2] = lat
            row[3] = lng
            outputRows.append(row)
        else:
            outputRows.append(row)
    print 'without latLng=['+str(count)+']'
finally:
    print 'outputing to csv...'
    outputCsv(outputRows)
    print 'done...'
    f.close()
