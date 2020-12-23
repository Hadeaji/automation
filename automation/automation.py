import re

def read_file():
    with open('./assets/potential-contacts.txt','r') as fil:
        all_lines = fil.read()
    return all_lines


def get_emails():
    text = read_file()
    email_validation = r'([\w\.-]+)@([\w\.-]+)'
    all_valid_emails = re.findall(email_validation,text)
    for i in range(len(all_valid_emails)):
        all_valid_emails[i]= '@'.join(all_valid_emails[i])

    all_valid_emails.sort()    

    with open('./assets/emails.txt','w') as fil:
        # remove duplicate
        no_dupl =[]
        for i in all_valid_emails:
            if i not in no_dupl:
                fil.write(str(i)+'\n')
            no_dupl.append(i)

def get_phones():
    text = read_file()
    phone_validation = r'([+]?[(]?[0-9]{1,4}[)]?)([-|.]?[0-9]{1,4})([-|.]?[0-9]{1,4})([-|.]?([0-9]{1,4})?)([x]?([0-9]{1,7})?)'
    all_valid_phones = re.findall(phone_validation,text)
    for i in range(len(all_valid_phones)):
        all_valid_phones[i]= list(all_valid_phones[i])
        all_valid_phones[i][4]=''
        all_valid_phones[i][6]=''

        all_valid_phones[i]= ''.join(all_valid_phones[i])


    print(all_valid_phones)
    all_valid_phones.sort()    

    with open('./assets/phone_numbers.txt','w') as fil:
        no_dupl =[]
        for i in all_valid_phones:
            if i not in no_dupl:
                if i[0]== '+' or i[0] == '(':
                    fil.write(str(i)+'\n')
                elif i[0]=='0' and i[1]=='0' and i[2]=='1':
                    fil.write(str(i)+'\n')
                else:
                    fil.write('206-'+str(i)+'\n')
            no_dupl.append(i)

get_emails()
get_phones()
