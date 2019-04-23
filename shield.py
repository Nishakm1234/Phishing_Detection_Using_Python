#!/usr/bin/env python3
import webbrowser
import tempfile
import urllib.request
import urllib.parse
import re
from tkinter import Tk, Text, TOP, Label, Menu, Entry, Button, RAISED, END
from tkinter import *
from tkinter.colorchooser import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import ssl, socket
import csv
# Run main application 
class Browser:
    """This creates a relay that allows a user to directly view data sent from a web server."""
    def __init__(self, master):
        """Sets up a browsing session."""
        # Explicit global declarations are used to allow certain variable to be used in all methods.
        global e1,e2,e3,e4,t1
        # Here we create some temporary settings that allow us to create a client that ignores proxy settings.
        self.proxy_handler = urllib.request.ProxyHandler(proxies=None)
        self.opener = urllib.request.build_opener(self.proxy_handler)
        # This sets up components for the GUI.
        menu=Menu(root)
        menu.configure(background='white')
        root.config(menu=menu)
        subMenu=Menu(menu)
        menu.add_cascade(label="Apps",menu=subMenu)
        subMenu.add_command(label="Gmail", command=lambda aurl=url1:OpenUrl(aurl))
        subMenu.add_command(label="Y! Mail", command=lambda aurl=url2:OpenUrl(aurl))
        subMenu.add_command(label="Youtube", command=lambda aurl=url3:OpenUrl(aurl))
        subMenu.add_command(label="Facebook", command=lambda aurl=url4:OpenUrl(aurl))
        subMenu.add_command(label="Github", command=lambda aurl=url5:OpenUrl(aurl))
        subMenu.add_command(label="LinkedIn", command=lambda aurl=url6:OpenUrl(aurl))
        subMenu.add_separator()
        editMenu=Menu(menu)
        menu.add_cascade(label="Settings",menu=editMenu)
        editMenu.add_command(label="Themes and Colors", command=getColor)
        editMenu.add_command(label="History")
        editMenu.add_command(label="Connect account...")
        editMenu.add_command(label="Exit", command=root.quit)
        editMenu=Menu(menu)
        menu.add_cascade(label="Bookmarks",menu=editMenu)
        editMenu.add_command(label="View")
        editMenu.add_command(label="Add bookmark")
        editMenu=Menu(menu)
        menu.add_cascade(label="Tools",menu=editMenu)
        editMenu.add_command(label="Inspect Element")
        editMenu.add_command(label="Manage Extensions")
        editMenu.add_command(label="Developer Tools")
        editMenu=Menu(menu)
        menu.add_cascade(label="Downloads",menu=editMenu)
        editMenu.add_command(label="Open Downloads Folder", command=callback)
        
        """Label widget"""
        Label(root, text='Enter the search item',bg="lightblue",font=("Times New Roman",18)).pack(side=TOP)
        """Entry widget"""
        e1 = Entry(root,width=80)
        e1.pack(side=TOP)
        """Button widget"""
        Button(root, text='Browse', width=10, relief=RAISED,bg="white", font=("Times New Roman",14), command=self.ButtonClick).pack(side=TOP)
        
        """Label widget"""
        Label(root, text='To display URLs of legitimate websites',bg="lightblue",font=("Times New Roman",18)).pack(side=TOP)
        """Entry widget"""
        e3 = Entry(root,width=80)
        e3.pack(side=TOP)
        """Button widget"""
        Button(root, text='Search', width=10, relief=RAISED,bg="white", font=("Times New Roman",14),command=self.buttonClick).pack(side=TOP)
        """Text widget"""
        t1 = Text(root, height=5, width=80)
        t1.pack()
        """Button widget"""
        Button(root, text='Clear', width=10, relief=RAISED,bg="white", font=("Times New Roman",14),command=lambda: t1.delete(1.0,END)).pack(side=TOP)
        
        """Label widget"""
        Label(root, text='Enter URL to be checked',bg="lightblue",font=("Times New Roman",18)).pack(side=TOP)
        """Entry widget"""
        e2 = Entry(root,width=80)
        e2.pack(side=TOP)
        """Button widget"""
        Button(root, text='Check', width=10, relief=RAISED,bg="white", font=("Times New Roman",14), command=self.buttonOnClick).pack(side=TOP)
       
        """Label widget"""
        Label(root, text='To fetch Certificate Details',bg="lightblue",font=("Times New Roman",18)).pack(side=TOP)
        """Entry widget"""
        e4 = Entry(root,width=80)
        e4.pack(side=TOP)
        """Button widget"""
        Button(root, text='Details', width=10, relief=RAISED,bg="white", font=("Times New Roman",14), command=self.Certificate_details).pack(side=TOP)
     
    """This function is to display the top 10 legitimate URLs of the given item in the entry field"""    
    def buttonClick(self):
        try: 
            from googlesearch import search 
        except ImportError:  
            print("No module named 'google' found")
        
        """Iterate 10 times to fetch the top 10 legitimate URLs"""
        for j in search(e3.get(), tld="co.in", num=10, stop=10, pause=2): 
            """To display the results to the text widget"""
            t1.insert(END,j)
            t1.insert(END,'\n')
        """To delete or clear the entry item"""
        e3.delete(0, END)
        e3.insert(0, "")
   
    """This function is to browse the given search item"""   
    def ButtonClick(self):
        """It will open webbrowser with the given url pattern"""
        webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % e1.get())
        """To delete or clear the entry item"""
        e1.delete(0, END)
        e1.insert(0, "") 
    
    """This function is to fetch the certificate details"""    
    def Certificate_details(self):
        """Fetch the hostname"""
        hostname = e4.get()
        ctx = ssl.create_default_context()
        s = ctx.wrap_socket(socket.socket(), server_hostname=hostname)
        """To check if the connection is established correctly"""
        try:
            s.connect((hostname, 443))
            cert = s.getpeercert()
            subject = dict(x[0] for x in cert['subject'])
            issued_to = subject['commonName']
            issuer = dict(x[0] for x in cert['issuer'])
            issued_by = issuer['commonName']
            """To display the message box with the fetched certificate details"""
            messagebox.showinfo("Certificate Details","Issued To:%s\nIssued By:%s"%(issued_to,issued_by))
        except Exception as e:
            #To display the exception message
            messagebox.showinfo("Information","Give a valid hostname \n or \n Could not fetch the certificate details")
        """To delete or clear the entry item"""
        e4.delete(0, END)
        e4.insert(0, "")
        
    """This function is to check the url features to predict whether it is legitimate,phishing or suspicious"""     
    def buttonOnClick(self):
        u1=valid_url(e2.get())
        a=long_url(e2.get())
        b=have_at_symbol(e2.get())
        c=redirection(e2.get())
        d=prefix_suffix_seperation(e2.get())
        e=sub_domains(e2.get())
        f=slash_count(e2.get())
        g=have_mod_symbol(e2.get())
        i=have_dollar_symbol(e2.get())
        j=have_anchor_symbol(e2.get())
        k=have_question_symbol(e2.get())
        m=have_underscore_symbol(e2.get())
        n=have_equal_symbol(e2.get())
        o=have_hash_symbol(e2.get())
        p=have_space_symbol(e2.get())
        q=have_asp_extension(e2.get())
        r=have_doc_extension(e2.get())
        s=have_htm_extension(e2.get())
        t=have_html_extension(e2.get())
        u=have_mp3_extension(e2.get())
        v=have_mpeg_extension(e2.get())
        w=have_pdf_extension(e2.get())
        x=have_php_extension(e2.get())
        y=have_txt_extension(e2.get())
        z=have_ampersand_symbol(e2.get())
        a1=have_xyz_extension(e2.get())
        bl1=blacklist_function(e2.get())
        if u1==4:
            #Error message 
            messagebox.showerror("Error", "Enter a valid url which begins from http:// or https://")
            e2.delete(0, END)
            e2.insert(0, "")
        elif bl1==0:
            """To check if the phished url is present in the dataset and display a warning if present"""
            messagebox.showwarning("Warning","This is a phishing website.")
                
            #To clear the entry field    
            e2.delete(0, END)
            e2.insert(0, "")
        elif a==1 or b==1 or c==1 or d==1 or e==1 or f==1 or g==1 or i==1 or j==1 or k==1 or m==1 or n==1 or o==1 or p==1 or q==1 or r==1 or s==1 or t==1 or u==1 or v==1 or w==1 or x==1 or y==1 or z==1 or a1==1:
            """To check if the phished url is present in the dataset. If it is not present it is added to the dataset"""
            if(bl1==1):
                with open('train1.csv', 'a') as newFile:
                    newFileWriter = csv.writer(newFile)
                    newFileWriter.writerow([e2.get()])
                    #Warning is displayed
                    messagebox.showwarning("Warning","This is a phishing website.")
           
            #To clear the entry field    
            e2.delete(0, END)
            e2.insert(0, "")
        
        elif a==2 or d==2 or f==2:
            """To check for a suspicious website"""
            #Ok or cancel message
            mbox=messagebox.askokcancel("Question","This is a suspicious website.\n Do you want to continue?")
            if mbox ==1:
                #Redirect to the requested URL
                webbrowser.open_new_tab('%s' % e2.get())
            e2.delete(0, END)
            e2.insert(0, "")
            
        elif a==0 or b==0 or c==0 or d==0 or e==0 or f==0 or g==0 or i==0 or j==0 or k==0 or m==0 or n==0 or o==0 or p==0 or q==0 or r==0 or s==0 or t==0 or u==0 or v==0 or w==0 or x==0 or y==0 or z==0 or a1==0:
            """To check for a legitimate website"""
            #Display information message
            messagebox.showinfo("Information","This is a legitimate website \n It is safe to use")
            webbrowser.open_new_tab('%s' % e2.get())
            """To delete or clear the entry item"""
            e2.delete(0, END)
            e2.insert(0, "")
    
