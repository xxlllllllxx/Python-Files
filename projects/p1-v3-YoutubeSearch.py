import requests

url = "https://api.apilayer.com/youtube/auto-complete?q={q}"

payload = {}
headers = {
    "apikey": "Zl97CzsvCn9yQ051MGOruScgks2GBo8q"
}

response = requests.request("GET", url, headers=headers, data=payload)

status_code = response.status_code
result = response.text
