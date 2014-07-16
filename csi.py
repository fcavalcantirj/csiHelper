import csv
import sys
import urllib, urllib2                                                          
import json


def outputCsv(fileName, data):
    with open(fileName, 'w') as fp:
        a = csv.writer(fp, delimiter=',')
        a.writerows(data)

f = open(sys.argv[1], 'rt')
outputRows = []
try:
    reader = csv.reader(f)
    rows = list(reader)
    print len(rows)
    count = 0
    rows[0].insert(47, "latIdentification")
    rows[0].insert(48, "longIdentification")
    outputRows.append(rows[0])
    for x in range(1, len(rows)):
        row = rows[x]
        latitude = row[2]
        longitude = row[3]
        location = row[6]
        identification = row[8]
        age = row[9]
        randomQuestion = row[25]
        searchStr = 'null'
        if (age != 'null' or randomQuestion != 'null' or ((latitude!= 'null' and longitude!='null') or (location != 'null') )):
            # if(location != 'null' and identification != 'null'):
            #     searchStr = location + ', ' + identification
            # elif(location != 'null'):
            #     searchStr = location
            # else:
            #     searchStr = identification
            if(latitude == 'null' or longitude == 'null'):
                count=count+1
                searchStr = location
                print 'searching for str=[',searchStr,']'
                params = {'address': searchStr + ', '+sys.argv[2], 'sensor': 'false'} 
                url = 'http://maps.googleapis.com/maps/api/geocode/json?' + urllib.urlencode(params)

                rawreply = urllib2.urlopen(url).read()                                          
                reply = json.loads(rawreply)                                                    
            
                lat = reply['results'][0]['geometry']['location']['lat']                        
                lng = reply['results'][0]['geometry']['location']['lng']                        
            
                print '[%f; %f]' % (lat, lng)
                row[2] = lat
                row[3] = lng
            if(identification!='null' ):
                searchStr = identification
                print 'searching for str=[',searchStr,']'
                params = {'address': searchStr + ', '+sys.argv[2], 'sensor': 'false'} 
                url = 'http://maps.googleapis.com/maps/api/geocode/json?' + urllib.urlencode(params)

                rawreply = urllib2.urlopen(url).read()                                          
                reply = json.loads(rawreply)                                                    
            
                lat = reply['results'][0]['geometry']['location']['lat']                        
                lng = reply['results'][0]['geometry']['location']['lng']                        
            
                print '[%f; %f]' % (lat, lng)
                row.insert(47, lat)
                row.insert(48, lng)
            else:
                row.insert(47, 'null')
                row.insert(48, 'null')
            outputRows.append(row)
            
        #print latitude
    print 'without latLng=['+str(count)+']'
finally:
    print 'outputing to csv...'
    outputCsv("out_"+sys.argv[1], outputRows)
    print 'done...'
    f.close()
