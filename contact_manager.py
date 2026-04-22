print("do you want to say yes only type 'y' and do you want to say no only type 'n'")
print("do want to exit anything please press enter without any words or letter")
contact = {  
}
add_run = True 
srch_run = True
del_run = True 
letters = "abcdefghijklmnopqrstuvwxyz"
characters = letters+letters.upper()+"!@#$%^&*()_+=-|;:?/>,.<"
def add_contact():
   global add_run
   name = input("Enter your contact name?").capitalize()
   number = input('Enter your contact number')
   if name == '' or number == '':
      add_run= False
   if name in contact.keys():
      return "This name is already exsist"
   else :
      for char in characters:
          if char in number:
              "Please type only numbers for contact number?"
          else:
            contact[name] = number
def del_contacts():
   global del_run
   access = ""
   del_name = input("Enter what number do you want to delet").capitalize()
   if del_name == '':
      del_run = False
   for key in contact.keys():
      if del_name == key:
         access = True 
     
   if access != True:
      print("Name is not exsist")
      pass 
   permission = input("conform to delete" )
   if permission == 'y':
      contact.pop(del_name)
   elif permission == 'n':
       pass
   else:
       print("don't type any words or letters")
def search_contact():
   global srch_run 
   srch_name = input("Enter what number do you want?").capitalize()
   if srch_name == '' :    
            srch_run= False
            pass
   if srch_name in contact.keys():
         print(contact.get(srch_name))   
   else:
         print("Name does not match") 
         desition = input("do you want to add any numer to this name")
         if desition == 'y':
            add_contact()
def show_contact():
   result = "Your contacts:"
   for key,values in contact.items():
      result+= f"\n {key}"
   print (result) 
while add_run :
   add_contact()
   show_contact()
desition = input("do you want to delete any contacts?").strip().lower()
if desition == 'n':
   del_run= False
elif desition == "y":
   del_run = True
else:
    print("Please don't type any words.") 
while del_run:
    del_contacts() 
    show_contact()
desition = input("do you want to search any contacts?").strip().lower()
if desition == 'y':
    srch_run= True
elif desition =='n' or desition == '':
   srch_run = False
else :
    print("don't type any word")
while srch_run:
            search_contact()