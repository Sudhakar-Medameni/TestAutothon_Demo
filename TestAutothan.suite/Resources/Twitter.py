import requests
import json
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

url = "https://api.twitter.com/2/tweets"

payload = json.dumps({
"text": "#STEPINSUMMIT20223 @stepin_foum @verifty_software"+current_time
})
headers = {
'Content-Type': 'application/json',
'Authorization': 'OAuth oauth_consumer_key="Oe44SEdKCnqQ8YwLIiuhy2NJ9",oauth_token="1694194770426380289-EBdmxoaQe2ayI9eqHFIs7ckwGRCLE8",oauth_signature_method="HMAC-SHA1",oauth_timestamp="1692774014",oauth_nonce="c19CfAnd5Kh",oauth_version="1.0",oauth_signature="ZvMrJ0lQMb7L%2FzO49dCc5qmryHA%3D"',
'Cookie': 'ct0=9e244690da55a8bb33bb7a007fee6f68; guest_id=v1%3A169276773359327968; guest_id_ads=v1%3A169276773359327968; guest_id_marketing=v1%3A169276773359327968; personalization_id="v1_T9zxx9QSUCfYRYLERP1qEw=="'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)