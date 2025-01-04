import requests
import json
import os

def FoodData(query):
    
    api_url = f'https://api.nal.usda.gov/fdc/v1/foods/search?api_key=your_api_key_hear&query={query}'

    #get api key form " https://fdc.nal.usda.gov/api-key-signup " hear and pest it
    #free api by US gov to use 

    response = requests.get(api_url)

    if response.status_code == 200: # check the connection beetwin the api it perfet if it then it satus_code it 200 
        #status_code is inbuilt funtion in requests modyl to chek connetion  

        data = response.json() #fetch the data from the api and store it in to data varible
        return data #retun store data

    else:
        print("Error:", response.status_code) #if any issue the show the code (ex. 404 not found etc)
        return None

if __name__ == "__main__": #for can be use as module in ither file if this functon need

    query = input("Enter the food name:- ") #enter food name for search

    food_info = FoodData(query) #calling function

    if food_info:  #if food_inof get data then it"s true so it enter the if statment
        file_path = f"your_file_path\\{query + " " + "info"}.json" 

        if os.path.exists(file_path):  #check if file exits in the that path
            print("File already exists.")  

        else:  
            with open(file_path, 'w') as file:  #if file no exits then it save data from the api in json file
                json.dump(food_info, file, indent=4)  #write the dicsnory formet data in .json file
            print(f"File created at {file_path}")  #show where it save the file


"""
***what can be improve****
featch only importent data like protin, vitamins data from the api
"""
