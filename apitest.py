import urllib.request
import json
APPID = '1e8b3e63'
APPKEY = 'a03d71215bc5fee7dc12bd2d077655f1—'
url = "https://api.nutritionix.com/v1_1/search/mcdonalds?results=0:20&fields=item_name,brand_name,item_id,nf_calories&appId=" + APPID + '&appKey=' + APPKEY
print (url)
with urllib.request.urlopen(url) as f:
    response_text = f.read().decode('utf-8')
    j = json.loads(response_text)