import imaplib
import email

def get_blog_emails():
	try:
		gmail = imaplib.IMAP4_SSL('imap.gmail.com')
		gmail.login('gnereicusername1@gmail.com', 'password')
		gmail.list()
		gmail.select('blog_journal')
		
		type, data = gmail.search(None, 'ALL')
		
		for x in range(len(data[0].split())):
			latest = data[0].split()[x]
			result, email_data = gmail.uid('fetch', latest, '(RFC822)')
			raw_email = email_data[0][1]
			raw_email = raw_email.decode('utf-8')
			msg = email.message_from_string(raw_email)
			date = msg['Date']
			
			## Section to compare date to most recent date, only proceed if more recent
			## if date <= last_date
			##     break
			
            if msg.is_multipart():
                body = msg.get_payload(0).get_payload()
            else:
                body = msg.get_payload()
			
            ## Write to md file
            ## date
            ## -----
            ## body
            
            
