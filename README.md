# UBC Grade Checker
Ubc course checker works by going to the ubc ssc website and logging using your info. It then looks through the html code to find your grades and prints them to you. You can automate the process so that it checks for you at a given time interval without the need for you to tell it to continue.

# Usage 
You need to have installed the BeautifulSoup4 and requests libraries which you install using the commands 'pip install requests' and pip 'install bs4' on the command line.

works as of Python 3.6.3 Dec 2017.

You only need to enter your username and password in string format and the code will do the rest. 

Use y or n to continue and exit.

There is a delay so that the server does not get overwhelmed.
