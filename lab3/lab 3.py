import requests

domain = raw_input('Enter your domain: ')
url = 'https://www.virustotal.com/vtapi/v2/domain/report'
params = {'apikey':'c9a6b6b224757a81b1b460eb3a5236e8f31e47c3ff4a5e859cdd832833a40149','domain':domain}
response = requests.get(url, params=params)
subdomains = response.json()['subdomains']
f = open("subdomain.txt", "w")
for i in subdomains:
    f.write(i.encode('utf-8') + '\n ')
    print i
f.close()