import json
import requests
from urllib.parse import urlencode
from urllib.parse import quote  
# set up authentication credentials if necessary
auth = ('admin', 'password')

# specify the URL for the view

host = "172.26.131.143"
#host = "localhost"

employment_sudo = "employment-sudo"
employment_twitter = "employee-twitter"
education_sudo = "education-sudo"
education_twitter = "education-twitter"
marital_sudo = "marital-sudo"
marital_twitter = "marital-twitter"
mastodon_education = "education_v1"
mastodon_employee = "employee_v1"
mastodon_marital = "marital_v1"


def view_sex_education(para_sex,para_edu):
    url = f'http://{host}:5984/{education_sudo}/_design/my_design_doc/_view/sex_edu'
    # build the query parameters
    params = urlencode({"key": json.dumps([para_sex,para_edu])})

    # construct the full URL
    full_url = f'{url}?{params}'

    # make the request and get the response
    response = requests.get(full_url, auth=auth)

    return response.json()


def view_area_education(para_area,para_edu):
    url = f'http://{host}:5984/{education_sudo}/_design/my_design_doc/_view/area_edu'
    # build the query parameters
    params = urlencode({"key": json.dumps([para_area,para_edu])})

    # construct the full URL
    full_url = f'{url}?{params}'

    # make the request and get the response
    response = requests.get(full_url, auth=auth)

    return response.json()

def view_area_marital_status(area_para,mar_para):
    url = f'http://{host}:5984/{marital_sudo}/_design/my_design_doc/_view/area_mar'
    # build the query parameters
    params = urlencode({"key": json.dumps([area_para,mar_para])})

    # construct the full URL
    full_url = f'{url}?{params}'

    # make the request and get the response
    response = requests.get(full_url, auth=auth)

    return response.json()

def view_age_marital_status(age_para,mar_para):
    url = f'http://{host}:5984/{marital_sudo}/_design/my_design_doc/_view/age_mar'
    # build the query parameters
    params = urlencode({"key": json.dumps([age_para,mar_para])})

    # construct the full URL
    full_url = f'{url}?{params}'

    # make the request and get the response
    response = requests.get(full_url, auth=auth)

    return response.json()

def view_sex_marital_status(sex_para,mar_para):
    url = f'http://{host}:5984/{marital_sudo}/_design/my_design_doc/_view/sex_mar'
    # build the query parameters
    params = urlencode({"key": json.dumps([sex_para,mar_para])})

    # construct the full URL
    full_url = f'{url}?{params}'

    # make the request and get the response
    response = requests.get(full_url, auth=auth)

    return response.json()

def view_sex_employee(sex_para,emp_para):
    url = f'http://{host}:5984/{employment_sudo}/_design/my_design_doc/_view/sex_emp'
    # build the query parameters
    params = urlencode({"key": json.dumps([sex_para,emp_para])})

    # construct the full URL
    full_url = f'{url}?{params}'

    # make the request and get the response
    response = requests.get(full_url, auth=auth)

    return response.json()

def view_area_employee(area_para,emp_para):
    url = f'http://{host}:5984/{employment_sudo}/_design/my_design_doc/_view/area_emp'
        # build the query parameters
    params = urlencode({"key": json.dumps([area_para,emp_para])})

    # construct the full URL
    full_url = f'{url}?{params}'

    # make the request and get the response
    response = requests.get(full_url, auth=auth)

    return response.json()

def view_sex_school(sex_para,sch_para):
    url = f'http://{host}:5984/{education_sudo}/_design/my_design_doc/_view/sex_sch'
        # build the query parameters
    params = urlencode({"key": json.dumps([sex_para,sch_para])})

    # construct the full URL
    full_url = f'{url}?{params}'

    # make the request and get the response
    response = requests.get(full_url, auth=auth)

    return response.json()

def view_area_school_type(area_para,sch_para):
    url = f'http://{host}:5984/{education_sudo}/_design/my_design_doc/_view/area_sch'
    # build the query parameters
    params = urlencode({"key": json.dumps([area_para,sch_para])})

    # construct the full URL
    full_url = f'{url}?{params}'

    # make the request and get the response
    response = requests.get(full_url, auth=auth)

    return response.json()

