import requests
from datetime import datetime

#url = https://www.youtube.com/
#url = http://python.org/
#url = https://www.twitch.tv/
#url = https://www.skroutz.gr/
#url = https://www.netflix.com/browse

def get_input():
    
    while True :   
        url = input("Enter the URL you wish to check.\nIf you want to exit the program, type: exit. \n")
        
        if len(url) == 0 :
            print("You didn't type anything! Please try again...")
            continue
        elif url == "exit":
            print("Goodbye...")
            exit()
        elif (("https://" not in url) == True) and (("http://" not in url)== True):
            print("The desired URL was not found... Please try again")
            continue
        else:
            try:
                r = requests.get(url) 
                break
            except:
                print("Connection Error... Please try again")
                continue
    return url

def show_headers(url):
    print("")
    with requests.get(url) as response:
        headers = response.headers
        if bool(headers) is False:
            print("There are no response headers\n")
        else:
            print("The  response headers and their values are listed below...")
            for heads, values in headers.items():
                print(heads + " : " + values)

def show_cookies(url):
    with requests.get(url) as response:
        jar = response.cookies
        if bool(jar) is False :
            print("\nThis website does not use cookies! ")
        else:
            print("\nThis website uses cookies and they are listed below with their expiration dates...")
            expires = None
            for cookie in jar:
                expires = cookie.expires
                if cookie.expires is None :
                    print("Cookie Name: " + cookie.name + " and it lasts indefinitely")
                else:
                
                    print("Cookie Name: " + cookie.name + " and it expires at " + str(datetime.fromtimestamp(cookie.expires)))
    print("\n")

def show_web_server_type(url):
    with requests.get(url) as response:
        wbt = response.headers.get('Server')
        if wbt==None:
            print("\n\nThis URL has no server type...?\n")
        else:
            print("\n\nThe web server is using the " + wbt + " software in order to respond to our request!\n")

def main():
    url = get_input()
    show_headers(url)
    show_web_server_type(url)
    show_cookies(url)

main()
