import csv

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

def validateURL(url):
        status=''
        a=long_url(url)
        b=have_at_symbol(url)
        c=redirection(url)
        d=prefix_suffix_seperation(url)
        e=sub_domains(url)
        f=slash_count(url)
        g=have_mod_symbol(url)
        i=have_dollar_symbol(url)
        j=have_anchor_symbol(url)
        k=have_question_symbol(url)
        m=have_underscore_symbol(url)
        n=have_equal_symbol(url)
        o=have_hash_symbol(url)
        p=have_space_symbol(url)
        q=have_asp_extension(url)
        r=have_doc_extension(url)
        s=have_htm_extension(url)
        t=have_html_extension(url)
        u=have_mp3_extension(url)
        v=have_mpeg_extension(url)
        w=have_pdf_extension(url)
        x=have_php_extension(url)
        y=have_txt_extension(url)
        z=have_ampersand_symbol(url)
        a1=have_xyz_extension(url)
        bl1=blacklist_function(url)
        
        if bl1==0:
            """To check if the phished url is present in the dataset and display a warning if present"""
            status='Already BlackListed'
        elif a==1 or b==1 or c==1 or d==1 or e==1 or f==1 or g==1 or i==1 or j==1 or k==1 or m==1 or n==1 or o==1 or p==1 or q==1 or r==1 or s==1 or t==1 or u==1 or v==1 or w==1 or x==1 or y==1 or z==1 or a1==1:
            """To check if the phished url is present in the dataset. If it is not present it is added to the dataset"""
            if(bl1==1):
                with open('train1.csv', 'a') as newFile:
                    newFileWriter = csv.writer(newFile)
                    newFileWriter.writerow([url])
                    
            status='Phishing detected,Added to Blacklist'
        
        elif a==2 or d==2 or f==2:
            """To check for a suspicious website"""
            status='suspicious'
            
        elif a==0 or b==0 or c==0 or d==0 or e==0 or f==0 or g==0 or i==0 or j==0 or k==0 or m==0 or n==0 or o==0 or p==0 or q==0 or r==0 or s==0 or t==0 or u==0 or v==0 or w==0 or x==0 or y==0 or z==0 or a1==0:
            """To check for a legitimate website"""
            status='No threat detected'
        return status