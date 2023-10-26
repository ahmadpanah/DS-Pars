import urllib.request as urllib

print("This is Site Connectiity Checker!")
input_url = input("Please Enter Url: ")

def main(url):
    print("Checking Connectivity...")

    response = urllib.urlopen(url)

    print("Connected to: " , url , "Succecsfully")
    print("The Response code is" , response.getcode())

main(input_url)