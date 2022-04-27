from flask import Flask
from flask import request, render_template
from nutritionapi import *

app = Flask(__name__)

listofresults = []
userchoice = []
dailynut = {'Calories': 0, 'Fat': 0, 'Cholesterol': 0, 'Sodium': 0, 'Carbohydrates': 0, 'Dietary Fiber': 0, 'Sugar': 0, 'Protein': 0, 'Vitamin A': 0, 'Vitamin C': 0, 'Calcium': 0, 'Iron': 0}
itemnut = []
@app.route('/', methods = ['POST', 'GET'])
def hello():
    return render_template("index.html")

@app.route('/data', methods = ['POST', 'GET'])
def data():
    formdata = request.form
    userinput = formdata['Food']
    templist = initialsearch(userinput)
    listofresults.append(templist)
    # result1 = 'First Result: ' + listofresults[0]['fields']['item_name'] 
    # result1desc = 'Item Description: ' + str(listofresults[0]['fields']['item_description'])  
    # result1brand = 'Brand: ' + listofresults[0]['fields']['brand_name'] 
    # result1cals = 'Calories: ' + str(listofresults[0]['fields']['nf_calories']) 
    # result1serving = 'Serving Size: ' + str(listofresults[0]['fields']['nf_serving_size_qty']) + ' ' + listofresults[0]['fields']['nf_serving_size_unit']
    # result2 = 'Second Result: ' + listofresults[1]['fields']['item_name'] 
    # result2desc = 'Item Description: ' + str(listofresults[1]['fields']['item_description'])  
    # result2brand = 'Brand: ' + listofresults[1]['fields']['brand_name'] 
    # result2cals = 'Calories: ' + str(listofresults[1]['fields']['nf_calories']) 
    # result2serving = 'Serving Size: ' + str(listofresults[1]['fields']['nf_serving_size_qty']) + ' ' + listofresults[1]['fields']['nf_serving_size_unit']
    # result3 = 'Third Result: ' + listofresults[2]['fields']['item_name'] 
    # result3desc = 'Item Description: ' + str(listofresults[2]['fields']['item_description'])  
    # result3brand = 'Brand: ' + listofresults[2]['fields']['brand_name'] 
    # result3cals = 'Calories: ' + str(listofresults[2]['fields']['nf_calories']) 
    # result3serving = 'Serving Size: ' + str(listofresults[2]['fields']['nf_serving_size_qty']) + ' ' + listofresults[2]['fields']['nf_serving_size_unit']
    # result4 = 'Fourth Result: ' + listofresults[3]['fields']['item_name'] 
    # result4desc = 'Item Description: ' + str(listofresults[3]['fields']['item_description'])  
    # result4brand = 'Brand: ' + listofresults[3]['fields']['brand_name'] 
    # result4cals = 'Calories: ' + str(listofresults[3]['fields']['nf_calories']) 
    # result4serving = 'Serving Size: ' + str(listofresults[3]['fields']['nf_serving_size_qty']) + ' ' + listofresults[3]['fields']['nf_serving_size_unit']
    # result5 = 'Fifth Result: ' + listofresults[4]['fields']['item_name'] 
    # result5desc = 'Item Description: ' + str(listofresults[4]['fields']['item_description'])  
    # result5brand = 'Brand: ' + listofresults[4]['fields']['brand_name'] 
    # result5cals = 'Calories: ' + str(listofresults[4]['fields']['nf_calories']) 
    # result5serving = 'Serving Size: ' + str(listofresults[4]['fields']['nf_serving_size_qty']) + ' ' + listofresults[4]['fields']['nf_serving_size_unit']
    # return render_template("results.html",  result1 = result1, result1desc = result1desc, result1brand = result1brand, result1cals = result1cals, result1serving = result1serving, result2 = result2, result2desc = result2desc, result2brand = result2brand, result2cals = result2cals, result2serving = result2serving, result3 = result3, result3desc = result3desc, result3brand = result3brand, result3cals = result3cals, result3serving = result3serving, result4 = result4, result4desc = result4desc, result4brand = result4brand, result4cals = result4cals, result4serving = result4serving, result5 = result5, result5desc = result5desc, result5brand = result5brand, result5cals = result5cals, result5serving = result5serving)
    
    result1 = 'First Result: ' + listofresults[0][0]['fields']['item_name'] 
    result1desc = 'Item Description: ' + str(listofresults[0][0]['fields']['item_description'])  
    result1brand = 'Brand: ' + listofresults[0][0]['fields']['brand_name'] 
    result1cals = 'Calories: ' + str(listofresults[0][0]['fields']['nf_calories']) 
    result1serving = 'Serving Size: ' + str(listofresults[0][0]['fields']['nf_serving_size_qty']) + ' ' + listofresults[0][0]['fields']['nf_serving_size_unit']
    result2 = 'Second Result: ' + listofresults[0][1]['fields']['item_name'] 
    result2desc = 'Item Description: ' + str(listofresults[0][1]['fields']['item_description'])  
    result2brand = 'Brand: ' + listofresults[0][1]['fields']['brand_name'] 
    result2cals = 'Calories: ' + str(listofresults[0][1]['fields']['nf_calories']) 
    result2serving = 'Serving Size: ' + str(listofresults[0][1]['fields']['nf_serving_size_qty']) + ' ' + listofresults[0][1]['fields']['nf_serving_size_unit']
    result3 = 'Third Result: ' + listofresults[0][2]['fields']['item_name'] 
    result3desc = 'Item Description: ' + str(listofresults[0][2]['fields']['item_description'])  
    result3brand = 'Brand: ' + listofresults[0][2]['fields']['brand_name'] 
    result3cals = 'Calories: ' + str(listofresults[0][2]['fields']['nf_calories']) 
    result3serving = 'Serving Size: ' + str(listofresults[0][2]['fields']['nf_serving_size_qty']) + ' ' + listofresults[0][2]['fields']['nf_serving_size_unit']
    result4 = 'Fourth Result: ' + listofresults[0][3]['fields']['item_name'] 
    result4desc = 'Item Description: ' + str(listofresults[0][3]['fields']['item_description'])  
    result4brand = 'Brand: ' + listofresults[0][3]['fields']['brand_name'] 
    result4cals = 'Calories: ' + str(listofresults[0][3]['fields']['nf_calories']) 
    result4serving = 'Serving Size: ' + str(listofresults[0][3]['fields']['nf_serving_size_qty']) + ' ' + listofresults[0][3]['fields']['nf_serving_size_unit']
    result5 = 'Fifth Result: ' + listofresults[0][4]['fields']['item_name'] 
    result5desc = 'Item Description: ' + str(listofresults[0][4]['fields']['item_description'])  
    result5brand = 'Brand: ' + listofresults[0][4]['fields']['brand_name'] 
    result5cals = 'Calories: ' + str(listofresults[0][4]['fields']['nf_calories']) 
    result5serving = 'Serving Size: ' + str(listofresults[0][4]['fields']['nf_serving_size_qty']) + ' ' + listofresults[0][4]['fields']['nf_serving_size_unit']
    return render_template("results.html",  result1 = result1, result1desc = result1desc, result1brand = result1brand, result1cals = result1cals, result1serving = result1serving, result2 = result2, result2desc = result2desc, result2brand = result2brand, result2cals = result2cals, result2serving = result2serving, result3 = result3, result3desc = result3desc, result3brand = result3brand, result3cals = result3cals, result3serving = result3serving, result4 = result4, result4desc = result4desc, result4brand = result4brand, result4cals = result4cals, result4serving = result4serving, result5 = result5, result5desc = result5desc, result5brand = result5brand, result5cals = result5cals, result5serving = result5serving)


