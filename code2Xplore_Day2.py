student_id = input("ID: ")
email_id = input("Email: ")
password = input("Password: ")
referral_code = input("Referral: ")

if student_id[:4]=="CSE-" and "0"<=student_id[4]<="9" and "0"<=student_id[5]<="9" and "0"<= student_id[6]<="9" and \
        "@" in email_id and email_id[0]!="@" and email_id[len(email_id )-1]!="@" and email_id[len(email_id)-4:]==".edu" and \
   len(password)>=8 and "A"<= password[0]<="Z" and ("0"<=password[0]<="9" or "0"<=password[1]<="9" or "0"<=password[2]<="9" or \
     "0"<=password[3]<="9" or "0"<=password[4]<="9" or "0"<=password[5]<="9" or "0"<=password[6]<="9" or "0"<=password[7]<="9") and \
        referral_code[:3]=="REF" and "0"<=referral_code[3]<="9" and "0"<=referral_code[4]<="9" and referral_code[len(referral_code)-1]=="@":
    print('APPROVED')
else:
    print("REJECTED")
