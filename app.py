from flask import Flask
from flask import request, render_template
from nutritionapi import *

app = Flask(__name__)

listofresults = []
userchoice = []
reccomended_dvs = {'Calories': 2000, 'Fat': 78, 'Cholesterol': 300, 'Sodium': 2300, 'Carbohydrates': 275, 'Dietary Fiber': 28, 'Sugar': 50, 'Protein': 50, 'Vitamin A': 100, 'Vitamin C': 100, 'Calcium': 100, 'Iron': 100}
dailynut = {'Calories': 0, 'Fat': 0, 'Cholesterol': 0, 'Sodium': 0, 'Carbohydrates': 0, 'Dietary Fiber': 0, 'Sugar': 0, 'Protein': 0, 'Vitamin A': 0, 'Vitamin C': 0, 'Calcium': 0, 'Iron': 0}
itemnut = []
@app.route('/', methods = ['POST', 'GET'])
def hello():
    """Initial Screen for User to input a food item"""
    return render_template("index.html")

@app.route('/data', methods = ['POST', 'GET'])
def data():
    """Takes the Users search and displays to them the top results so they can select what fits best"""
    formdata = request.form
    userinput = formdata['Food']
    templist = initialsearch(userinput)
    listofresults.append(templist)
    if len(listofresults) == 0:
        return render_template('incorrect.html')
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
    """After they select their food item, this screen allows them to choose their serving size"""
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
    """Displays the nutrition info of the food they just added, then gives them a choice to either add a new one or see the end of day results"""
    formdata3 = request.form
    userserving = formdata3['Which_size']
    x = userchoice[0]
    z = 0
    p = 0
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
        for w in itemnut:
            if w == None:
                itemnut[p] = 0
            p += 1
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
        for w in itemnut:
            if w == None:
                itemnut[p] = 0
            p += 1
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
        for w in itemnut:
            if w == None:
                itemnut[p] = 0
            p += 1
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
        for w in itemnut:
            if w == None:
                itemnut[p] = 0
            p += 1
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
        for w in itemnut:
            if w == None:
                itemnut[p] = 0
            p += 1
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
        for w in itemnut:
            if w == None:
                itemnut[p] = 0
            p += 1 

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
        for w in itemnut:
            if w == None:
                itemnut[p] = 0
            p += 1
        servingnut = [i * 3 for i in itemnut]
        for c in dailynut:
            dailynut[c] = dailynut[c] + servingnut[z]
            z += 1
    itemfacts = 'The following nutrients were added to your daily totals:'
    itemcal = 'Calories: ' + str(servingnut[0]) 
    itemfat = 'Total Fat: ' + str(servingnut[1]) + 'g'
    itemcholesterol = 'Cholesterol: ' + str(servingnut[2]) + 'mg'
    itemsodium = 'Sodium: ' + str(servingnut[3]) + 'mg'
    itemcarbs = 'Total Carbohydrates: ' + str(servingnut[4]) + 'g'
    itemfiber = 'Fiber: ' + str(servingnut[5]) + 'g'
    itemsugar = 'Sugar: ' + str(servingnut[6]) + 'g'
    itemprotein = 'Protein: ' + str(servingnut[7]) + 'g'
    itemvita = 'Vitamin A: ' + str(servingnut[8]) + '%'
    itemvitc = 'Vitamin C: ' + str(servingnut[9]) + '%'
    itemcalc = 'Calcium: ' + str(servingnut[10]) + '%'
    itemiron = 'Iron: ' + str(servingnut[11]) + '%'
    listofresults.clear()
    itemnut.clear()
    servingnut.clear() 
    userchoice.clear()            
    return render_template("nutrition.html", itemadded = itemadded, itemfacts = itemfacts, itemvita = itemvita, itemvitc = itemvitc, itemcalc = itemcalc, itemiron = itemiron, itemfiber = itemfiber, itemsugar = itemsugar, itemprotein = itemprotein, itemsodium = itemsodium, itemcarbs = itemcarbs,  itemcal = itemcal, itemfat = itemfat, itemcholesterol = itemcholesterol)