@app.route('/serving', methods = ['POST', 'GET'])
def serving():
    formdata2 = request.form
    userfood = formdata2['Which_food']
    if userfood == 'First Result':
        userchoice.append(0)
        foodselection = 'You selected: ' + listofresults[0][0]['fields']['item_name']
        resultdesc = 'Item Description: ' + str(listofresults[0][0]['fields']['item_description'])  
        resultbrand = 'Brand: ' + listofresults[0][0]['fields']['brand_name'] 
        resultcals = 'Calories: ' + str(listofresults[0][0]['fields']['nf_calories']) 
        resultserving = 'Serving Size: ' + str(listofresults[0][0]['fields']['nf_serving_size_qty']) + ' ' + listofresults[0][0]['fields']['nf_serving_size_unit']
    elif userfood == 'Second Result':
        userchoice.append(1)
        foodselection = 'You selected: ' + listofresults[0][1]['fields']['item_name']
        resultdesc = 'Item Description: ' + str(listofresults[0][1]['fields']['item_description'])  
        resultbrand = 'Brand: ' + listofresults[0][1]['fields']['brand_name'] 
        resultcals = 'Calories: ' + str(listofresults[0][1]['fields']['nf_calories']) 
        resultserving = 'Serving Size: ' + str(listofresults[0][1]['fields']['nf_serving_size_qty']) + ' ' + listofresults[0][1]['fields']['nf_serving_size_unit']         
    elif userfood == 'Third Result':
        userchoice.append(2)
        foodselection = 'You selected: ' + listofresults[0][2]['fields']['item_name']
        resultdesc = 'Item Description: ' + str(listofresults[0][2]['fields']['item_description'])  
        resultbrand = 'Brand: ' + listofresults[0][2]['fields']['brand_name'] 
        resultcals = 'Calories: ' + str(listofresults[0][2]['fields']['nf_calories']) 
        resultserving = 'Serving Size: ' + str(listofresults[0][2]['fields']['nf_serving_size_qty']) + ' ' + listofresults[0][2]['fields']['nf_serving_size_unit']
    elif userfood == 'Fourth Result':
        userchoice.append(3)
        foodselection = 'You selected: ' + listofresults[0][3]['fields']['item_name']
        resultdesc = 'Item Description: ' + str(listofresults[0][3]['fields']['item_description'])  
        resultbrand = 'Brand: ' + listofresults[0][3]['fields']['brand_name'] 
        resultcals = 'Calories: ' + str(listofresults[0][3]['fields']['nf_calories']) 
        resultserving = 'Serving Size: ' + str(listofresults[0][3]['fields']['nf_serving_size_qty']) + ' ' + listofresults[0][3]['fields']['nf_serving_size_unit']         
    elif userfood == 'Fifth Result':
        userchoice.append(4)
        foodselection = 'You selected: ' + listofresults[0][4]['fields']['item_name'] 
        resultdesc = 'Item Description: ' + str(listofresults[0][4]['fields']['item_description'])  
        resultbrand = 'Brand: ' + listofresults[0][4]['fields']['brand_name'] 
        resultcals = 'Calories: ' + str(listofresults[0][4]['fields']['nf_calories']) 
        resultserving = 'Serving Size: ' + str(listofresults[0][4]['fields']['nf_serving_size_qty']) + ' ' + listofresults[0][4]['fields']['nf_serving_size_unit']    
    return render_template("serving.html", foodselection = foodselection, resultdesc = resultdesc, resultbrand = resultbrand, resultcals = resultcals, resultserving =  resultserving)

