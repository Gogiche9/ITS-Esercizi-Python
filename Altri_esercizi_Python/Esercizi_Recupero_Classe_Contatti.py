#Esercizi_Recupero_Classe_Contatti

class ContactManager:

    def __init__(self): #chiave è nome contatto, valore numero telefono come stringa
            self.contacts:dict[str,list[str]] = {}

    def create_contact(self,name:str,phone_number:list[str])->dict[str,list[str]]:
        new_contact = {}
        for k,v in self.contacts.items():
            if k == name:
                 raise ValueError(f"Errore: il contatto esiste già.")
            else:
                self.contacts[name]= phone_number
                new_contact[name] = phone_number
                return new_contact
    #Si può ottimizzare usando l'if per confrontare la key
    
    def add_phone_number(self,contact_name:str,phone_number:str)->dict[str,list[str]]:
        updated_phone_number = {}

        for k,v in self.contacts.items():
            if k == contact_name:
                if phone_number not in v:
                    self.contacts[contact_name].append(phone_number)
                    updated_phone_number[contact_name] = phone_number
                    return updated_phone_number
                else:
                    raise ValueError("Errore: il numero di telefono esiste già.")
            else:
                raise ValueError("Errore: il contatto non esiste.")
    
    def remove_phone_number(self,contact_name: str, phone_number: str)->dict[str,list[str]]:
        removed_phone_number = {}
        for k,v in self.contacts.items():
            if k == contact_name:
                if phone_number in v:
                    v.remove(phone_number)
                    removed_phone_number[contact_name] = phone_number
                    return removed_phone_number
                else:
                    raise ValueError("Errore: il numero di telefono non è presente.")
            else:
                raise ValueError("Errore: il contatto non esiste.")
    
    def update_phone_number(self,contact_name: str, old_phone_number: str,new_phone_number: str)->dict[str,list[str]]:
        new_updated_number = {}
        for k,v in self.contacts.items():
            if k == contact_name:
                if old_phone_number in v:
                    v.remove(old_phone_number)
                    v.append(new_phone_number)
                    new_updated_number[contact_name] = new_phone_number
                    return new_updated_number
                    
                else:
                    raise ValueError("Errore: il numero di telefono non è presente.")
            else:
                raise ValueError("Errore: il contatto non esiste.")


            
                
                         
                         
                
         
        
        

          