@app.route('/dailytotals', methods = ['POST', 'GET'])
def final():
    """Final screen that shows your daily nutritional info versus what the reccomended daily values are"""
    finalcal = 'Calories: ' + str(dailynut['Calories'])
    finalfat = 'Total Fat: ' + str(dailynut['Fat']) + 'g'
    finalcholesterol = 'Cholesterol: ' + str(dailynut['Cholesterol']) + 'mg'
    finalsodium = 'Sodium: ' + str(dailynut['Sodium']) + 'mg'
    finalcarbs = 'Total Carbohydrates: ' + str(dailynut['Carbohydrates']) + 'g'
    finalfiber = 'Fiber: ' + str(dailynut['Dietary Fiber']) + 'g'
    finalsugar = 'Sugar: ' + str(dailynut['Sugar']) + 'g'
    finalprotein = 'Protein: ' + str(dailynut['Protein']) + 'g'
    finalvita = 'Vitamin A: ' + str(dailynut['Vitamin A']) + '%'
    finalvitc = 'Vitamin C: ' + str(dailynut['Vitamin C']) + '%'
    finalcalc = 'Calcium: ' + str(dailynut['Calcium']) + '%'
    finaliron = 'Iron: ' + str(dailynut['Iron']) + '%'  
    dvcal = 'Calories: ' + str(reccomended_dvs['Calories'])
    dvfat = 'Total Fat: ' + str(reccomended_dvs['Fat']) + 'g'
    dvcholesterol = 'Cholesterol: ' + str(reccomended_dvs['Cholesterol']) + 'mg'
    dvsodium = 'Sodium: ' + str(reccomended_dvs['Sodium']) + 'mg'
    dvcarbs = 'Total Carbohydrates: ' + str(reccomended_dvs['Carbohydrates']) + 'g'
    dvfiber = 'Fiber: ' + str(reccomended_dvs['Dietary Fiber']) + 'g'
    dvsugar = 'Sugar: ' + str(reccomended_dvs['Sugar']) + 'g'
    dvprotein = 'Protein: ' + str(reccomended_dvs['Protein']) + 'g'
    dvvita = 'Vitamin A: ' + str(reccomended_dvs['Vitamin A']) + '%'
    dvvitc = 'Vitamin C: ' + str(reccomended_dvs['Vitamin C']) + '%'
    dvcalc = 'Calcium: ' + str(reccomended_dvs['Calcium']) + '%'
    dviron = 'Iron: ' + str(reccomended_dvs['Iron']) + '%'
    propcal = dailynut['Calories'] /reccomended_dvs['Calories'] 
    propfat = dailynut['Fat'] /reccomended_dvs['Fat']
    propcholesterol = dailynut['Cholesterol'] /reccomended_dvs['Cholesterol']
    propsodium = dailynut['Sodium'] /reccomended_dvs['Sodium']
    propcarbs = dailynut['Carbohydrates'] /reccomended_dvs['Carbohydrates']
    propfiber = dailynut['Dietary Fiber'] /reccomended_dvs['Dietary Fiber'] 
    propsugar = dailynut['Sugar'] /reccomended_dvs['Sugar'] 
    propprotein = dailynut['Protein'] /reccomended_dvs['Protein'] 
    propvita = dailynut['Vitamin A'] /reccomended_dvs['Vitamin C'] 
    propvitc = dailynut['Vitamin C'] /reccomended_dvs['Vitamin C'] 
    propcalc = dailynut['Calcium'] /reccomended_dvs['Calcium'] 
    propiron = dailynut['Iron'] /reccomended_dvs['Iron'] 
    if propcal < 1:
        vscal = "Great Job staying under the reccomended daily value for calories"
    elif propcal > 1:
        vscal = "Yeah yeah you went over the Calorie goal, sometimes that slice of pizza is worth it"
    if propfat < 1:
        vsfat = "Great Job staying under the reccomended daily value for fat"
    elif propfat > 1:
        vsfat = "It's alright you ate a little too much fat today, who doesn't love butter"
    if propcholesterol < 1:
        vscholesterol = "Nice job you stayed under the reccomended value of cholesterol, no heart issues for you"
    elif propcholesterol > 1:
        vscholesterol = "Heart disease is the leading cause of death in America, don't add to that statistic"
    if propsodium < 1:
        vssodium = "Great Job staying under the reccomended daily value of sodium"
    elif propsodium > 1:
        vssodium = "Maybe lay off the hot dogs covered in soy sauce"
    if propcarbs < 1:
        vscarbs = "What??? Are you keto, eat some pasta, live a little"
    elif propcarbs > 1:
        vscarbs = "Who does not love pasta and bread"
    if propfiber < 1:
        vsfiber = "For the sake of your toilet eat some more fiber"
    elif propfiber > 1:
        vsfiber = "Great job, keep those movements regular"
    if propsugar < 1:
        vssugar = "Wow, you might be the one person in America who eats less than the reccomended value for sugar"
    elif propsugar > 1:
        vssugar = "Maybe just one less brownie for dessert..."
    if propprotein < 1:
        vsprotein = "Go geat yourself a steak (unless you are vegan, in whichcase get yourself some tofu or whatever you eat)"
    elif propprotein > 1:
        vsprotein = "There you go, get those gains in"
    if propvita < 1:
        vsvita = "Get some more Vitamin A in you, your eyes will thank you"
    elif propvita > 1:
        vsvita = "Great job, no glasses needed for you (unless you already wear glasses in which case sucks to suck)"
    if propvitc < 1:
        vsvitc = "You ever heard of an orange?"
    elif propvitc > 1:
        vsvitc = "No scurvy for you"
    if propiron < 1:
        vsiron = "Won't lie I think you will make it, what does iron even do for the body"
    elif propiron > 1:
        vsiron = "Nice work I guess, I think Iron is a good thing"
    if propcalc < 1:
        vscalc = "Drink some milk, get that bone density up"
    elif propcalc > 1:
        vscalc = "No broken bones for you"
    dailynut.clear()
    
    return render_template("final.html", vscal = vscal, vsiron = vsiron, vscalc = vscalc, vsvita = vsvita, vsvitc = vsvitc, vsfat = vsfat, vscholesterol = vscholesterol, vssugar = vssugar, vsfiber = vsfiber, vsprotein = vsprotein, vssodium = vssodium, vscarbs = vscarbs, propcal = propcal, finalcal = finalcal, finalfat = finalfat, finalcholesterol = finalcholesterol, finalsodium = finalsodium, finalcarbs = finalcarbs, finalfiber = finalfiber, finalsugar = finalsugar, finalprotein = finalprotein, finalvita = finalvita, finalvitc = finalvitc, finalcalc = finalcalc, finaliron = finaliron, dvcal = dvcal, dvfat = dvfat, dvcholesterol = dvcholesterol, dvsodium = dvsodium, dvcarbs = dvcarbs, dvfiber = dvfiber, dvsugar = dvsugar, dvprotein = dvprotein, dvvita = dvvita, dvvitc = dvvitc, dvcalc = dvcalc, dviron = dviron)

@app.errorhandler(404)
def error404(error):
    return render_template("error.html")
if __name__ == '__main__':
    app.run(debug=True)