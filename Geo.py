import urllib.request, urllib.parse, urllib.error
import json
import ssl
import re
from tkinter import *
from PIL import ImageTk,Image

# This GUI app show the location (countries mainly) of any name the user enters.

# Defining the graphical window main attributes
root = Tk()
root.geometry("250x250")
root.resizable(False,False)
root.title("Country App")
root.iconbitmap('icon.ico')# do not forget to put the icon file in the same directory.


# I do not have api key for using google geocode, so I am using here another server that mimics the same service as google geocode BUT FOR EDUCATIONAL PURPOSES ONLY!
api_key = False
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# A function to find the location and assign it the variable T.
def locate(address):

    # Establishing a connection with error handling
    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    try:
        uh = urllib.request.urlopen(url, context=ctx)
        data = uh.read().decode()
    except:
        T = "====No Internet Connection===="
        label_2.pack_forget()
        label_2['text']=T
        label_2.pack(pady=10)
        return

    # Loading json data and hadle failures
    try:
        js = json.loads(data)
        #print(js)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        T = '==== Failure To Retrieve ===='
    else:
        try:
            # Find the desired info within json data and assign to T
            I = len(js['results'][0]['address_components'])

            A_string = js['results'][0]['address_components'][I-1]['short_name']
            if not re.findall("([A-Z]+)", A_string):
                CC = js['results'][0]['address_components'][I-2]['long_name']
            else:
                CC = js['results'][0]['address_components'][I-1]['long_name']

            T = CC
        except:
            T="{} is not a country or not within a country.".format(address)

    # Replace the data on labels, T for location and C for counter
    global C
    C +=1
    label_3.pack_forget()
    label_3['text']=C
    label_3.pack()
    label_2.pack_forget()
    label_2['text']=T
    label_2.pack(pady=10)

# Defining the labels, the button and the frame
fr = Frame(root, bd=2, relief=SUNKEN)
label_1 = Label(root, text="Enter a name to know the location:").pack(pady=10)
e = Entry(root)
e.pack(pady=15)
label_2 = Label(fr, text="<Empty>")
C = IntVar
C = 0
label_3 = Label(fr, text=C, padx=5)
btn = Button(root, text="search", command=lambda: locate(e.get()), pady=3, padx=3).pack(pady=10)
def eVal(event):
    locate(e.get())
e.bind('<Return>',eVal)
fr.pack(pady=3)
label_4 = Label(fr, text="Number of searches done",padx =5).pack()
label_3.pack()
label_2.pack(pady=10)

root.mainloop()
