import os

def get_ip_address(url):
    command = "ping " + url
    process = os.popen(command)
    results = str(process.read())
    marker = results.find('statistics for') + 15
    return results[marker:].splitlines()[0]

ip = (get_ip_address('adress'))[:-1]
print(ip)