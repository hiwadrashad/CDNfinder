from django.shortcuts import render, render_to_response
import os
import requests, json, sys, socket
from django import forms

# Create your views here.
def get_ip_address(url):
    command = "ping " + url
    process = os.popen(command)
    results = str(process.read())
    marker = results.find('statistics for') + 15
    return results[marker:].splitlines()[0]


ip = (get_ip_address('google.com'))[:-1]

if not ip:
    url = "https://ipinfo.io/"
else:
    try:
        socket.inet_aton(ip)
        domain = False
    except socket.error:
        domain = True
    if domain:
        try:
            ip = socket.gethostbyname(ip)
        except:
            print("invalid domain name...")
            sys.exit()
    url = "https://ipinfo.io/" + str(ip)

try:
    r = requests.get(url)
except:
    print("error while querying info...")
    sys.exit()

data = json.loads(r.text)

text = """

     {5}

"""

text = text.format(data.get("ip", "[NO DATA]"), data.get("city", "[NO DATA]"), \
                   data.get("region", "[NO DATA]"), \
                   data.get("country", "[NO DATA]"), \
                   data.get("loc", "[NO DATA]"), \
                   data.get("org", "[NO DATA]"), \
                   data.get("postal", "[NO DATA]"))

print(text)

def index(request):
    if not request.GET:
        return render_to_response('index.html')

    else:
        print(request.GET['term'])
        term = (request.GET['term'])
        ip = (get_ip_address(term))[:-1]
        if not ip:
            url = "https://ipinfo.io/"
        else:
            try:
                socket.inet_aton(ip)
                domain = False
            except socket.error:
                domain = True
            if domain:
                try:
                    ip = socket.gethostbyname(ip)
                except:
                    print("invalid domain name...")
                    sys.exit()
            url = "https://ipinfo.io/" + str(ip)

        try:
            r = requests.get(url)
        except:
            print("error while querying info...")
            sys.exit()

        data = json.loads(r.text)

        text = """

             {5}

        """

        text = text.format(data.get("ip", "[NO DATA]"), data.get("city", "[NO DATA]"), \
                           data.get("region", "[NO DATA]"), \
                           data.get("country", "[NO DATA]"), \
                           data.get("loc", "[NO DATA]"), \
                           data.get("org", "[NO DATA]"), \
                           data.get("postal", "[NO DATA]"))

        return render(request,'index2.html',{'website':text})

