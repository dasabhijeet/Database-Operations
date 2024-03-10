# import libraries
import mysql.connector
import json
import datetime
import time

# code execution time calculator (start here)
start_time = time.time()

# load configuration file
conf = json.load(open("/home/ubuntu/config.json"))

data = {}
data["host"] = conf['mysql']['host']
data["username"] = conf['mysql']['username']
data["password"] = conf['mysql']['password']
data["database"] = conf['mysql']['db']

'''
# MYSQL Connection settings global
con = mysql.connector.connect(user=data["username"], password=data["password"], database=data["database"], host=data["host"])
mycursor = con.cursor(buffered=True)
'''

# counter vars
count = 0
count1 = 0
count2 = 0
count3 = 0

# List inits
lib_record = []
database_record = []
database_record_yes = []
database_record_no = []
database_record_inp_id = []

# FUNCTION SECTION
def checkmain(y1,m1,d1,y2,m2,d2):
    global count
    global lib_record

    con = mysql.connector.connect(user=data["username"], password=data["password"], database=data["database"], host=data["host"])
    mycursor = con.cursor(buffered=True)

    # dynamic value assign in query
    query = ("SELECT c_id FROM tablemain WHERE datetime BETWEEN %s AND %s")
    date_start = datetime.date(y1, m1, d1)
    date_end = datetime.date(y2, m2, d2)
    mycursor.execute(query, (date_start, date_end))

    #result = mycursor.fetchone()
    #print(result)

    cursordata = mycursor.fetchall()
  
    for res in cursordata:
        res = delimiterremover(res)
        #print(res)
        lib_record.append(res)
        count = count + 1
        #break

    print("Iterations(tablemain): ",count)
    mycursor.close()
    con.close()

# function to remove delimiters and unnecessary special characters in ID fetching
def delimiterremover(result):
    result = str(result)
    result = result.replace("(","")
    result = result.replace("'","")
    result = result.replace(")","")
    result = result.replace(",","")
    result = result.replace(" ","")
    return result

# secondary table modification
def checkdatabasedb():
    global count1
    global database_record
    global database_record_yes
    global database_record_no
    global database_record_inp_id

    con = mysql.connector.connect(user=data["username"], password=data["password"], database=data["database"], host=data["host"])
    mycursor = con.cursor(buffered=True)

    query = ("SELECT c_id FROM sample_table_ WHERE identifier = %s")

    for c_inp_id in lib_record:
        
        mycursor.execute(query, (c_inp_id,))
        result = str(mycursor.fetchone())

        if result == 'None':
            database_record_no.append(c_inp_id)

        elif result != 'None':
            database_record_yes.append(c_inp_id)
            result = delimiterremover(result)
            database_record_inp_id.append(result)  
        
        count1 = count1 + 1
      
    print("Iterations (sample table 2): ",count1)
    
    mycursor.close()
    con.close()

#######################################
####### USER INPUT STARTS HERE ########
#######################################
# Date Range To Pass

# START RANGE
year1_start = 2024
month1_start = 2
day1_start = 28

# END RANGE
year2_end = 2024
month2_end = 2
day2_end = 29

###################

# Run function and pass 6 parameters

checkmain(year1_start,month1_start,day1_start,year2_end,month2_end,day2_end)

checkdatabasedb()

# execution time output
print("--- %s seconds ---" % (time.time() - start_time))

###################

########
# Github Repo Owner: https://github.com/dasabhijeet/
# Date: 10 March 2024 (last edited)
# Version: 01
########
