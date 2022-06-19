# Plan : Have 3 things, Send Email, do some job (toll booth operator), password manager, and maybe a multi-clipboard,or a generate signature thing.



task = input("What automation would you like to do? Type '1' for send email, '2' for automating toll booth, '3' for password manager, '4' generate signature and '5' for a multi-clipboard? ")

if task == "1":
    from sendemails import *