def view_type_employee(type_para,emp_para):
    url = f'http://{host}:5984/{employment_sudo}/_design/my_design_doc/_view/type_emp'
    # build the query parameters
    params = urlencode({"key": json.dumps([type_para,emp_para])})

    # construct the full URL
    full_url = f'{url}?{params}'

    # make the request and get the response
    response = requests.get(full_url, auth=auth)

    return response.json()

def view_twitter_area_employee(area_para,emp_para):
    url = f'http://{host}:5984/{employment_twitter}/_design/my_design_doc/_view/area_emp'
    # build the query parameters
    params = urlencode({"key": json.dumps([area_para,emp_para])})

    # construct the full URL
    full_url = f'{url}?{params}'

    # make the request and get the response
    response = requests.get(full_url, auth=auth)

    return response.json()

def view_twitter_area_marital(area_para,mar_para):
    url = f'http://{host}:5984/{marital_twitter}/_design/my_design_doc/_view/area_mar'
    # build the query parameters
    params = urlencode({"key": json.dumps([area_para,mar_para])})

    # construct the full URL
    full_url = f'{url}?{params}'

    # make the request and get the response
    response = requests.get(full_url, auth=auth)

    return response.json()

def view_twitter_area_education(area_para,edu_para):
    url = f'http://{host}:5984/{education_twitter}/_design/my_design_doc/_view/area_edu'
    # build the query parameters
    params = urlencode({"key": json.dumps([area_para,edu_para])})

    # construct the full URL
    full_url = f'{url}?{params}'

    # make the request and get the response
    response = requests.get(full_url, auth=auth)

    return response.json()

def view_twitter_time_marital(start_year,start_month,mar_para):
    url = f'http://{host}:5984/{marital_twitter}/_design/my_design_doc/_view/time_mar'
    # build the query parameters
    params = urlencode({"key": json.dumps([start_year,start_month,mar_para])})

    # construct the full URL
    full_url = f'{url}?{params}'

    # make the request and get the response
    response = requests.get(full_url, auth=auth)

    return response.json()

def view_twitter_time_employee(start_year,start_month,emp_para):
    url = f'http://{host}:5984/{employment_twitter}/_design/my_design_doc/_view/time_emp'
    # build the query parameters
    params = urlencode({"key": json.dumps([start_year,start_month,emp_para]),'limit' : 10000})

    # construct the full URL
    full_url = f'{url}?{params}'

    # make the request and get the response
    response = requests.get(full_url, auth=auth)

    return response.json()

def view_twitter_time_education(start_year,start_month,edu_para):
    url = f'http://{host}:5984/{education_twitter}/_design/my_design_doc/_view/time_edu'
    # build the query parameters
    params = urlencode({"key": json.dumps([start_year,start_month,edu_para])})

    # construct the full URL
    full_url = f'{url}?{params}'

    # make the request and get the response
    response = requests.get(full_url, auth=auth)

    return response.json()

def view_mastodon_time_marital(start_year,start_month,mar_para):
    url = f'http://{host}:5984/{mastodon_marital}/_design/my_design_doc/_view/time_mar'
    # build the query parameters
    params = urlencode({"key": json.dumps([start_year,start_month,mar_para])})

    # construct the full URL
    full_url = f'{url}?{params}'

    # make the request and get the response
    response = requests.get(full_url, auth=auth)

    return response.json()
def view_mastodon_time_education(start_year,start_month,edu_para):
    url = f'http://{host}:5984/{mastodon_education}/_design/my_design_doc/_view/time_edu'
    # build the query parameters
    params = urlencode({"key": json.dumps([start_year,start_month,edu_para])})

    # construct the full URL
    full_url = f'{url}?{params}'

    # make the request and get the response
    response = requests.get(full_url, auth=auth)

    return response.json()
def view_mastodon_time_employee(start_year,start_month,emp_para):
    url = f'http://{host}:5984/{mastodon_employee}/_design/my_design_doc/_view/time_emp'
    # build the query parameters
    params = urlencode({"key": json.dumps([start_year,start_month,emp_para])})

    # construct the full URL
    full_url = f'{url}?{params}'

    # make the request and get the response
    response = requests.get(full_url, auth=auth)

    return response.json()
