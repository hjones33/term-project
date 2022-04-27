import urllib.request
import json
from urllib.parse import urlencode
from config import APPID, APPKEY

reccomended_dvs = {'Calories': 2000, 'Fat': 78, 'Cholesterol': 300, 'Sodium': 2300, 'Carbohydrates': 275, 'Dietary Fiber': 28, 'Sugar': 50, 'Protein': 50, 'Vitamin A': 100, 'Vitamin C': 100, 'Calcium': 100, 'Iron': 100}
initial = []
def initialsearch(item):
    """Display Initial Search Results to User, Ideally allow them to select"""
    item2 = item.replace(" ", "")
    url = "https://api.nutritionix.com/v1_1/search/" + item2 + "?results=0:5&fields=item_name,brand_name,item_description,nf_calories,nf_total_fat,nf_cholesterol,nf_sodium,nf_total_carbohydrate,nf_dietary_fiber,nf_sugars,nf_protein,nf_vitamin_a_dv,nf_vitamin_c_dv,nf_calcium_dv,nf_iron_dv&appId=" + APPID + '&appKey=' + APPKEY
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        j = json.loads(response_text)
        listofresults = j['hits']

        return listofresults       

            


def selectsize():
    """Select serving size"""

def storenutrition():
    """Stores the nutrition facts of the selected item"""

def main():
    """Goes through and runs everything you need to get the closest station and whether or not it is wheelchair acessible or not"""
    templist = initialsearch('Tacos')
    initial.append(templist)
    print(templist)
if __name__ == '__main__':
    main()