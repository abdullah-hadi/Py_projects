email_id=input("enter your email address: ").strip()

username=email_id[:email_id.find("@")]

domain_name=email_id[email_id.find("@")+1:]

print(f"your username is : {username}\nyour domain name is: {domain_name}\n")