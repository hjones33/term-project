import urllib.request
import json
from urllib.parse import urlencode
from config import APPID, APPKEY

def initialsearch(item):
    """Pulls the top 5 results from the API based off the user inpute"""
    item2 = item.replace(" ", "")
    url = "https://api.nutritionix.com/v1_1/search/" + item2 + "?results=0:5&fields=item_name,brand_name,item_description,nf_calories,nf_total_fat,nf_cholesterol,nf_sodium,nf_total_carbohydrate,nf_dietary_fiber,nf_sugars,nf_protein,nf_vitamin_a_dv,nf_vitamin_c_dv,nf_calcium_dv,nf_iron_dv&appId=" + APPID + '&appKey=' + APPKEY
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        j = json.loads(response_text)
        listofresults = j['hits']

        return listofresults       

            
def main():
    """"""
    templist = initialsearch('Caesar Salad')
if __name__ == '__main__':
    main()