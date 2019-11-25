#!/usr/bin/env python3

import os
import argparse

from tabulate import tabulate
from termcolor import colored
from selenium import webdriver
from googleapiclient.discovery import build

api_key = ""
cse_id = ""

banner =  """

DDDDDDDDDDDDD             OOOOOOOOO                        kkkkkkkk                                    
D::::::::::::DDD        OO:::::::::OO                      k::::::k                                    
D:::::::::::::::DD    OO:::::::::::::OO                    k::::::k                                    
DDD:::::DDDDD:::::D  O:::::::OOO:::::::O                   k::::::k                                    
  D:::::D    D:::::D O::::::O   O::::::Orrrrr   rrrrrrrrr   k:::::k    kkkkkkkyyyyyyy           yyyyyyy
  D:::::D     D:::::DO:::::O     O:::::Or::::rrr:::::::::r  k:::::k   k:::::k  y:::::y         y:::::y 
  D:::::D     D:::::DO:::::O     O:::::Or:::::::::::::::::r k:::::k  k:::::k    y:::::y       y:::::y  
  D:::::D     D:::::DO:::::O     O:::::Orr::::::rrrrr::::::rk:::::k k:::::k      y:::::y     y:::::y   
  D:::::D     D:::::DO:::::O     O:::::O r:::::r     r:::::rk::::::k:::::k        y:::::y   y:::::y    
  D:::::D     D:::::DO:::::O     O:::::O r:::::r     rrrrrrrk:::::::::::k          y:::::y y:::::y     
  D:::::D     D:::::DO:::::O     O:::::O r:::::r            k:::::::::::k           y:::::y:::::y      
  D:::::D    D:::::D O::::::O   O::::::O r:::::r            k::::::k:::::k           y:::::::::y       
DDD:::::DDDDD:::::D  O:::::::OOO:::::::O r:::::r           k::::::k k:::::k           y:::::::y        
D:::::::::::::::DD    OO:::::::::::::OO  r:::::r           k::::::k  k:::::k           y:::::y         
D::::::::::::DDD        OO:::::::::OO    r:::::r           k::::::k   k:::::k         y:::::y          
DDDDDDDDDDDDD             OOOOOOOOO      rrrrrrr           kkkkkkkk    kkkkkkk       y:::::y           
                                                                                    y:::::y            
                                                                                   y:::::y             
                                                                                  y:::::y              
                                                                                 y:::::y               
                                                                                yyyyyyy          

                                  v1.0 - Mikestro    
                            https://github.com/mikestr0     

"""

print(colored(banner, 'red'))

i = 0
list = []

def screenshot(a, b):
    from selenium import webdriver
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    options.add_argument('--headless')
    options.binary_location = "/usr/bin/google-chrome"
    driver = webdriver.Chrome(options=options)

    driver.get(a)
    driver.save_screenshot(args.d + "/" + b + ".png")
    return b + ".png"
    driver.close()

def HTMLOutput(a):
    f = open(a + "/" + a + '.html', 'a')
    body = "<h2 align='center'>" + "Search Query:" + "<br> <br>" + search_query + "</h2> <br> <br>" + tabulate(list, tablefmt='html', headers=['Page Title', 'Page URL', 'Screenshot']) 
    f.write(body)
    f.close()

parser = argparse.ArgumentParser(description='Example: dorky.py -d google.com -r dorks.txt')
parser.add_argument("-d", type=str, required=True, help="Use this argument to specify your domain")
parser.add_argument("-r", type=str, required=False, default="dorks.txt", help="Use this argument to specify your dorks file")

args = parser.parse_args()
domain = args.d
site = 'site:' + args.d

if not os.path.exists("./" + args.d):
    os.mkdir("./" + args.d)

dorks = args.r

print("Searching for Google Dorks on", args.d, "\n\n")

with open(dorks, 'r') as file:
    for line in file:
        search_query = site + " " + line
        print("Search query - ", search_query, "\n")

        resource = build("customsearch", 'v1', developerKey=api_key).cse()
        result = resource.list(q=search_query, cx=cse_id).execute()

        if not len(result) <= 5:
            list.clear()
            for item in result['items']:
                i += 1
                print(item['title'], item['link'])
                filename = screenshot(item['link'], str(i))
                list.append([item['title'], '<a href=' + '"' + item['link'] + '"' + ' target="_blank"' + '>' + 'Visit Page' + '</a>', '<img src="' + filename + '" alt="" border=3 height=480 width=640></img>'])
        HTMLOutput(domain)
        print("\n\nThis query returned " + str(i) + " results\n\n")


path = os.getcwd()
print("Saving your results to " + path + "/" + domain + "/" + domain + '.html')


