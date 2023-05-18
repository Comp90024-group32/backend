
import view_data
import utils
from urllib.parse import unquote

mastodon_marital_enum = ["married",'seperated','divorced','never married','widowed']
mastodon_employee_enum = ['service','technology','manufacture','Operators and drivers','Professionals']
mastodon_education_enum = ['preshool','primary','secondary','tertiary_vocational','tertiary_university','education','phd program','phd','doctorate','bachelor\'s degree','master\'s degree']

twitter_employee_enum = ['Operators and drivers', 'service', 'manufacture', 'Professionals', 'technology']
twitter_marital_enum = ['divorced', 'married', 'widowed', 'seperated']
twitter_education_enum = ['education', 'secondary', 'phd', 'primary', "master's degree", "bachelor's degree", 'phd program', 'tertiary_university', 'tertiary_vocational', 'preshool', 'doctorate']

education_level_enum = ['Type', 'Total', 'Tertiary', 'Other', 'Preschool', 'Primary', 'Secondary']
marital_status_enum = ['Widowed', 'Married', 'Never married', 'Divorced', 'Separated', 'Total']
employee_enum = ["Clerical and Administrative Workers","Labourers","Machinery Operators And Drivers","Managers","Professionals","Sales Workers","Technicians and Trades Workers",]
school_type_enum = ['type_of_education_institution_Full_time_student', 'catholic', 'Total_Primary', 'type_of_education_institution_Total', 'Total_Tertiary', 'of_education_institution_not_stated', 'type_of_education_institution_Part_time_student', 'Total_Secondary', 'other-non-government', 'type_of_education_institution_Full_time_Part_time_student_status_not_stated', 'government', 'university']
def marital_status(args):
    
    start_year = args.get('start_year')
    start_month = args.get('start_month')
    end_year = args.get('end_year')
    end_month = args.get('end_month')
    age_group = args.get('age_group')
    area = args.get('area')
    sex = args.get('sex')
    selected_age_group = age_group.split(',')
    selected_sex_group = sex.split(',')
    selected_area_group = area.split(',')

    source = args.get('source')
    selected_source_group = source.split(',')
    final_result = {}

    if "sudo" in selected_source_group:
        result = {}

        result["sex_marital_status"] = []
        result["age_marital_status"] = []
        result["area_marital_status"] = []
        for sex_para in selected_sex_group:
            for mar_para in marital_status_enum:
                count = 0
                data = view_data.view_sex_marital_status(sex_para,mar_para.capitalize())
                for item in data['rows']:
                    count += item['value']
                temp = {}
                temp['sex'] = sex_para
                temp['marital_status'] = mar_para
                temp['count'] = count
                result['sex_marital_status'].append(temp)
        for age_para in selected_age_group:
            for mar_para in marital_status_enum:
                count = 0
                data = view_data.view_age_marital_status(age_para,mar_para.capitalize())
                for item in data['rows']:
                    count += item['value']
                temp = {}
                temp['age'] = age_para
                temp['marital_status'] = mar_para
                temp['count'] = count
                result['age_marital_status'].append(temp)

        for area_para in selected_area_group:
            
            for mar_para in marital_status_enum:
                count = 0
                data = view_data.view_area_marital_status(area_para.upper(),mar_para.capitalize())
                for item in data['rows']:
                    count += item['value']
                temp = {}
                temp['area'] = area_para
                temp['marital_status'] = mar_para
                temp['count'] = count
                result['area_marital_status'].append(temp)
        final_result['sudo'] = result
    if 'twitter' in selected_source_group:
        result = {}
        result['time_marital_status'] = []
        if start_year != 0 and start_month != 0 and end_year != 0 and end_month != 0:
            time_list = utils.generate_time_list(int(start_year),int(start_month),int(end_year),int(end_month))
            for time in time_list:
                for mar_para in twitter_marital_enum:
                    data = view_data.view_twitter_time_marital(time[0],time[1],mar_para)
                    temp = {}
                    temp['time'] = f'{time[0]}-{time[1]}'
                    temp['marital_status'] = mar_para
                    temp['count'] = len(data['rows'])
                    result['time_marital_status'].append(temp)
        result['area_marital_status'] = []
        for area_para in selected_area_group:
            for mar_para in twitter_marital_enum:
                data = view_data.view_twitter_area_marital(area_para,mar_para)
                temp = {}
                temp['area'] = area_para
                temp['marital_status'] = mar_para
                temp['count'] = len(data['rows'])
                result['area_marital_status'].append(temp)
        final_result['twitter'] = result
    if 'mastodon' in selected_source_group:
        result = {}
        result['time_marital_status'] = []
        if start_year != 0 and start_month != 0 and end_year != 0 and end_month != 0:
            time_list = utils.generate_time_list(int(start_year),int(start_month),int(end_year),int(end_month))
            for time in time_list:
                for mar_para in mastodon_marital_enum:
                    data = view_data.view_mastodon_time_marital(time[0],time[1],mar_para)
                    temp = {}
                    count = 0
                    for item in data['rows']:
                        count += int(item['value'])
                    temp['time'] = f'{time[0]}-{time[1]}'
                    temp['marital_status'] = mar_para
                    temp['count'] = count
                    result['time_marital_status'].append(temp)
                    
        final_result['mastodon'] = result
    return final_result

