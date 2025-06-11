#Password Validation
 
def validate_password(password):
    sc = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-' 
          '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', "\\", "]",'^', 
          '_',"`", '{', '|', '}', '~']
    counter = 0
    count = 0
    if len(password) > 20:
        raise IndexError (f"La password non dovrebbe superare i 20 caratteri. {len(password)}")
    for i in password:
        if i.isupper():
            count += 1
    if count < 3:
        raise ValueError (f"Devi mettere almeno 3 lettere maiuscole. {count}")
    for i in password:
        if i in sc:
            counter += 1
    if counter < 4:
        raise ValueError (f" Devi mettere almeno 4 caratteri speciali. {counter}")
    else:
        password = True
    return password

print(validate_password("AAA!!!!ieieie"))
    

        
        
    


      