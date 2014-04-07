import requests
from BeautifulSoup import BeautifulSoup as BS

resp = requests.get('http://example.com')
form = BS(resp.text).find('form')

# send POST request to "Accept" URL
data = {input.get('name'):input.get('value') for input in form.findAll('input') if input.get('name') is not None}
action = form.get('action')
resp = requests.post("http:"+action, data=data)

print("Success." if resp.status_code==200 else "Failure: POST to {} returned {}".format(action, str(resp)))

