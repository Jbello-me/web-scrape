import requests
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "en-US,en;q=0.9",
    "sec-ch-ua": "\"Google Chrome\";v=\"95\", \"Chromium\";v=\"95\", \";Not A Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "cookie": "PHPSESSID=45289652941680c4d050ab8eed76bbb8",
    "Referer": "https://wateroffice.ec.gc.ca/download/index_e.html?results_type=historical",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  }
req = requests.get('https://wateroffice.ec.gc.ca/download/report_e.html?dt=dd&df=ddf&md=1&ext=csv', headers=headers)
open('output.csv', 'wb').write(req.content)
