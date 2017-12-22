import requests
import random
from bs4 import BeautifulSoup as bs
import time

#the function prototype
def getGrades(us, pa):
    while(True):
        wait = input("Do you want your grades?(1 or 0)")
        if(wait != "1"):
                break
        #random delay
        delay = 30 + random.randint(0, 100)
        print("wait for " + str(delay) + " seconds so we don't overload the server")
       	for i in range(1,delay):
                if(i % 10 == 0):
                        print(i)
                time.sleep(1)
       
        
        #ubc ssc website
        url = "https://cas.id.ubc.ca/ubc-cas/login?TARGET=https%3A%2F%2Fssc.adm.ubc.ca%2Fsscportal%2Fservlets%2FSRVSSCFramework"
        #create a new request
        r = requests.Session()
        page = r.get(url)
        #if page does not open
        if(page.status_code > 200):
                print("Sorry, could not open")
                continue
        #read the page
        s = bs(page.content,"html.parser")
        #get the stuff we need to login
        box = s.findAll('div',{'class':'box fl-panel'})
        val = box[0].findAll("input",{"type":"hidden"})
        token = val[0]["value"]
        token2 = val[1]['value']
        token3 = val[2]['value']

        #username and password
        user = us
        password = pa
        #this gathers the stuff from above to be used
        payload = { 'username': user, 'password': password , "lt": token, "execution":token2,"_eventId":token3}
        #logs into the site
        p = r.post(url,data=payload)
        #if we cannot log in
        if(p.status_code > 200):
                print("Sorry, could not open")
                continue
        #read
        s = bs(p.content,"html.parser")
        #grades page
        url2 = "https://ssc.adm.ubc.ca/sscportal/servlets/SRVAcademicRecord?context=html?context=html"
        #open and read
        u = r.get(url2)
        if(u.status_code > 200):
                print("Sorry, could not open")
                continue
        s = bs(u.content,"html.parser")

        #get the grades
        for i in range(0,20):
                x = s.findAll("tr",{"id":"row-all-" + str(i)})
                v = x[0].td.text
                y = x[0].findAll("td",{"class":"listRow grade"})
                k = "Not available"
                if(len(y) != 0):
                        k = y[0]["grade"]
                
                print(v+ " " + k) 

        r.close();

#your infp
userID = 
passID = 

#the function
getGrades(userID,passID)

