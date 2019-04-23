import extractInfo
import detectPhishing
import csv
import tkinter as tk

def handleClick(username,password):
    Status=[]
    #Files=extractInfo.extractFromEmail('networkteam2019@gmail.com','cdnn@1997')
    Files=extractInfo.extractFromEmail(username,password)
    extractInfo.extract_URL_From_Sub(Files)
    if Files:
        with open('Data/mailout.txt', mode='r') as infile:
            reader = csv.reader(infile)
            for row in reader:
                print(row)
                with open("Data/Status.txt", "a+") as fh_out:
                        res=detectPhishing.validateURL(row)
                        Status.append(res)
                        fh_out.write(res+'\n')    
                        fh_out.close()


window=tk.Tk()

l1=tk.Label(window,text='Email-Id:')
l2=tk.Label(window,text='Password')

t1=tk.Entry(window,textvariable=tk.StringVar())
t2=tk.Entry(window,show="*",textvariable=tk.StringVar())
print('$$$$$$$$$$$$$$$$$$$$$$$$$$'+t1.get())
b1=tk.Button(window,text="Check",command=lambda: handleClick(t1.get(),t2.get()))

l1.grid(row=0,column=0)
t1.grid(row=0,column=1)
l2.grid(row=1,column=0)
t2.grid(row=1,column=1)
b1.grid(row=2,column=1)

window.mainloop()