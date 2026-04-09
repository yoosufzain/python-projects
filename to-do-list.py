print("Welcome to to-do-list maker")
print("if you not want to add any task please press enter without any words")

tasks = []
run_button = True 
run2_botton =True
def add_task():
        global get_task
        get_task = input("Add your task:")
        tasks.append(get_task)
        return tasks  
while True:
     retrned_task = add_task()
     for i in retrned_task:
          print(i)
     if get_task == "":
          tasks.pop(-1)
          break  


def get_index():
           global index
           index = int(input("Enter your task's index"))  

def del_task():
                        
            if (len(tasks)-1) < index or index <0:

               print("please enter the correct index")
            else:
               tasks.pop(index)
               for i in tasks:
                 print(i)   
get_del_task = input("Do you want to delete any task yes or no:")
if get_del_task == "yes" or get_del_task == "no":
     if get_del_task == "yes":
          while True : 
                for ind, task in enumerate(tasks):
                    print(ind,task) 

                if len(tasks) == 0:
                      break      
                get_index()  
                if index == "":
                     break
                del_task()              
else:
         print("Don't type any words")
