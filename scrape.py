import requests
headers = {
    "cookie": "PHPSESSID=45289652941680c4d050ab8eed76bbb8"
  }
req = requests.get('https://wateroffice.ec.gc.ca/download/report_e.html?dt=dd&df=ddf&md=1&ext=csv', headers=headers)
open('output.csv', 'wb').write(req.content)
