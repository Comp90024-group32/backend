import json
from flask import Flask, jsonify
import couchdb
import requests
from urllib.parse import urlencode
import view_data
from urllib.parse import quote  
# set up authentication credentials if necessary
auth = ('admin', 'password')
"""
count = 0 
data = view_data.view_mastodon_time_marital(2023,5,"married")
print(data)
for item in data['rows']:
    count += item['value']
print(count)

# specify the URL for the view
url = 'http://localhost:5984/mydb/_design/testtime/_view/new-view'

# build the query parameters
start_date = quote('"2021-01-01T00:00:00.000Z"')
end_date = quote('"2023-08-31T23:59:59.999Z"')

# construct the full URL
full_url = f'{url}?startkey={start_date}&endkey={end_date}'

response = requests.get(full_url, auth=auth)
print(response.json()['rows'])

url = f'http://localhost:5984/mydb/_design/testtime/_view/new-view'
# build the query parameters

params = urlencode({"key": json.dumps([2022,2,"education"])})

# construct the full URL
full_url = f'{url}?{params}'

# make the request and get the response
response = requests.get(full_url, auth=auth)

print(response.json())



# specify the URL for the view
url = 'http://localhost:5984/mydb/_design/testtime/_view/re'

# build the query parameters
start_date = quote('"2021-01-01T00:00:00.000Z"')
end_date = quote('"2023-08-31T23:59:59.999Z"')

# construct the full URL
full_url = f'{url}?startkey={start_date}&endkey={end_date}'

# make the request and get the response
response = requests.get(full_url, auth=auth)
print(response.json()['rows'])
"""
host = "115.146.93.109"
def view_mastodon_time_education(start_year,start_month,start_day,edu_para):
    url = f'http://{host}:5984/education_v1/_design/my_design_doc/_view/time_edu'
    # build the query parameters
    params = urlencode({"key": json.dumps([start_year,start_month,start_day,edu_para])})

    # construct the full URL
    full_url = f'{url}?{params}'

    # make the request and get the response
    response = requests.get(full_url, auth=auth)

    return response.json()
print(view_mastodon_time_education(2023,5,13,'preshool'))


"""
education_level_enum = ["Tertiary","Primary","Other","Preschool","Type","Secondary"]

def marital_status():
    result = {}

    result["sex_education"] = []
    result["income_education"] = []
    result["area_education"] = []

    for sex_para in ['Persons','Males']:
        for edu_para in education_level_enum:
            count = 0
            data = view_data.view_sex_education(sex_para,edu_para)
            #print(data)
            for item in data['rows']:
                count += item['value']['count_val']
            temp = {}
            temp['sex'] = sex_para
            temp['education_level'] = edu_para
            temp['count'] = count
            result['sex_education'].append(temp)
    
    for income_para in []:
        for edu_para in education_level_enum:
            count = 0
            data = view_data.view_income_education(income_para,edu_para)
            for item in data['rows']:
                count += item['value']['count_val']
            temp = {}
            temp['income'] = income_para
            temp['education_level'] = edu_para
            temp['count'] = count
            result['income_education'].append(temp)

    for area_para in []:
        for edu_para in education_level_enum:
            count = 0
            data = view_data.view_area_education(area_para,edu_para)
            for item in data['rows']:
                count += item['value']['count_val']
            temp = {}
            temp['area'] = area_para
            temp['education_level'] = edu_para
            temp['count'] = count
            result['area_education'].append(temp)
    
    print(result)
    return result


marital_status()
"""

"""
host = "115.146.93.109"
couchdb_url = f"http://{host}:5984"
username = "admin"
password = "password"
auth = (username,password)
def create_design_document(database_url, design_doc,database_name):
    response = requests.put(f"{database_url}/{database_name}/_design/my_design_doc", json=design_doc,auth=auth)
    if response.ok:
        print("Design document created successfully.")
    else:
        print("Failed to create design document:", response.text)

mastodon_design_document_edu = {
  
  "views": {
    "time_edu": {
      "map": "function (doc) {\n  var parts = doc.day.split(':');\n  var year = parseInt(parts[0]);\n  var month = parseInt(parts[1]);\n var day = parseInt(parts[2]);\n emit([year, month,day,doc['key_word']], parseInt(doc['count_users']));\n}"
    }
  }
}
create_design_document(couchdb_url, mastodon_design_document_edu,database_name="education_v1")

mastodon_design_document_mar = {
  
  "views": {
    "time_mar": {
      "map": "function (doc) {\n  var parts = doc.day.split(':');\n  var year = parseInt(parts[0]);\n  var month = parseInt(parts[1]);\n var day = parseInt(parts[2]);\n emit([year, month,day,doc['key_word']], parseInt(doc['count_users']));\n}"
    }
  }
}
create_design_document(couchdb_url, mastodon_design_document_mar,database_name="marital_v1")

mastodon_design_document_emp = {
  
  "views": {
    "time_emp": {
      "map": "function (doc) {\n  var parts = doc.day.split(':');\n  var year = parseInt(parts[0]);\n  var month = parseInt(parts[1]);\n var day = parseInt(parts[2]);\n emit([year, month,day,doc['key_word']], parseInt(doc['count_users']));\n}"
    }
  }
}
create_design_document(couchdb_url, mastodon_design_document_emp,database_name="employee_v1")
"""