# Creates a Tk() window that is always in front of all other windows.
root = Tk()
#The total size of the window
root.geometry("1366x768+0+0")
C = Canvas(root, bg="blue", height=250, width=300)
#To set the background image
filename = PhotoImage(file ="image.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
#The title of the application window
root.wm_title("Web Browser ")
url1='http://www.gmail.com'
url2='http://www.yahoomail.com'
url3='http://www.youtube.com'
url4='http://www.facebook.com'
url5='http://www.github.com'
url6='http://www.linkedin.com'
url7='http://www.firefox.com'
url8='http://www.bing.com'
url9='http://www.yahoo.com'
url10='http://www.google.com'
"""scrollbar = Scrollbar(root)
scrollbar.configure(background='grey')
scrollbar.pack(side=RIGHT, fill=Y)"""

def OpenUrl(url):
    webbrowser.open_new(url)

from tkinter.colorchooser import *
def getColor():
    color = askcolor()

def callback():
    name= askopenfilename() 
    
def valid_url(l):
    l=str(l)
    if "http" in str(l) or "https" in str(l):
        return 3
    else: 
        return 4
def long_url(l):
    """This function is defined in order to differntiate website based on the length of the URL"""
    l= str(l)
    if len(l) < 53:
        return 0
    elif len(l)>=53 and len(l)<75:
        return 2
    else:
        return 1

def have_at_symbol(l):
    """This function is used to check whether the URL contains @ symbol or not"""
    if "@" in str(l):
        return 1
    else:
        return 0

def redirection(l):
    """If the url has symbol(//) after protocol then such URL is to be classified as phishing """
    l= str(l)
    if l.count('//')>1:
        return 1
    else:
        return 0

def prefix_suffix_seperation(l):
    """seprate prefix and suffix"""
    l= str(l)
    if l.count('-')<=3:
        return 0
    elif l.count('-')>3 and l.count('-')<=5:
        return 2
    else:
        return 1

def sub_domains(l):
    """check the subdomains"""
    l= str(l)
    if l.count('.') <= 3:
        return 0
    else:
        return 1
    
def slash_count(l):
    """Check the slash count"""
    l= str(l)
    if l.count('/')<5:
        return 0
    elif l.count('/')>=5 and l.count('/')<=7:
        return 2
    else:
        return 1
    
def have_mod_symbol(l):
    """Check if modulus is present"""
    if "%" in str(l):
        return 1
    else:
        return 0
    
def have_dollar_symbol(l):
    """Check dollar is present"""
    if "$" in str(l):
        return 1
    else:
        return 0
    
def have_anchor_symbol(l):
    """Check if anchor symbol is present"""
    if "<" in str(l) or ">" in str(l):
        return 1
    else:
        return 0
def have_question_symbol(l):
    """Check if question mark is present"""
    if "?" in str(l):
        return 1
    else:
        return 0
def have_underscore_symbol(l):
    """Check if underscore is present"""
    if "_" in str(l):
        return 1
    else:
        return 0

def have_equal_symbol(l):
    """Check if equal symbol is present"""
    if "=" in str(l):
        return 1
    else:
        return 0
    
def have_hash_symbol(l):
    """Check if hash symbol is present"""
    if "#" in str(l):
        return 1
    else:
        return 0

def have_space_symbol(l):
    """Check if space is present"""
    if " " in str(l):
        return 1
    else:
        return 0
    
def have_asp_extension(l):
    """Check if .asp extension is present"""
    if ".asp" in str(l):
        return 1
    else:
        return 0

def have_doc_extension(l):
    """Check if .doc extension is present"""
    if ".doc" in str(l):
        return 1
    else:
        return 0
    
def have_htm_extension(l):
    """Check if .htm extension is present"""
    if ".htm" in str(l):
        return 1
    else:
        return 0
    
def have_html_extension(l):
    """Check if .html extension is present"""
    if ".html" in str(l):
        return 1
    else:
        return 0
    
def have_mp3_extension(l):
    """Check if .mp3 extension is present"""
    if ".mp3" in str(l):
        return 1
    else:
        return 0
    
def have_mpeg_extension(l):
    """Check if .mpeg extension is present"""
    if ".mpeg" in str(l):
        return 1
    else:
        return 0
    
def have_pdf_extension(l):
    """Check if .pdf extension is present"""
    if ".pdf" in str(l):
        return 1
    else:
        return 0
    
def have_php_extension(l):
    """Check if .php extension is present"""
    if ".php" in str(l):
        return 1
    else:
        return 0
    
def have_txt_extension(l):
    """Check if .txt extension is present"""
    if ".txt" in str(l):
        return 1
    else:
        return 0
  
def have_ampersand_symbol(l):
    """Check if ampersand symbol is present"""
    if "&" in str(l):
        return 1
    else:
        return 0
    
def have_xyz_extension(l):
    """Check if .xyz extension is present"""
    if ".xyz" in str(l):
        return 1
    else:
        return 0
def blacklist_function(l):
    with open('train1.csv', mode='r') as infile:
        reader = csv.reader(infile)
        for row in reader:
            if row==[l]:
                return 0
    return 1
   
Label(root, text='Direct Links',bg="lightblue",font=("Times New Roman",18)).pack(side=TOP)
frame=Frame(root)
frame.pack(side=TOP)

b1=ttk.Button(frame, command=lambda aurl=url10:OpenUrl(aurl))
b1.pack(side=LEFT)
m1=PhotoImage(file="g.png")
b1.config(image=m1)
tm1=m1.subsample(7,7)
b1.config(image=tm1)
b2=ttk.Button(frame, command=lambda aurl=url8:OpenUrl(aurl))
b2.pack(side=LEFT)
m2=PhotoImage(file="bing.png")
b2.config(image=m2)
tm2=m2.subsample(6,6)
b2.config(image=tm2)
b3=ttk.Button(frame, command=lambda aurl=url9:OpenUrl(aurl))
b3.pack(side=LEFT)
m3=PhotoImage(file="yahoo.png")
b3.config(image=m3)
tm3=m3.subsample(6,6)
b3.config(image=tm3)
# Starts the program by initializing the Browser object and main-looping the Tk() window.
info_from_server = Browser(root)
root.mainloop()


