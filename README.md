# UBC Grade Checker
Ubc course checker works by going to the ubc ssc website and logging using your info. It then looks through the html code to find your grades and prints them to you. You can automate the process so that it checks for you at a given time interval without the need for you to tell it to continue.

# Usage 
works as of Python 3.6.3 Dec 2017.

Instructions:

Install Python, if you haven't already (Mac OS already comes with Python pre-installed). You need to have installed the BeautifulSoup4 and requests libraries which you can install using the commands 'pip install requests' and 'pip install bs4' on the command line.

On Github, click on the green button that says "Clone or download", then "Download ZIP".

Extract the zipped/compressed folder and open the resulting folder.

Edit the ubc-gradecheck.py to add your username and password
Run ubc-gradecheck.py

# Remarks
You only need to enter your username and password in string format and the code will do the rest. 
Use y or n to continue or exit.
There is a delay so that the server does not get overwhelmed.
