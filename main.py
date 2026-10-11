def employee_records(filename):
    with open(filename,"r") as file:
        headers = file.readline().strip().split(",")
        content = file.readlines()
        emp_list = list()
    for emp in content:
       employee = emp.strip().split(",")
       employee_detail = dict(zip(headers,employee))
       emp_list.append(employee_detail)
    return emp_list

employees = employee_records("employees.csv")



def find_duplicate_ids(employees):
    seen = set()
    duplicate = set()
    all_emp_id = []
    for emp in employees:
        all_emp_id.append(emp["employee_id"])
    for emp_id in all_emp_id:
        if emp_id in seen:
            duplicate.add(emp_id)
        else:
            seen.add(emp_id)
            
 
    return (list(duplicate))
   
    

def missing_values_detector(employees):
    result = []
    for emp in employees:
        for header,value in emp.items():
            if value == '':
                missing_value = {
                    "employee_id": emp["employee_id"],
                    "missing_fields": [header]
                }
                result.append(missing_value)
    return result
                

def find_invalid_salaries(employees):
    result = []
    for emp in employees:
        salary = emp["salary"]
        try:
            if int(salary) < 0:
                invalid_salary = {
                    "employee_id": emp["employee_id"],
                    "salary": salary
                }
                result.append(invalid_salary)
        except ValueError:
                invalid_salary = {
                    "employee_id": emp["employee_id"],
                    "salary": salary
                }
                result.append(invalid_salary)
    return result




def generate_quality_report(employees):
    total_records = len(employees)
    duplicate_ids = find_duplicate_ids(employees)
    duplicate_records = len(duplicate_ids)
    missing_values = missing_values_detector(employees)
    missing_values_count = len(missing_values)
    invalid_salaries = find_invalid_salaries(employees)
    invalid_salaries_count = len(invalid_salaries)
    final_report = {
        "total_records": total_records,
        "duplicate_count": duplicate_records,
        "duplicate_ids": duplicate_ids,
        "missing_count": missing_values_count,
        "missing_value_records": missing_values,
        "invalid_salary_count": invalid_salaries_count,
        "invalid_salary_records": invalid_salaries
    }

    return final_report

report = generate_quality_report(employees)
print(report)