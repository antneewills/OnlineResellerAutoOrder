# Online Reseller Auto Order
 
Python 3 module that provides an educational example of web automation using Selenium
and ChromeDriver.

## Introduction

Covid 19 has wrecked havoc on our economy and has caused an increase demand for
cleaning supplies, toiletries, and other non-parishable house-hold goods. In an
effort to maximize social distancing, people have increased online shopping and by
doing so have caused many items to often be unavailable for online purchase. This
python module is an educational example of how to develop source code for web automation
that pontentially could be leveraged to order unavailable items from an online reseller.
This module is provided for demonstration purposes only and may violate end user
agreements. DO NOT EXECUTE THIS MODULE or similar modules without first reviewing end
user agreements with online resellers. Failure to comply with online reseller user
agreements could result in legal actions.

### Prerequisites for web automation

1. Python (obviously). [Python 3.6.7 64-bit](https://www.python.org/ftp/python/3.6.7/python-3.6.7-amd64.exe).
1. [Google Chrome](https://www.google.com/chrome/).
1. [ChromeDriver](https://chromedriver.chromium.org/downloads) - download to python installation directory; otherwise be 
   sure to set up PATH environmental variables for when ChromeDriver is located.
   Be sure that the version of ChromeDriver downloaded is correct for the version
   of Chrome installed on the PC. Install the latest versions of both if unsure.
1. Selenium library - install via cmd line: `pip install selenium`
1. Requests library - install via cmd line: `pip install requests`

### Web automation in practice

Python modules can be run from the cmd line: `python <module name>`

The following files are provided to demonstrate how custom user parameters can be
stored in secondary modules and imported as needed to the main module.
 - credentials.py
   Used to specify *username* and *password* for the online reseller account.

 - productUrls.py
   Used to specify the URLs for the products to be ordered. URLs can be obtained
   by navigating to the pages manually then copying from the browser and pasting
   into the URLs array. The existing list in the file was provided as an example.
   Repeat a URL as needed to purchase more than one.
   
This source code shown in this module demonstrates:
1. Launching an automated chrome browser
1. Entering user credentials for a login
1. Waiting for a user to manually perform some action,
   e.g. perform a "I am not a robot" reCAPTCHA check
1. Navigate to URLs and scrap web data, e.g. availability information
1. Make decisions based on scrapped web data
1. Loop as necessary until all desired operations are completed, e.g. all
   products have been purchased
1. Close automated chrome browser and quit when done