def education(args):
    start_year = args.get('start_year')
    start_month = args.get('start_month')
    end_year = args.get('end_year')
    end_month = args.get('end_month')

    area = args.get('area')
    sex = args.get('sex')

    selected_sex_group = sex.split(',')
    selected_area_group = area.split(',')

    source = args.get('source')
    selected_source_group = source.split(',')
    final_result = {}

    if "sudo" in selected_source_group:
        result = {}      

        result["sex_education"] = []
        result["area_education"] = []
        result["sex_school_type"] = []
        result["area_school_type"] = []
        for sex_para in selected_sex_group:
            for edu_para in education_level_enum:
                count = 0
                
                data = view_data.view_sex_education(sex_para.lower().capitalize(),edu_para)
                for item in data['rows']:
                    count += item['value']
                temp = {}
                temp['sex'] = sex_para
                temp['education_level'] = edu_para
                temp['count'] = count
                result['sex_education'].append(temp)
        for sex_para in selected_sex_group:
            for sch_para in school_type_enum:
                count = 0
                
                data = view_data.view_sex_school(sex_para.lower().capitalize(),sch_para)
                for item in data['rows']:
                    count += item['value']
                temp = {}
                temp['sex'] = sex_para
                temp['school_type'] = edu_para
                temp['count'] = count
                result['sex_school_type'].append(temp)
        for area_para in selected_area_group:
            for edu_para in education_level_enum:
                count = 0
                
                data = view_data.view_area_education(area_para.upper(),edu_para)
                for item in data['rows']:
                    count += item['value']
                temp = {}
                temp['area'] = area_para
                temp['education_level'] = edu_para
                temp['count'] = count
                result['area_education'].append(temp)
        for area_para in selected_area_group:
            for sch_para in school_type_enum:
                count = 0
                data = view_data.view_area_school_type(area_para.upper(),sch_para)
                for item in data['rows']:
                    count += item['value']
                temp = {}
                temp['area'] = area_para
                temp['school_type'] = sch_para
                temp['count'] = count
                result['area_school_type'].append(temp)
        final_result['sudo'] = result
    if 'twitter' in selected_source_group:
        result = {}
        result['time_education'] = []
        if start_year != 0 and start_month != 0 and end_year != 0 and end_month != 0:
            time_list = utils.generate_time_list(int(start_year),int(start_month),int(end_year),int(end_month))
            for time in time_list:
                for edu_para in twitter_education_enum:
                    data = view_data.view_twitter_time_education(time[0],time[1],edu_para)
                    temp = {}
                    temp['time'] = f'{time[0]}-{time[1]}'
                    temp['education'] = edu_para
                    temp['count'] = len(data['rows'])
                    result['time_education'].append(temp)
        result['area_education'] = []
        for area_para in selected_area_group:
            for edu_para in twitter_education_enum:
                data = view_data.view_twitter_area_education(area_para,edu_para)
                temp = {}
                temp['area'] = area_para
                temp['education'] = edu_para
                temp['count'] = len(data['rows'])
                result['area_education'].append(temp)
        final_result['twitter'] = result
    if 'mastodon' in selected_source_group:
        result = {}
        result['time_education'] = []
        if start_year != 0 and start_month != 0 and end_year != 0 and end_month != 0:
            time_list = utils.generate_time_list(int(start_year),int(start_month),int(end_year),int(end_month))
            for time in time_list:
                for edu_para in education_level_enum:
                    data = view_data.view_mastodon_time_education(time[0],time[1],edu_para)
                    temp = {}
                    count = 0
                    for item in data['rows']:
                        count += int(item['value'])
                    temp['time'] = f'{time[0]}-{time[1]}'
                    temp['education'] = edu_para
                    temp['count'] = count
                    result['time_education'].append(temp)
                    
        final_result['mastodon'] = result
    return final_result

