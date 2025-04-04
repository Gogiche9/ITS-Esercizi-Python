#Password Validation
 
def validate_password(password):
    sc = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-' 
          '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\', ']','^', '_','`', 
    '{', '|', '}', '~']
    if len(password) > 20:
        raise Exception(f"La password non dovrebbe superare i 20 caratteri. {len(password)}")
    for i in password:
        if i.isupper():
            count += 1
    if count < 3:
        raise Exception (f"Devi mettere almeno 3 lettere maiuscole. {count}")
    for i in password:
        
    


      