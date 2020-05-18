Python 2.7.16 (v2.7.16:413a49145e, Mar  2 2019, 14:32:10) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> ##UNCOMMENT THE FOLLOWING to use espeak, not included in colab
import time
from espeak import espeak


"""PROGRAM STARTS HERE"""

espeak.synth("What part of the body is hurting? ")
body_part = input("What part of the body is hurting? ")

parts = body_part
espeak.synth(parts)
time.sleep(1)

espeak.synth("What is one symptom? " )

symptom = input("What is one symptom? " )
espeak.synth(symptom)

search= {'q': symptom + r"+" + body_part}
for i in range (3):
    print("Calculating...")
    espeak.synth("Calculating")
    time.sleep(1)

import requests

#r= requests.get("https://www.google.com/search", params=search)
r= requests.get("https://www.mayoclinic.org/search/search-results?", params=search)
print (r.url)

"""r.text"""
#print (r.text)

def illness_title(x):  # 95% there
  import re
  x=re.split(r"-*\:*\(*",x)
                  ## What if there is a parenthesis, bracket, or ~
  return(x[0].strip())  

def say_illness(illness):    # this is ok
  return "You may have " + illness       # return will quit the function, and the following lines will never be spoken,  you may need to reorder the following lines

from bs4 import BeautifulSoup

soup= BeautifulSoup(r.text, 'html.parser')
#print(soup.prettify())

"""x=str(soup.select("a[href*=webmd]"))
start= x.index("https")
print (start)
stop= x.index("&", start+1)
print (stop)
print (x[start:stop])
r= requests.get(x[start:stop])
#print (r.text)
soup2= BeautifulSoup(r.text, 'html.parser')"""
print("=========== RAW TEXT ============")
##print(soup.get_text())  ##uncomment if you want to see the page text, but I do not recommend
print("=========== END TEXT ============")
soup.title.name
## soup.find_all('Treatment') ##uncomment if you want to see all entries with "Treatment"
## soup.find_all('a')         ##uncomment if you want to see all links on the page

mydivs = soup.findAll("li", {"class": "noimg"})
z = 0
for par in mydivs:                     ## Iterating over all the links
    x = par.find("h3")
    x = x.text              
    illness=illness_title(x)
    z += 1
    if z<4:
      print(say_illness(illness))
      espeak.synth(say_illness(illness))
      if z<3:
          espeak.synth("or")
          time.sleep(.5)
          print("or")
      time.sleep(2)                                
    #print(x)

print("")
print("We are not professional doctors, if you believe that you need medical attention, please seek help ASAP.")
time.sleep(2)
espeak.synth("We are not professional doctors, if you believe that you need medical attention, please seek help ASAP")

#print(soup.prettify())
#print(soup.get_text())
#soup.find_all('Treatment')