@app.route('/nutrition', methods = ['POST', 'GET'])
def nutrition():
    """"""
    formdata3 = request.form
    userserving = formdata3['Which_size']
    x = userchoice[0]
    z = 0
    if userserving == '1/4':
        itemadded = 'Great job, you just added ' + userserving + ' servings of ' + listofresults[0][x]['fields']['item_name'] + ' from ' + listofresults[0][x]['fields']['brand_name']
        itemnut.append(listofresults[0][x]['fields']['nf_calories'])
        itemnut.append(listofresults[0][x]['fields']['nf_total_fat'])
        itemnut.append(listofresults[0][x]['fields']['nf_cholesterol'])
        itemnut.append(listofresults[0][x]['fields']['nf_sodium'])
        itemnut.append(listofresults[0][x]['fields']['nf_total_carbohydrate'])
        itemnut.append(listofresults[0][x]['fields']['nf_dietary_fiber'])
        itemnut.append(listofresults[0][x]['fields']['nf_sugars'])
        itemnut.append(listofresults[0][x]['fields']['nf_protein'])
        itemnut.append(listofresults[0][x]['fields']['nf_vitamin_a_dv'])
        itemnut.append(listofresults[0][x]['fields']['nf_vitamin_c_dv'])
        itemnut.append(listofresults[0][x]['fields']['nf_calcium_dv'])
        itemnut.append(listofresults[0][x]['fields']['nf_iron_dv'])
        servingnut = [i * .25 for i in itemnut]
        for c in dailynut:
            dailynut[c] = dailynut[c] + servingnut[z]
            z += 1
    if userserving == '1/2':
        itemadded = 'Great job, you just added ' + userserving + ' servings of ' + listofresults[0][x]['fields']['item_name'] + ' from ' + listofresults[0][x]['fields']['brand_name']
        itemnut.append(listofresults[0][x]['fields']['nf_calories'])
        itemnut.append(listofresults[0][x]['fields']['nf_total_fat'])
        itemnut.append(listofresults[0][x]['fields']['nf_cholesterol'])
        itemnut.append(listofresults[0][x]['fields']['nf_sodium'])
        itemnut.append(listofresults[0][x]['fields']['nf_total_carbohydrate'])
        itemnut.append(listofresults[0][x]['fields']['nf_dietary_fiber'])
        itemnut.append(listofresults[0][x]['fields']['nf_sugars'])
        itemnut.append(listofresults[0][x]['fields']['nf_protein'])
        itemnut.append(listofresults[0][x]['fields']['nf_vitamin_a_dv'])
        itemnut.append(listofresults[0][x]['fields']['nf_vitamin_c_dv'])
        itemnut.append(listofresults[0][x]['fields']['nf_calcium_dv'])
        itemnut.append(listofresults[0][x]['fields']['nf_iron_dv'])
        servingnut = [i * .5 for i in itemnut]
        for c in dailynut:
            dailynut[c] = dailynut[c] + servingnut[z]
            z += 1
    if userserving == '3/4':
        itemadded = 'Great job, you just added ' + userserving + ' servings of ' + listofresults[0][x]['fields']['item_name'] + ' from ' + listofresults[0][x]['fields']['brand_name']
        itemnut.append(listofresults[0][x]['fields']['nf_calories'])
        itemnut.append(listofresults[0][x]['fields']['nf_total_fat'])
        itemnut.append(listofresults[0][x]['fields']['nf_cholesterol'])
        itemnut.append(listofresults[0][x]['fields']['nf_sodium'])
        itemnut.append(listofresults[0][x]['fields']['nf_total_carbohydrate'])
        itemnut.append(listofresults[0][x]['fields']['nf_dietary_fiber'])
        itemnut.append(listofresults[0][x]['fields']['nf_sugars'])
        itemnut.append(listofresults[0][x]['fields']['nf_protein'])
        itemnut.append(listofresults[0][x]['fields']['nf_vitamin_a_dv'])
        itemnut.append(listofresults[0][x]['fields']['nf_vitamin_c_dv'])
        itemnut.append(listofresults[0][x]['fields']['nf_calcium_dv'])
        itemnut.append(listofresults[0][x]['fields']['nf_iron_dv'])
        servingnut = [i * .75 for i in itemnut]
        for c in dailynut:
            dailynut[c] = dailynut[c] + servingnut[z]
            z += 1
    if userserving == '1':
        itemadded = 'Great job, you just added ' + userserving + ' servings of ' + listofresults[0][x]['fields']['item_name'] + ' from ' + listofresults[0][x]['fields']['brand_name']
        itemnut.append(listofresults[0][x]['fields']['nf_calories'])
        itemnut.append(listofresults[0][x]['fields']['nf_total_fat'])
        itemnut.append(listofresults[0][x]['fields']['nf_cholesterol'])
        itemnut.append(listofresults[0][x]['fields']['nf_sodium'])
        itemnut.append(listofresults[0][x]['fields']['nf_total_carbohydrate'])
        itemnut.append(listofresults[0][x]['fields']['nf_dietary_fiber'])
        itemnut.append(listofresults[0][x]['fields']['nf_sugars'])
        itemnut.append(listofresults[0][x]['fields']['nf_protein'])
        itemnut.append(listofresults[0][x]['fields']['nf_vitamin_a_dv'])
        itemnut.append(listofresults[0][x]['fields']['nf_vitamin_c_dv'])
        itemnut.append(listofresults[0][x]['fields']['nf_calcium_dv'])
        itemnut.append(listofresults[0][x]['fields']['nf_iron_dv'])
        servingnut = [i * 1 for i in itemnut]
        for c in dailynut:
            dailynut[c] = dailynut[c] + servingnut[z]
            z += 1
    if userserving == '1.5':
        itemadded = 'Great job, you just added ' + userserving + ' servings of ' + listofresults[0][x]['fields']['item_name'] + ' from ' + listofresults[0][x]['fields']['brand_name']
        itemnut.append(listofresults[0][x]['fields']['nf_calories'])
        itemnut.append(listofresults[0][x]['fields']['nf_total_fat'])
        itemnut.append(listofresults[0][x]['fields']['nf_cholesterol'])
        itemnut.append(listofresults[0][x]['fields']['nf_sodium'])
        itemnut.append(listofresults[0][x]['fields']['nf_total_carbohydrate'])
        itemnut.append(listofresults[0][x]['fields']['nf_dietary_fiber'])
        itemnut.append(listofresults[0][x]['fields']['nf_sugars'])
        itemnut.append(listofresults[0][x]['fields']['nf_protein'])
        itemnut.append(listofresults[0][x]['fields']['nf_vitamin_a_dv'])
        itemnut.append(listofresults[0][x]['fields']['nf_vitamin_c_dv'])
        itemnut.append(listofresults[0][x]['fields']['nf_calcium_dv'])
        itemnut.append(listofresults[0][x]['fields']['nf_iron_dv'])
        servingnut = [i * 1.5 for i in itemnut]
        for c in dailynut:
            dailynut[c] = dailynut[c] + servingnut[z]
            z += 1
    if userserving == '2':
        itemadded = 'Great job, you just added ' + userserving + ' servings of ' + listofresults[0][x]['fields']['item_name'] + ' from ' + listofresults[0][x]['fields']['brand_name']
        itemnut.append(listofresults[0][x]['fields']['nf_calories'])
        itemnut.append(listofresults[0][x]['fields']['nf_total_fat'])
        itemnut.append(listofresults[0][x]['fields']['nf_cholesterol'])
        itemnut.append(listofresults[0][x]['fields']['nf_sodium'])
        itemnut.append(listofresults[0][x]['fields']['nf_total_carbohydrate'])
        itemnut.append(listofresults[0][x]['fields']['nf_dietary_fiber'])
        itemnut.append(listofresults[0][x]['fields']['nf_sugars'])
        itemnut.append(listofresults[0][x]['fields']['nf_protein'])
        itemnut.append(listofresults[0][x]['fields']['nf_vitamin_a_dv'])
        itemnut.append(listofresults[0][x]['fields']['nf_vitamin_c_dv'])
        itemnut.append(listofresults[0][x]['fields']['nf_calcium_dv'])
        itemnut.append(listofresults[0][x]['fields']['nf_iron_dv'])
        servingnut = [i * 2 for i in itemnut]
        for c in dailynut:
            dailynut[c] = dailynut[c] + servingnut[z]
            z += 1
    if userserving == '3':
        itemadded = 'Great job, you just added ' + userserving + ' servings of ' + listofresults[0][x]['fields']['item_name'] + ' from ' + listofresults[0][x]['fields']['brand_name']
        itemnut.append(listofresults[0][x]['fields']['nf_calories'])
        itemnut.append(listofresults[0][x]['fields']['nf_total_fat'])
        itemnut.append(listofresults[0][x]['fields']['nf_cholesterol'])
        itemnut.append(listofresults[0][x]['fields']['nf_sodium'])
        itemnut.append(listofresults[0][x]['fields']['nf_total_carbohydrate'])
        itemnut.append(listofresults[0][x]['fields']['nf_dietary_fiber'])
        itemnut.append(listofresults[0][x]['fields']['nf_sugars'])
        itemnut.append(listofresults[0][x]['fields']['nf_protein'])
        itemnut.append(listofresults[0][x]['fields']['nf_vitamin_a_dv'])
        itemnut.append(listofresults[0][x]['fields']['nf_vitamin_c_dv'])
        itemnut.append(listofresults[0][x]['fields']['nf_calcium_dv'])
        itemnut.append(listofresults[0][x]['fields']['nf_iron_dv'])
        servingnut = [i * 3 for i in itemnut]
        for c in dailynut:
            dailynut[c] = dailynut[c] + servingnut[z]
            z += 1
    itemfacts = 'The following nutrients were added to your daily totals'
    itemnut.clear()
    servingnut.clear() 
    userchoice.clear()            
    return render_template("nutrition.html", itemadded = itemadded, itemfacts = itemfacts)


if __name__ == '__main__':
    app.run(debug=True)