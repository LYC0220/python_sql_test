import tkinter as tk
from tkinter import ttk
import company_SQL as sql

def check_login():
    username = username_entry.get()
    password = password_entry.get()

    if(sql.start_search(username,password)):
        global name
        name = sql.get_name(username,password)
        login_success()
    else:
        error_label.config(text="帳號或密碼錯誤")  

def login_success():
    login_window.destroy()
    main_window()

def new_window_one():

    def search():
        ID = search_ID_entry.get()
        Name = search_Name_entry.get()
        Department = search_department_entry.get()
        LV = search_LV_entry.get()

        results = sql.window_one_search(ID,Name,Department,LV)

        for row in tree.get_children():
            tree.delete(row)

        for result in results:
            tree.insert("", "end", values=(result[0], result[1], result[3], result[4], result[5] ,result[6], result[7]))
    
    def all():
        results = sql.window_one_all()

        for row in tree.get_children():
            tree.delete(row)

        for result in results:
            tree.insert("", "end", values=(result[0], result[1], result[3], result[4], result[5] ,result[6], result[7]))

    def add():
        add_window = tk.Toplevel()
        add_window.geometry("250x350+900+300")
        add_window.resizable(False, False)
        add_window.title("新增員工資料")

        ID_label = tk.Label(add_window, text="員工編號:")
        ID_label.place(x=50, y=20, anchor="center")

        ID_entry = tk.Entry(add_window)
        ID_entry.place(x=150, y=20, anchor="center")

        add_Name_label = tk.Label(add_window, text="員工姓名:")
        add_Name_label.place(x=50, y=50, anchor="center")

        add_Name_entry = tk.Entry(add_window)
        add_Name_entry.place(x=150, y=50, anchor="center")

        passwort_label = tk.Label(add_window, text="員工密碼:")
        passwort_label.place(x=50, y=80, anchor="center")

        password_entry = tk.Entry(add_window)
        password_entry.place(x=150, y=80, anchor="center")

        department_label = tk.Label(add_window, text="部門名稱:")
        department_label.place(x=50, y=110, anchor="center")

        department_entry = tk.Entry(add_window)
        department_entry.place(x=150, y=110, anchor="center")

        position_label = tk.Label(add_window, text="員工職位:")
        position_label.place(x=50, y=140, anchor="center")

        position_entry = tk.Entry(add_window)
        position_entry.place(x=150, y=140, anchor="center")

        sex_label = tk.Label(add_window, text="員工性別:")
        sex_label.place(x=50, y=170, anchor="center")

        sex_entry = tk.Entry(add_window)
        sex_entry.place(x=150, y=170, anchor="center")

        phone_label = tk.Label(add_window, text="員工電話:")
        phone_label.place(x=50, y=200, anchor="center")

        phone_entry = tk.Entry(add_window)
        phone_entry.place(x=150, y=200, anchor="center")

        address_label = tk.Label(add_window, text="員工地址:")
        address_label.place(x=50, y=230, anchor="center")

        address_entry = tk.Entry(add_window)
        address_entry.place(x=150, y=230, anchor="center")

        def add_data():
            ID = ID_entry.get()
            Name = add_Name_entry.get()
            password = password_entry.get()
            department = department_entry.get()
            position = position_entry.get()
            sex = sex_entry.get()
            phone = phone_entry.get()
            address = address_entry.get()

            if(sql.window_one_add(ID,Name,password,department,position,sex,phone,address)):
                error_label.config(text="資料輸入成功")
            else:
                error_label.config(text="資料輸入失敗")

        add_button = tk.Button(add_window, text="新增資料")
        add_button.config(width=20,height=1)
        add_button.place(x=125, y=270, anchor="center")
        add_button.config(command=add_data)

        error_label = tk.Label(add_window, text="", fg="red")
        error_label.place(x=125, y=320, anchor="center")

    def delete():
        delete_window = tk.Toplevel()
        delete_window.geometry("250x150+900+300")
        delete_window.resizable(False, False)
        delete_window.title("刪除員工資料")

        label = tk.Label(delete_window, text='刪除員工資料')
        label.config(font=("微軟正黑體", 15))
        label.place(x=125, y=20,anchor="center")

        ID_label = tk.Label(delete_window, text="員工編號:")
        ID_label.place(x=50, y=70, anchor="center")

        ID_entry = tk.Entry(delete_window)
        ID_entry.place(x=150, y=70, anchor="center")

        def delete_data():
            ID = ID_entry.get()

            if(sql.window_one_delete(ID)):
                error_label.config(text="資料成功刪除")
            else:
                error_label.config(text="查無此資料")
        
        delete_button = tk.Button(delete_window, text="刪除資料")
        delete_button.config(width=20,height=1)
        delete_button.place(x=125, y=110, anchor="center")
        delete_button.config(command=delete_data)

        error_label = tk.Label(delete_window, text="", fg="red")
        error_label.place(x=125, y=140, anchor="center")



    new_window_one = tk.Toplevel()
    new_window_one.geometry("800x600+900+300")
    new_window_one.resizable(False, False)
    new_window_one.title("查詢員工資料")

    title_label = tk.Label(new_window_one, text="查詢員工資料", font=("微軟正黑體", 20))
    title_label.place(x=400, y=35, anchor="center")

    search_ID_label = tk.Label(new_window_one, text="員工編號:")
    search_ID_label.place(x=200, y=80, anchor="center")

    search_ID_entry = tk.Entry(new_window_one)
    search_ID_entry.place(x=300, y=80, anchor="center")

    search_Name_label = tk.Label(new_window_one, text="員工姓名:")
    search_Name_label.place(x=200, y=110, anchor="center")

    search_Name_entry = tk.Entry(new_window_one)
    search_Name_entry.place(x=300, y=110, anchor="center")

    search_department_label = tk.Label(new_window_one, text="部門名稱:")
    search_department_label.place(x=440, y=80, anchor="center")

    search_department_entry = tk.Entry(new_window_one)
    search_department_entry.place(x=540, y=80, anchor="center")

    search_LV_label = tk.Label(new_window_one, text="部門職位:")
    search_LV_label.place(x=440, y=110, anchor="center")

    search_LV_entry = tk.Entry(new_window_one)
    search_LV_entry.place(x=540, y=110, anchor="center")

    search_button = tk.Button(new_window_one, text="選項查詢")
    search_button.config(width=20,height=1)
    search_button.place(x=320, y=145, anchor="center")
    search_button.config(command=search)

    search_all_button = tk.Button(new_window_one, text="全部列出")
    search_all_button.config(width=20,height=1)
    search_all_button.place(x=480, y=145, anchor="center")
    search_all_button.config(command=all)

    add_button = tk.Button(new_window_one, text="新增資料")
    add_button.config(width=20,height=1)
    add_button.place(x=320, y=180, anchor="center")
    add_button.config(command=add)

    delete_button = tk.Button(new_window_one, text="刪除資料")
    delete_button.config(width=20,height=1)
    delete_button.place(x=480, y=180, anchor="center")
    delete_button.config(command=delete)

    columns = ("ID", "Name", "Department", "Position", "Sex", "Phone", "address")
    tree = ttk.Treeview(new_window_one, columns=columns, show='headings')

    tree.heading("ID", text="員工編號")
    tree.column("ID", width=60,anchor="center")
    tree.heading("Name", text="員工姓名")
    tree.column("Name", width=60,anchor="center")
    tree.heading("Department", text="部門")
    tree.column("Department", width=60,anchor="center")
    tree.heading("Position", text="職位")
    tree.column("Position", width=60,anchor="center")
    tree.heading("Sex", text="性別")
    tree.column("Sex", width=20,anchor="center")
    tree.heading("Phone", text="電話")
    tree.column("Phone", width=80,anchor="center")
    tree.heading("address", text="地址")
    tree.column("address", width=110,anchor="center")

    tree.place(x=10, y=200, width=780, height=390)

    scrollbar = ttk.Scrollbar(new_window_one, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.place(x=790, y=200, height=390)



    new_window_one.mainloop()

def new_window_two():

    def change_window():
        change_window = tk.Toplevel()
        change_window.geometry("250x200+900+300")
        change_window.resizable(False, False)
        change_window.title("更改員工獎金")

        label = tk.Label(change_window, text='更改員工獎金')
        label.config(font=("微軟正黑體", 15))
        label.place(x=125, y=30,anchor="center")

        ID_label = tk.Label(change_window, text="員工編號:")
        ID_label.place(x=50, y=70, anchor="center")

        ID_entry = tk.Entry(change_window)
        ID_entry.place(x=150, y=70, anchor="center")

        pa_label = tk.Label(change_window, text="員工獎金:")
        pa_label.place(x=50, y=100, anchor="center")

        pa_entry = tk.Entry(change_window)
        pa_entry.place(x=150, y=100, anchor="center")

        def change_data():
            ID = ID_entry.get()
            PA = pa_entry.get()

            if(PA != ''):
                PA = int(PA)
                if(0 <= PA <= 50000):
                    if(sql.window_two_change(ID,PA)):
                        error_label.config(text="獎金成功更改")
                    else:
                        error_label.config(text="ID輸入錯誤")
                else:
                    error_label.config(text="獎金輸入錯誤(0 ~ 50000)")
            else:
                error_label.config(text="獎金輸入錯誤(0 ~ 50000)")
        
        change_button = tk.Button(change_window, text="更改資料")
        change_button.config(width=20,height=1)
        change_button.place(x=125, y=140, anchor="center")
        change_button.config(command=change_data)

        error_label = tk.Label(change_window, text="", fg="red")
        error_label.place(x=125, y=170, anchor="center")

    def reset_data():
        reset_window = tk.Toplevel()
        reset_window.geometry("250x130+1000+400")
        reset_window.resizable(False, False)
        reset_window.title("重置員工獎金")

        label = tk.Label(reset_window, text='重置員工獎金')
        label.config(font=("微軟正黑體", 15))
        label.place(x=125, y=40,anchor="center")

        def yes():
            sql.window_two_reset()
            reset_window.destroy()

        yes_button = tk.Button(reset_window, text="確認")
        yes_button.config(width=20,height=1)
        yes_button.place(x=75, y=85, anchor="center", width=90)
        yes_button.config(command=yes)

        def no():
            reset_window.destroy()

        no_button = tk.Button(reset_window, text="取消")
        no_button.config(width=20,height=1)
        no_button.place(x=175, y=85, anchor="center", width=90)
        no_button.config(command=no)

    def update(*all):
        department = selected_option.get()

        results = sql.window_two_update(department)

        for row in tree.get_children():
            tree.delete(row)

        for result in results:
            tree.insert("", "end", values=(result[0], result[2], result[4]))

    new_window_two = tk.Toplevel()
    new_window_two.geometry("500x600+900+300")
    new_window_two.resizable(False,False)
    new_window_two.title("員工獎金修改")

    options = ["資訊部", "人資部", "會計部", "銷售部", "研發部"]
    selected_option = tk.StringVar()
    selected_option.set(options[0])

    selected_option.trace_add('write', update)

    title_label = tk.Label(new_window_two, text="員工業績修改", font=("微軟正黑體", 20))
    title_label.place(x=250, y=35, anchor="center")
    
    option_menu = tk.OptionMenu(new_window_two, selected_option, *options)
    option_menu.place(x=250, y=90, anchor="center")

    update_button = tk.Button(new_window_two, text="更改獎金")
    update_button.config(width=20,height=1)
    update_button.place(x=250, y=130, anchor="center")
    update_button.config(command=change_window)

    re_button = tk.Button(new_window_two, text="所有獎金重置")
    re_button.config(width=20,height=1)
    re_button.place(x=250, y=165, anchor="center")
    re_button.config(command=reset_data)

    columns = ("ID", "Position", "PA")
    tree = ttk.Treeview(new_window_two, columns=columns, show='headings')

    tree.heading("ID", text="員工編號")
    tree.column("ID", width=60,anchor="center")
    tree.heading("Position", text="職位")
    tree.column("Position", width=60,anchor="center")
    tree.heading("PA", text="員工獎金")
    tree.column("PA",width=60,anchor="center")

    tree.place(x=10, y=200, width=480, height=390)

    scrollbar = ttk.Scrollbar(new_window_two, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.place(x=490, y=200, height=390)

    new_window_two.mainloop() 

def new_window_three():

    def PA():
        results = sql.window_three_PA()

        for row in tree.get_children():
            tree.delete(row)

        for result in results:
            tree.insert("", "end", values=(result[0], result[1], result[2]))
    
    def salary():
        results = sql.window_three_salary()

        for row in tree.get_children():
            tree.delete(row)

        for result in results:
            tree.insert("", "end", values=(result[0], result[1], result[2]))

    new_window_three = tk.Toplevel()
    new_window_three.geometry("500x600+900+300")
    new_window_three.resizable(False,False)
    new_window_three.title("員工薪水比較")

    title_label = tk.Label(new_window_three, text="員工薪水比較", font=("微軟正黑體", 20))
    title_label.place(x=250, y=35, anchor="center")

    PA_button = tk.Button(new_window_three, text="按獎金排序")
    PA_button.config(width=20,height=1)
    PA_button.place(x=150, y=80, anchor="center")
    PA_button.config(command=PA)

    salary_button = tk.Button(new_window_three, text="按薪水排序")
    salary_button.config(width=20,height=1)
    salary_button.place(x=350, y=80, anchor="center")
    salary_button.config(command=salary)

    columns = ("ID", "PA", "salary")
    tree = ttk.Treeview(new_window_three, columns=columns, show='headings')

    tree.heading("ID", text="員工編號")
    tree.column("ID", width=60,anchor="center")
    tree.heading("PA", text="員工獎金")
    tree.column("PA", width=60,anchor="center")
    tree.heading("salary", text="薪水+獎金")
    tree.column("salary",width=60,anchor="center")

    tree.place(x=10, y=110, width=480, height=480)

    scrollbar = ttk.Scrollbar(new_window_three, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.place(x=490, y=110, height=480)

    new_window_three.mainloop()

def main_window():

    def stop():
        main_window.destroy()

    main_window = tk.Tk()
    main_window.geometry("300x400+500+300")
    main_window.resizable(False, False)
    main_window.title("主要介面")

    main_title_label = tk.Label(main_window, text="某某某公司資料系統", font=("Arial", 20))
    main_title_label.place(x=150, y=35, anchor="center")
    main_employee_label = tk.Label(main_window, text=f"{name}您好，歡迎使用某某某公司系統", font=("微軟正黑體", 10))
    main_employee_label.place(x=150, y=70, anchor="center")

    button1 = tk.Button(main_window, text="查詢員工資料")
    button1.config(width=20,height=2)
    button1.config(command=new_window_one)
    button1.place(x=150, y=125, anchor="center")

    button2 = tk.Button(main_window, text="員工獎金新增")
    button2.config(width=20,height=2)
    button2.config(command=new_window_two)
    button2.place(x=150, y=200, anchor="center")

    button3 = tk.Button(main_window, text="員工薪水比較")
    button3.config(width=20,height=2)
    button3.config(command=new_window_three)
    button3.place(x=150, y=275, anchor="center")

    button4 = tk.Button(main_window, text="登出")
    button4.config(width=20,height=2)
    button4.config(command=stop)
    button4.place(x=150, y=350, anchor="center")

    main_window.mainloop()

login_window = tk.Tk()
login_window.geometry("400x200+700+400")
login_window.resizable(False, False)
login_window.title("登入畫面")

title_label = tk.Label(login_window, text="登入系統", font=("Arial", 20))
title_label.place(x=200, y=35, anchor="center")

username_label = tk.Label(login_window, text="員工編號:")
username_label.place(x=125, y=85 ,anchor="center")
username_entry = tk.Entry(login_window)
username_entry.place(x=225, y=85 ,anchor="center")

password_label = tk.Label(login_window, text="員工密碼:")
password_label.place(x=125, y=115 ,anchor="center")
password_entry = tk.Entry(login_window,show="*")
password_entry.place(x=225, y=115 ,anchor="center")

login_button = tk.Button(login_window, text="登入", command=check_login)
login_button.place(x=200, y=155, anchor="center")
error_label = tk.Label(login_window, text="", fg="red")
error_label.place(x=200, y=185, anchor="center")

login_window.mainloop()
