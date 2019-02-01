import os,gani

input("\nWelcome to the Gani's directory editor! Type 'Enter' to see what i can do! ")
print("\n->Type '1' to move to a directory")
print("\n-->Type '2' to see the content of the current directory")
print("\n--->Type '3' to delete a directory")
print("\n---->Type '4' to create a directory")

 
ans = 100
while ans != 0:
    number = int(input("\nWhat do you want me to do? Type the number here ---> "))
    if number == 1:
        answer = input("\nWhere do you want to move? Type directory name here ---> ")
        try:
            os.chdir(answer)
            print("\nMoved to {} succesfully".format(answer))
        except FileNotFoundError:
            print("\nDirectory doesn't exist :(")
            
    if number == 2:
        for i in os.listdir(path="."):
            print("\n",i)
    
    if number == 3:
        answer = input("\nWhat directory do you want to delete? Type directory name here ---> ")
        gani.deldir(answer)
    
    if number == 4:
        answer = input("\nWhat directory do you want to create? Type directory name here ---> ")
        gani.adddir(answer)
        
    print("\nType '1' if you want to continue or type '0' if you need to go :(" )
    ans = int(input("\nYour answer : "))

print("\nOkay, see you later ;( ")
  
            
            
    
    


		
