
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