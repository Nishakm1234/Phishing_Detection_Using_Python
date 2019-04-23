#following class is used to extract the information from email and get the rquired data
import re
import datetime
import email
import imaplib

#following method is used to extract the information from mail service
def extractFromEmail(EMAIL_ACCOUNT,PASSWORD):

    #EMAIL_ACCOUNT = "networkteam2019@gmail.com"
    #PASSWORD = "cdnn@1997"
    Files=[]
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(EMAIL_ACCOUNT, PASSWORD)
    mail.list()
    mail.select('inbox')
    result, data = mail.uid('search', None, "UNSEEN") # (ALL/UNSEEN)
    i = len(data[0].split())

    for x in range(i):
        latest_email_uid = data[0].split()[x]
        result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        # result, email_data = conn.store(num,'-FLAGS','\\Seen') 
        # this might work to set flag to seen, if it doesn't already
        raw_email = email_data[0][1]
        raw_email_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email_string)
        
        # Header Details
        date_tuple = email.utils.parsedate_tz(email_message['Date'])
        if date_tuple:
            local_date = datetime.datetime.fromtimestamp(email.utils.mktime_tz(date_tuple))
            local_message_date = "%s" %(str(local_date.strftime("%a, %d %b %Y %H:%M:%S")))
            email_from = str(email.header.make_header(email.header.decode_header(email_message['From'])))
            email_to = str(email.header.make_header(email.header.decode_header(email_message['To'])))
            subject = str(email.header.make_header(email.header.decode_header(email_message['Subject'])))
            
            # Body details
            for part in email_message.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True)
                    file_name = "Data/email_" + str(x) + ".txt"
                    Files.append(file_name)
                    output_file = open(file_name, 'w')
                    output_file.write("From: %s\nTo: %s\nDate: %s\nSubject: %s\n\nBody: \n\n%s" %(email_from, email_to,local_message_date, subject, body.decode('utf-8')))
                    output_file.close()
                else:
                    continue
    return Files

#the following method is used to extrct the required information from text file storing the extracted email
def extract_URL_From_Sub(Files):
    url_pattern = re.compile('((http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?)')
    From_pattern = re.compile('^(From:\s)(.*)')
    Sub_pattern = re.compile('^(Subject:\s)(.*)')
    for inputfile in Files:
        with open(inputfile) as fh_in:
            for line in fh_in:
                match_list = url_pattern.findall(line)
                From = From_pattern.findall(line)
                Subj= Sub_pattern.findall(line)
                if match_list:
                    with open("Data/mailout.txt", "a+") as fh_out:
                        fh_out.write(match_list[0][0]+'\n')
                        fh_out.close()
                if From:
                    with open("Data/From.txt", "a+") as fh_out:
                        fh_out.write(From[0][1]+'\n')    
                        fh_out.close()
                if Subj:
                    with open("Data/Sub.txt", "a+") as fh_out:
                        fh_out.write(Subj[0][1]+'\n')    
                        fh_out.close()