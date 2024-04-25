import customtkinter
import tkinter
import mysql.connector
from email_validator import validate_email, EmailNotValidError

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.user="tando"
        self.query="select title,movie_id from movie order by avg_rating desc;"
        self.login_window()
 
        
    def sign_up(self):
        
        def sign_up():
           mydb=mysql.connector.connect(host="localhost",user="root",password="stud",database="movies")
           mycursor = mydb.cursor()
           mycursor.execute("select * from user;")
           res=mycursor.fetchall()
           flag=0
           for i in res:
                if i[0]==entry_1.get():
                    label = customtkinter.CTkLabel(master=frame, text = "", font= ("Helvetica",13))
                    label.place(relx=0.20, rely=0.32, anchor=tkinter.CENTER)
                    print("Login Failed")                        
                    entry_1.configure(fg_color=("#E34234","#E34234"))
                    entry_2.configure(fg_color=("#E34234","#E34234"))
                    label.configure(text="User Already Exists!")
                    flag=1
                    break  
                if flag==0 and entry_1.get()=="":
                    try :
                        emailinfo = validate_email(entry_1.get(), check_deliverability=False)
                        email=emailinfo.normalized_email
                    except EmailNotValidError as e:
                        entry_1.configure(fg_color=("#E34234","#E34234"))
                        entry_2.configure(fg_color=("#E34234","#E34234"))
                        label.configure(text="Username not a valid email!")
                if flag==0 and entry_1.get()!="" and entry_2.get()!="":
                    mycursor.execute("insert into user values('"+entry_1.get()+"','"+entry_2.get()+"');")
                    mydb.commit()
                    print("User Added")
                    root_login.destroy()
                    self.login_window()
        #Define the login page window          
        root_login = customtkinter.CTk() 
        root_login.geometry(f"{500}x{500}")
        root_login.title("SIGN UP PAGE")

        #Add some widgets for login page
        frame = customtkinter.CTkFrame(master=root_login,width=450, height=450, corner_radius=10)
        frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        entry_1 = customtkinter.CTkEntry(master=frame, corner_radius=20, width=400, placeholder_text="Username")
        entry_1.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

        entry_2 = customtkinter.CTkEntry(master=frame, corner_radius=20, width=400, show="*", placeholder_text="Password")
        entry_2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        button_signup = customtkinter.CTkButton(master=frame, text="SIGN UP", corner_radius=6, command=sign_up, width=400)
        button_signup.place(relx=0.5,rely=0.6,anchor = tkinter.CENTER)

        
        

        root_login.mainloop()

    
    def login_window(self):
        def login_event():
           mydb=mysql.connector.connect(host="localhost",user="root",password="stud",database="movies")
           mycursor = mydb.cursor()
           mycursor.execute("select * from user;")
           res=mycursor.fetchall()
           flag = 0
           for i in res:
                if i[0]==entry_1.get() and i[1]==entry_2.get():
                    self.user=i[0]
                    root_login.destroy()
                    self.home()

                    flag = 1
                    break
            
           if flag == 0:
                label = customtkinter.CTkLabel(master=frame, text = "", font= ("Helvetica",13))
                label.place(relx=0.30, rely=0.32, anchor=tkinter.CENTER)
                print("Login Failed")                        
                entry_1.configure(fg_color=("#E34234","#E34234"))
                entry_2.configure(fg_color=("#E34234","#E34234"))
                label.configure(text="Wrong Password/User Doesn't Exist!")
            
        
        
        def sign_up():
            root_login.destroy()
            self.sign_up()
            
        #Define the login page window          
        root_login = customtkinter.CTk() 
        root_login.geometry(f"{500}x{500}")
        root_login.title("LOGIN PAGE")

        #Add some widgets for login page
        frame = customtkinter.CTkFrame(master=root_login,width=450, height=450, corner_radius=10)
        frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        entry_1 = customtkinter.CTkEntry(master=frame, corner_radius=20, width=400, placeholder_text="Username")
        entry_1.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

        entry_2 = customtkinter.CTkEntry(master=frame, corner_radius=20, width=400, show="*", placeholder_text="Password")
        entry_2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        button_login = customtkinter.CTkButton(master=frame, text="LOGIN", corner_radius=6, command=login_event, width=400)
        button_signup = customtkinter.CTkButton(master=frame, text="NEW USER", corner_radius=6, command=sign_up, width=400)
        button_login.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
        button_signup.place(relx=0.5,rely=0.7,anchor = tkinter.CENTER)

        font = customtkinter.CTkFont(family="Helvetica",size = 24, weight = "bold",slant= 'roman' )
        Title = customtkinter.CTkLabel(master=frame, text = "MOVIE RECOMMENDER SYSTEM", font= font)
        Title.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
        
        

        root_login.mainloop()
        
    def home(self):
        def search_movie(search):
            search=search.get()
            self.query="select title,movie_id from movie where title like \'%"+search+"%\' order by avg_rating desc;"
            print(self.query)
            root_home.destroy()
            self.home()
        def movie_event(i):
            root_home.destroy()
            self.movie_event(i)
        mydb=mysql.connector.connect(host="localhost",user="root",password="stud",database="movies")
        mycursor = mydb.cursor()
        mycursor.execute(self.query)
        res=mycursor.fetchall()
        count=res.__len__()
        movie_buttons = {}
        root_home = customtkinter.CTk()
        root_home.geometry(f"{1280}x{720}")
        root_home.title("MOVIE RECOMMENDER SYSTEM")
        frame=customtkinter.CTkScrollableFrame(master=root_home,width=1260, height=700, corner_radius=10)
        frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        search=customtkinter.CTkEntry(master=frame, corner_radius=20, width=400, placeholder_text="Search")
        search.pack(pady=10)
        print(search)
        customtkinter.CTkButton(master=frame,text="Search",command=lambda:(search_movie(search))).pack(pady=10)
        for i in range(count):
            movie_buttons[res[i][1]] = customtkinter.CTkButton(master=frame, text=res[i][0], corner_radius=6, width=400,command=lambda i = res[i][1]:movie_event(i))
            movie_buttons[res[i][1]].pack(pady = 10)
        root_home.mainloop()
    def movie_event(self,movie_id):
        def rate_movie():
            rate=slider.get()
            try:
                mycursor.execute("insert into rating values('"+self.user+"',"+str(movie_id)+","+str(rate)+");")
                mydb.commit()
            except:
                mycursor.execute("update rating set rating="+str(rate)+" where username='"+self.user+"' and movie_id="+str(movie_id)+";")
                mydb.commit()
        def home():
            root_movie.destroy()
            self.home()
        mydb=mysql.connector.connect(host="localhost",user="root",password="stud",database="movies")
        mycursor = mydb.cursor()
        root_movie = customtkinter.CTk()
        root_movie.geometry(f"{1280}x{720}")
        mycursor.execute("select title from movie where movie_id="+str(movie_id)+";")
        res=mycursor.fetchall()
        root_movie.title(res[0][0])
        frame=customtkinter.CTkScrollableFrame(master=root_movie,width=1260, height=700, corner_radius=10)
        frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        font = customtkinter.CTkFont(family="Helvetica",size = 24, weight = "bold",slant= 'roman' )
        Title = customtkinter.CTkLabel(master=frame, text = res[0][0], font= font)
        Title.pack(pady=10)
        mycursor.execute("select * from movie where movie_id="+str(movie_id)+";")
        res=mycursor.fetchall()
        readingfont = customtkinter.CTkFont(family="Helvetica",size = 16,slant= 'roman' )
        releasedate=customtkinter.CTkLabel(master=frame,text="Release Date: "+str(res[0][1]),font=readingfont)
        releasedate.pack(padx=10)
        mycursor.execute("select income from monthly_income where movie_id="+str(movie_id)+";")
        income=mycursor.fetchall()
        customtkinter.CTkLabel(master=frame,text="Income: "+str(income[0][0]),font=readingfont).pack(padx=10)
        mycursor.execute("select name from awards natural join movie where movie_id="+str(movie_id)+";")
        awards=mycursor.fetchall()
        listToStr = ','.join([str(elem[0]) for elem in awards])
        awards=customtkinter.CTkLabel(master=frame,text="Awards: "+listToStr,font=readingfont).pack(padx=10)
        rating=customtkinter.CTkLabel(master=frame,text="Rating: "+str(res[0][3]),font=readingfont)
        rating.pack(padx=10)
        mycursor.execute("select name from genre where movie_id="+str(movie_id)+";")
        genre=mycursor.fetchall()
        listToStr = ','.join([str(elem[0]) for elem in genre])
        customtkinter.CTkLabel(master=frame,text="Genres:"+listToStr,font=readingfont).pack(padx=10)
        mycursor.execute("select name,role from person natural join actor where movie_id="+str(movie_id)+";")
        actor=mycursor.fetchall()
        listToStr = ','.join([str(elem[0])+"("+str(elem[1])+")" for elem in actor])
        customtkinter.CTkLabel(master=frame,text="Actors:"+listToStr,font=readingfont).pack(padx=10)
        mycursor.execute("select name from person natural join director where movie_id="+str(movie_id)+";")
        director=mycursor.fetchall()
        listToStr = ','.join([str(elem[0]) for elem in director])
        customtkinter.CTkLabel(master=frame,text="Director:"+listToStr,font=readingfont).pack(padx=10)
        mycursor.execute("select name from person natural join producer where movie_id="+str(movie_id)+";")
        producer=mycursor.fetchall()
        listToStr = ','.join([str(elem[0]) for elem in producer])
        customtkinter.CTkLabel(master=frame,text="Producer:"+listToStr,font=readingfont).pack(padx=10)
        mycursor.execute("select description from movie_description where movie_id="+str(movie_id)+";")
        description=mycursor.fetchall()
        customtkinter.CTkLabel(master=frame,text=description[0][0],font=readingfont).pack(padx=10)
        slider=customtkinter.CTkSlider(master=frame,width=160,height=16,border_width=5.5,number_of_steps=5,from_=1,to=5)
        slider.pack(pady=10)
        customtkinter.CTkButton(master=frame,text="Rate",command=rate_movie).pack(pady=10)
        customtkinter.CTkButton(master=frame,text="Back",command=home).pack(pady=10)
        root_movie.mainloop()

app = App()
app.mainloop()