def employee(args):
    start_year = args.get('start_year')
    start_month = args.get('start_month')
    end_year = args.get('end_year')
    end_month = args.get('end_month')
    #income_group = args.get('income_group')
    area = args.get('area')
    sex = args.get('sex')
    type = args.get('type')
    #selected_income_group = income_group.split(',')
    selected_sex_group = sex.split(',')
    selected_area_group = area.split(',')
    selected_type_group = type.split(',')
    source = args.get('source')
    selected_source_group = source.split(',')
    final_result = {}

    if "sudo" in selected_source_group:    
        result = {}

        result["sex_employee"] = []
        result["type_employee"] = []
        result["area_employee"] = []

        for sex_para in selected_sex_group:
            for emp_para in employee_enum:
                count = 0
                
                data = view_data.view_sex_employee(sex_para.lower(),emp_para)
                for item in data['rows']:
                    count += item['value']
                temp = {}
                temp['sex'] = sex_para
                temp['employee_level'] = emp_para
                temp['count'] = count
                result['sex_employee'].append(temp)
        
        for type_para in selected_type_group:
            for emp_para in employee_enum:
                count = 0
                
                data = view_data.view_type_employee(type_para.replace("-", " "),emp_para)
                for item in data['rows']:
                    count += item['value']
                temp = {}
                temp['type'] = type_para.replace("-", " ")
                temp['employee'] = emp_para
                temp['count'] = count
                result['type_employee'].append(temp)
        
        for area_para in selected_area_group:
            for emp_para in employee_enum:
                count = 0
                
                data = view_data.view_area_employee(area_para.upper(),emp_para)
                for item in data['rows']:
                    count += item['value']
                temp = {}
                temp['area'] = area_para
                temp['employee_level'] = emp_para
                temp['count'] = count
                result['area_employee'].append(temp)
        final_result['sudo'] = result
    if 'twitter' in selected_source_group:
        result = {}
        result['time_employee'] = []
        if start_year != 0 and start_month != 0 and end_year != 0 and end_month != 0:
            time_list = utils.generate_time_list(int(start_year),int(start_month),int(end_year),int(end_month))
            for time in time_list:
                for emp_para in twitter_employee_enum:
                    data = view_data.view_twitter_time_employee(time[0],time[1],emp_para)
                    temp = {}
                    temp['time'] = f'{time[0]}-{time[1]}'
                    temp['employee'] = emp_para
                    temp['count'] = len(data['rows'])
                    result['time_employee'].append(temp)
        result['area_employee'] = []
        for area_para in selected_area_group:
            for emp_para in twitter_employee_enum:
                data = view_data.view_twitter_area_employee(area_para,emp_para)
                temp = {}
                temp['area'] = area_para
                temp['employee'] = emp_para
                temp['count'] = len(data['rows'])
                result['area_employee'].append(temp)
        final_result['twitter'] = result
    if 'mastodon' in selected_source_group:
        result = {}
        result['time_employee'] = []
        if start_year != 0 and start_month != 0 and end_year != 0 and end_month != 0:
            time_list = utils.generate_time_list(int(start_year),int(start_month),int(end_year),int(end_month))
            for time in time_list:
                for emp_para in mastodon_employee_enum:
                    data = view_data.view_mastodon_time_employee(time[0],time[1],emp_para)
                    temp = {}
                    count = 0
                    for item in data['rows']:
                        count += int(item['value'])
                    temp['time'] = f'{time[0]}-{time[1]}'
                    temp['employee'] = emp_para
                    temp['count'] = count
                    result['time_employee'].append(temp)
                    
        final_result['mastodon'] = result
    
    return final_result
def sample4():
    return 

def sample5():
    return 