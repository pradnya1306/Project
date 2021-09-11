print("***   welcome to Pradnya ToDo App  ***")

no_of_task=int(input("enter your number of task : "))
my_to_do_task=[]
task_status=[]
i=0
while i<no_of_task:
    task=input("enter your to do task: ")
    status=input("enter task status : ")
    i=i+1
    my_to_do_task.append(task) #append function is use to add the item end of list
    task_status.append(status)

print("your number of task = ",no_of_task)
k=0
while k<(len(my_to_do_task)):
    print(k+1,"task=",my_to_do_task[k])
    print(" ","status=",task_status[k])
    k=k+1
i=0
while i<4:
    option1=input("do you want do make changes(yes/no) : ")
    if option1=="yes":
        
        option=input("what do you want to do(add,delete,edit,clear all) :")
        if option=="add":
            new_task=input("enter your new task :")
            new_status=input("enter your new task status : ")
            my_to_do_task.append(new_task)
            task_status.append(new_status)
            print ("your  new task list :")
            j=0
            while j<len(my_to_do_task):
                print(j+1,"task= ",my_to_do_task[j])
                print(" ","status= ",task_status[j])
                j=j+1

        if option=="delete":
            delete_task=input("which task you want to delete :")
            delete_status=input("enter delete task status :")
            my_to_do_task.remove(delete_task) #remove use to remove specific item
            task_status.remove(delete_status)
            print("After delete task your task is :")
            f=0
            while f<len(my_to_do_task):
                print(f+1,"Task=",my_to_do_task[f])
                print(" ","Status= ",task_status[f])
                f=f+1

        if option=="edit":
            enter_task=int(input("which task you want to edit ,give number :"))
            print("task=",my_to_do_task[enter_task-1])
            edit_status=enter_task
            print("status=",task_status[edit_status-1])
            update_status=input("update the status :")
            task_status[edit_status-1]=update_status
            print("updated task list : ")
            b=0
            while b<len(my_to_do_task):
               print(b+1,"task=",my_to_do_task[b])
               print(" ","status=",task_status[b])
               b=b+1

        if option=="clear all":
            my_to_do_task.clear()#clear function is used to clear contain of list
            print(my_to_do_task)

        if option=="no":
            break #break statement breaks the loop
               
    if option1=="no":
        break
    i=i+1

print("showing number of tasks :  ",len(my_to_do_task))
n=0
while n<len(my_to_do_task):
    print(n+1,"task=",my_to_do_task[n])
    print(" ","status=",task_status[n])
    n=n+1