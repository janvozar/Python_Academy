# Task 48: Collecting emails

def collect_emails(text):

    words = text.split()
    emails = []

    for word in words:
        if '@' in word:
            email = word.strip(".,:!?")
            emails.append(email)
    print("emails:", emails)

    return emails

#============================================================

def select_num_emails(emails):

    num_mails = []

    for email in emails:
        if contains_number(email):
            num_mails.append(email)

    return num_mails

#============================================================

def contains_number(_string):

    for num in range(10):
        if str(num) in _string:
            return True
    return False

#============================================================

def extract_domains(emails):

    domains = []
    for email in emails:
        domains.append(email.split('@')[-1])
    return domains

#============================================================

def extract_domains(emails):

    domains = []
    for email in emails:
        domains.append(email.split('@')[-1])
    return domains

#============================================================

def main():

    result = {'emails_with_nums': None,
              'domains': None}

    emails = collect_emails(my_str)

    result['emails_with_nums'] = select_num_emails(emails)
    result['domains'] = extract_domains(emails)

    print(result)
    return result

#============================================================




