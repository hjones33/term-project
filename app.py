from flask import Flask
from flask import request, render_template
from nutritionapi import *

app = Flask(__name__)

global listofresults
listofresults = []
@app.route('/', methods = ['POST', 'GET'])
def hello():
    return render_template("index.html")

@app.route('/data', methods = ['POST', 'GET'])
def data():
    formdata = request.form
    userinput = formdata['Food']
    listofresults = initialsearch(userinput)
    result1 = 'First Result: ' + listofresults[0]['fields']['item_name'] 
    result1desc = 'Item Description: ' + str(listofresults[0]['fields']['item_description'])  
    result1brand = 'Brand: ' + listofresults[0]['fields']['brand_name'] 
    result1cals = 'Calories: ' + str(listofresults[0]['fields']['nf_calories']) 
    result1serving = 'Serving Size: ' + str(listofresults[0]['fields']['nf_serving_size_qty']) + ' ' + listofresults[0]['fields']['nf_serving_size_unit']
    result2 = 'Second Result: ' + listofresults[1]['fields']['item_name'] 
    result2desc = 'Item Description: ' + str(listofresults[1]['fields']['item_description'])  
    result2brand = 'Brand: ' + listofresults[1]['fields']['brand_name'] 
    result2cals = 'Calories: ' + str(listofresults[1]['fields']['nf_calories']) 
    result2serving = 'Serving Size: ' + str(listofresults[1]['fields']['nf_serving_size_qty']) + ' ' + listofresults[1]['fields']['nf_serving_size_unit']
    result3 = 'Third Result: ' + listofresults[2]['fields']['item_name'] 
    result3desc = 'Item Description: ' + str(listofresults[2]['fields']['item_description'])  
    result3brand = 'Brand: ' + listofresults[2]['fields']['brand_name'] 
    result3cals = 'Calories: ' + str(listofresults[2]['fields']['nf_calories']) 
    result3serving = 'Serving Size: ' + str(listofresults[2]['fields']['nf_serving_size_qty']) + ' ' + listofresults[2]['fields']['nf_serving_size_unit']
    result4 = 'Fourth Result: ' + listofresults[3]['fields']['item_name'] 
    result4desc = 'Item Description: ' + str(listofresults[3]['fields']['item_description'])  
    result4brand = 'Brand: ' + listofresults[3]['fields']['brand_name'] 
    result4cals = 'Calories: ' + str(listofresults[3]['fields']['nf_calories']) 
    result4serving = 'Serving Size: ' + str(listofresults[3]['fields']['nf_serving_size_qty']) + ' ' + listofresults[3]['fields']['nf_serving_size_unit']
    result5 = 'Fifth Result: ' + listofresults[4]['fields']['item_name'] 
    result5desc = 'Item Description: ' + str(listofresults[4]['fields']['item_description'])  
    result5brand = 'Brand: ' + listofresults[4]['fields']['brand_name'] 
    result5cals = 'Calories: ' + str(listofresults[4]['fields']['nf_calories']) 
    result5serving = 'Serving Size: ' + str(listofresults[4]['fields']['nf_serving_size_qty']) + ' ' + listofresults[4]['fields']['nf_serving_size_unit']
    return render_template("results.html", result1 = result1, result1desc = result1desc, result1brand = result1brand, result1cals = result1cals, result1serving = result1serving, result2 = result2, result2desc = result2desc, result2brand = result2brand, result2cals = result2cals, result2serving = result2serving, result3 = result3, result3desc = result3desc, result3brand = result3brand, result3cals = result3cals, result3serving = result3serving, result4 = result4, result4desc = result4desc, result4brand = result4brand, result4cals = result4cals, result4serving = result4serving, result5 = result5, result5desc = result5desc, result5brand = result5brand, result5cals = result5cals, result5serving = result5serving)

@app.route('/serving', methods = ['POST', 'GET'])
def serving():
    formdata2 = request.form
    userfood = formdata2['Which_food']
    if userfood == 'First Result':
        foodselection = 'You selected:' + listofresults[0]['fields']['item_name'] 



if __name__ == '__main__':
    app.run(debug=True)