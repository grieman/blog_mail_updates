import imaplib
import email

def get_blog_emails():
	try:
		gmail = imaplib.IMAP4_SSL('imap.gmail.com')
		gmail.login('username at gmail.com', 'password')
		gmail.list()
		gmail.select('blog_journal')
		
		type, data = mail.search(None, 'ALL')
		
		for x in range(len(data[0].split())):
			latest = data[0].split()[x]
			result, email_data = gmail.uid('fetch', latest, '(RFC822)')
			raw_email = email_data[0][1]
			raw_email = raw_email.decode('utf-8')