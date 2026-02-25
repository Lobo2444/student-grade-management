def menu_input(promptmenu):
    while True:
        try:
            choice = int(input(promptmenu))
            if 1 <= choice <= 5:
                return choice
            else:
                print("Choose between 1 and 5")
        except ValueError:
            print("Enter a valid number")


def returntomenu(promptreturnmenu):
    while True:
        
            
            returnchoice=str(input(promptreturnmenu)).strip().lower()
            if returnchoice in ('y', 'n' or 'Y', 'N'):
                return returnchoice
            else:
                
                print("Provide Y/N to continue")


def input_errorhandling(prompt):
    while True:#integer input error handling
        try:
            markv = int(input(prompt))
            if 0 <= markv <=100:
                return markv
            else:
                print("Mark should be between 0 to 100")
        except ValueError:
            print("Insert an integer not string")


#-----------------------
std_data_scheme={}
#-----------------------



def std_menu_mng():
    
    print("""
==============================================
    WELCOME TO STUDENT GRADE MANAGEMENT SYSTEM
==============================================
    1) VIEW Student Marks Data
    2) ADD Students & Marks Data
    3) UPDATE Students & Marks Data
    4) REMOVE Students & Marks Data
    5) Exit
===================================================
""")
        



def std_view():
    if not std_data_scheme:
        print("*******************The are no information or data to view****************** ")
    else:
        for name,markdetails in std_data_scheme.items():
            print(f"Student Name: {name}")
            for subname,markvalue in markdetails.items():
                print(f"{subname}: {markvalue} ")
            print("-----------------")

def std_add():
        stdName=input("Enter the Name of the Student: ").strip()
        if stdName in std_data_scheme:
            print(f"Student {stdName} already Exist choose 3 to Update Marks")
            return
            
        
        stdsub=["English","Tamil","Science","Social","Maths"]   
        submarks={}
        for sub in stdsub:
            submarks[sub]=input_errorhandling(f"{sub} Mark: ")
                 
        totalmarks=sum(submarks.values())
        avgmarks=totalmarks/len(submarks)
        submarks['Total Mark']=totalmarks
        submarks["Average Mark "]=avgmarks

        std_data_scheme[stdName]=submarks
        print("Student Data is ADDED Successfully!!!")
        retmenu=returntomenu("Do you want to continue[Y/N]:")
        if retmenu == 'y':
            std_add()
        else:
            return

    
#std_data_scheme={}
def std_update():

    stdName = input("Enter the Name of the Student: ").strip()
    if stdName in std_data_scheme:
        print(f"Student {stdName} exist")

        sub_update_logic(stdName)
    else:
        print(f"Student {stdName} doesn't EXIST")
        retmenu=returntomenu("Do you want to continue[Y/N]:")

        if retmenu == 'y':
            std_update()
        else:
            return 


def sub_update_logic(stdName):
        update_spec_mark=input("What subject mark to update: ").strip()
        stdsub=["English","Tamil","Science","Social","Maths"]   
        
        
        if update_spec_mark not in stdsub:
            print("Invalid Subject")
            return sub_update_logic(stdName)
        new_mark=input_errorhandling(f"New {update_spec_mark} Mark : ")

        std_data_scheme[stdName][update_spec_mark]=new_mark                    
        totalmarks=sum(std_data_scheme[stdName][sub] for sub in stdsub)
        avgmarks=totalmarks/len(stdsub)
        std_data_scheme[stdName]['Total Mark']=totalmarks
        std_data_scheme[stdName]["Average Mark "]=avgmarks

        print(f"Student {stdName} {update_spec_mark} Mark is updated successfully!!!")
        retmenu=returntomenu("Do you want to continue[Y/N]:")

        if retmenu == 'y':
            std_update()
        else:
            return 


        

        

def std_remove():
    stdName = input("Enter the Name of the Student: ").strip()
    if stdName in std_data_scheme:

        print(f"Student {stdName} exist")
        del std_data_scheme[stdName]#delete the std name(all data related to that name)
        print(f"Student {stdName} Data as been deleted successfully!!!")
        retmenu=returntomenu("Do you want to continue[Y/N]:")

        if retmenu == 'y':
            std_remove()
        else:
            return 
    else:
        print(f"Student Name Doesn't Exist")

        retmenu=returntomenu("Do you want to continue[Y/N]:")

        if retmenu == 'y':
            std_remove()
        else:
            return 

    
    




        
       
        
def run():
    while True:
        std_menu_mng()
        choice=menu_input("Choose any number to continue OPERATION: ")

        if choice == 1:
            std_view()
        elif choice == 2:
            std_add()
        elif choice == 3:
            std_update()
        elif choice == 4:
            std_remove()
        elif choice == 5:
            break
        
         
if __name__ == "__main__":
    run()   




             

    
    
