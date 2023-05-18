import requests

host = "115.146.93.109"
couchdb_url = f"http://{host}:5984"
username = "admin"
password = "password"
auth = (username,password)

employment_sudo = ""
employment_twitter = ""
education_sudo = ""
education_twitter = ""
marital_sudo = ""
marital_twiter = ""
mastodon_education = "education_v1"
mastodon_employee = "employee_v1"
mastodon_marital = "marital_v1"

def create_design_document(database_url, design_doc,database_name):
    response = requests.put(f"{database_url}/{database_name}/_design/my_design_doc", json=design_doc,auth=auth)
    if response.ok:
        print("Design document created successfully.")
    else:
        print("Failed to create design document:", response.text)

design_document_edu = {
  
  "views": {
    "sex_edu": {
      "map": "function (doc) {\n       emit([doc.sex,doc.education_level], doc.count_val);\n  }"
    },
    "area_edu": {
      "map": "function (doc) {\n       emit([doc.area,doc.education_level], doc.count_val);\n  }"
    },
    "sex_sch": {
      "map": "function (doc) {\n       emit([doc.sex,doc.school_type], doc.count_val);\n  }"
    },
    "area_sch": {
      "map": "function (doc) {\n       emit([doc.area,doc.school_type], doc.count_val);\n  }"
    }   
  }
}
create_design_document(couchdb_url, design_document_edu,database_name=education_sudo)

design_document_mar = {
  
  "views": {
    "sex_mar": {
      "map": "function (doc) {\n       emit([doc.sex,doc.marital_status], doc.count_val);\n  }"
    },
    "area_mar": {
      "map": "function (doc) {\n       emit([doc.area,doc.marital_status], doc.count_val);\n  }"
    },
    "age_mar": {
      "map": "function (doc) {\n       emit([doc.age,doc.marital_status], doc.count_val);\n  }"
    }
  }
}
create_design_document(couchdb_url, design_document_mar,database_name=marital_sudo)

design_document_emp = {
  
  "views": {
    "sex_emp": {
      "map": "function (doc) {\n       emit([doc.type,doc.occupation], doc.count_val);\n  }"
    },
    "area_emp": {
      "map": "function (doc) {\n       emit([doc.area,doc.occupation], doc.count_val);\n  }"
    },
    "type_emp": {
      "map": "function (doc) {\n       emit([doc.type,doc.occupation], doc.count_val);\n  }"
    }
  }
}
create_design_document(couchdb_url, design_document_emp,database_name=employment_sudo)

mastodon_design_document_edu = {
  
  "views": {
    "time_edu": {
      "map": "function (doc) {\n  var parts = doc.day.split(':');\n  var year = parseInt(parts[0]);\n  var month = parseInt(parts[1]);\n var day = parseInt(parts[2]);\n emit([year, month,day,doc['key_word']], parseInt(doc['count_users']));\n}"
    }
  }
}
create_design_document(couchdb_url, mastodon_design_document_edu,database_name=mastodon_education)

mastodon_design_document_mar = {
  
  "views": {
    "time_mar": {
      "map": "function (doc) {\n  var parts = doc.day.split(':');\n  var year = parseInt(parts[0]);\n  var month = parseInt(parts[1]);\n var day = parseInt(parts[2]);\n emit([year, month,day,doc['key_word']], parseInt(doc['count_users']));\n}"
    }
  }
}
create_design_document(couchdb_url, mastodon_design_document_mar,database_name=mastodon_marital)

mastodon_design_document_emp = {
  
  "views": {
    "time_emp": {
      "map": "function (doc) {\n  var parts = doc.day.split(':');\n  var year = parseInt(parts[0]);\n  var month = parseInt(parts[1]);\n var day = parseInt(parts[2]);\n emit([year, month,day,doc['key_word']], parseInt(doc['count_users']));\n}"
    }
  }
}
create_design_document(couchdb_url, mastodon_design_document_emp,database_name=mastodon_employee)

twitter_design_document_edu = {
    "views":{
        "time_edu":{
             "map": "function(doc) { if(doc && doc['create_at:'] && doc.key) { var date = new Date(doc['create_at:']); emit([date.getFullYear(), date.getMonth()+1,doc.key], 1); }}"
        },
        "area_edu":{
             "map": "function(doc) { if(doc && doc.gcc && doc.key) {  emit([doc.gcc,doc.key], 1); }}"
        }
    }
}
create_design_document(couchdb_url, twitter_design_document_edu,database_name=education_twitter)

twitter_design_document_mar = {
    "views":{
        "time_mar":{
             "map": "function(doc) { if(doc && doc['create_at:'] && doc.key) { var date = new Date(doc['create_at:']); emit([date.getFullYear(), date.getMonth()+1,doc.key], 1); }}"
        },
        "area_mar":{
             "map": "function(doc) { if(doc && doc.gcc && doc.key) {  emit([doc.gcc,doc.key], 1); }}"
        }
    }
}
create_design_document(couchdb_url, twitter_design_document_mar,database_name=marital_twiter)

twitter_design_document_emp = {
    "views":{
        "time_emp":{
             "map": "function(doc) { if(doc && doc['create_at:'] && doc.key) { var date = new Date(doc['create_at:']); emit([date.getFullYear(), date.getMonth()+1,doc.key], 1); }}"
        },
        "area_emp":{
             "map": "function(doc) { if(doc && doc.gcc && doc.key) {  emit([doc.gcc,doc.key], 1); }}"
        }
    }
}
create_design_document(couchdb_url, twitter_design_document_emp,database_name=employment_twitter)