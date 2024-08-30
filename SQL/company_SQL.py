import mysql.connector as mycont

config={
    'user':'root',
    'password':'36025343',
    'host':'127.0.0.1',
}

def get_name(username,password):
    con = mycont.connect(**config) 
    cursor = con.cursor(buffered=True)
    cursor.execute("use company")
    cursor.execute("select * from employee")

    rows = cursor.fetchall()
    for row in rows:

        if str(row[0]) == str(username) and row[2] == str(password):  
            return row[1]
        
    return False

def start_search(username,password):
    con = mycont.connect(**config) 
    cursor = con.cursor(buffered=True)
    cursor.execute("use company")
    cursor.execute("select * from employee")

    rows = cursor.fetchall()
    for row in rows:

        if str(row[0]) == str(username) and row[2] == str(password):
            print(f"{row[1]}登入成功")
            
            return True
        
    return False

def window_one_all():
    con = mycont.connect(**config) 
    cursor = con.cursor(buffered=True)
    cursor.execute("USE company")
    cursor.execute("SELECT * FROM employee order by Employee_ID")

    rows = cursor.fetchall()
    return rows

def window_one_add(ID,Name,password,department,position,sex,phone,address):
    try:
        con = mycont.connect(**config) 
        cursor = con.cursor(buffered=True)
        cursor.execute("USE company")
        cursor.execute(f"INSERT INTO employee (Employee_ID,Employee_Name,Employee_Password,Department_Name,LV,Sex,Phone,Address) VALUES ({int(ID)},'{Name}','{password}','{department}','{position}','{sex}','{phone}','{address}')")

        cursor.execute(f"INSERT INTO salary (Employee_ID, Department_Name, LV, salary, PA) VALUES ({ID},'{department}','{position}',30000,1)")
        con.commit()
    except:
        return False

    return True

def window_one_delete(ID):
    try:
        con = mycont.connect(**config)
        cursor = con.cursor(buffered=True)
        cursor.execute("USE company")
        cursor.execute("SET SQL_SAFE_UPDATES = 0")
        cursor.execute(f"select *  FROM employee WHERE Employee_ID = {ID}")

        if(cursor.rowcount == 0):
            return False
        else:
            cursor.execute(f"DELETE FROM salary WHERE Employee_ID = {ID}")
            cursor.execute(f"DELETE FROM employee WHERE Employee_ID = {ID}")
        
        con.commit()

    except:
        return False
    
    return True

def window_one_search(ID, Name, department, lv):
    con = mycont.connect(**config) 
    cursor = con.cursor(buffered=True)
    cursor.execute("USE company")
    
    print(type(ID), type(Name), department, type(lv))

    query = "SELECT * FROM employee WHERE 1=1"

    if(ID or Name or department or lv != ''):
        if ID:
            query += f" AND Employee_ID = {ID}"
        if Name:
            query += f" AND Employee_Name = {Name}"
        if department:
            query += f" AND Department_Name = '{department}'"
        if lv:
            query += f" AND Lv = '{lv}'"
    else:
        return []

    cursor.execute(query)
    rows = cursor.fetchall()
    return rows

def window_two_reset():

    try:
        con = mycont.connect(**config)
        cursor = con.cursor(buffered=True)
        cursor.execute("USE company")
        cursor.execute("SET SQL_SAFE_UPDATES = 0")

        cursor.execute("UPDATE salary SET PA = 0")
        con.commit()
    except:
        return False

def window_two_update(department):

    try:
        con = mycont.connect(**config)
        cursor = con.cursor(buffered=True)
        cursor.execute("USE company")
        cursor.execute(f"select * from salary where Department_Name = '{department}' order by salary desc")
        rows = cursor.fetchall()

        return rows
    except:
        return False

def window_two_change(ID,PA):

    try:
        con = mycont.connect(**config)
        cursor = con.cursor(buffered=True)
        cursor.execute("USE company")
        cursor.execute(f"select * from salary where Employee_ID = {ID}")
        row = cursor.fetchone()

        if(row):
            cursor.execute(f"UPDATE salary SET PA = {PA} WHERE Employee_ID = {ID}")
            con.commit()
            return True
        else:
            return False


    except:
        return False

def window_three_PA():

    try:
        con = mycont.connect(**config)
        cursor = con.cursor(buffered=True)
        cursor.execute("USE company")
        cursor.execute("select Employee_ID,PA,(PA+salary) from salary order by PA desc ")
        rows = cursor.fetchall()

        return rows
    except:
        return False

def window_three_salary():

    try:
        con = mycont.connect(**config)
        cursor = con.cursor(buffered=True)
        cursor.execute("USE company")
        cursor.execute("select Employee_ID,PA,(PA+salary) from salary order by salary desc ")
        rows = cursor.fetchall()

        return rows
    except:
        return False


