#!/usr/bin/python3

###This Code is for generating a report using 3 functions to read the CSV file and generate a report with the total number of people in each department###

##The first function read_employees(csv_file_location) receives a CSV file as a parameter and returns a list of dictionaries from that file##
##The second function process_data(employee_list) receive the list of dictionaries, i.e., employee_list as a parameter and return a dictionary of department:amount##
##The third function write_report(dictionary,report_file) writes a dictionary of department: amount to a file##


import os 
import csv

def read_employees(csv_file_location):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)    #The dialect is to remove any leading spaces while parsing the CSV file.
    employee_file = csv.DictReader(open(csv_file_location), dialect='empDialect')     #here we opened the csv file and read it with DictReader
    employee_list = []       # When you iterate over a CSV file, each iteration of the loop produces a dictionary from strings (key) to strings (value).
    
    for data in employee_file:     #making a list of dictionaries(keys are the first row of the CSV file)
        employee_list.append(data)
    
    return employee_list

employee_list = read_employees('/home/student-03-a8228369b265/data/employees.csv')


def process_data(employee_list):
    deparmtent_list = []                                            #initialize a new list called department_list
    for employee_data in employee_list:                             #iterate over employee_list
        department_list.append(employee_data['Department'])         #and add only the departments into the department_list
                                                                    #We now have to remove the redundancy and return a dictionary
    department_data = {}
    for department_name in set(department_list):                    #we used set to get rid of the repeated data
        department_data[department_name] = department_list.count(department_name)
    
    return department_data

dictionary = process_data(employee_list)


def write_report(dictionary, report_file):                           
    with open(report_file, 'w+') as f:                                        #open the file with write+ permissions to create and write in it
        for k in sorted(dictionary):                                          #loop over the sorted dictionary 
            f.write(str(k)+ ':' + str(dictionary[k]) + '\n')                  #write the key(department) + ":" + the value inside each key
        f.close()

write_report(dictionary, '/home/student-03-a8228369b265/data/test_report.txt')












