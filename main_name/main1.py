from main2 import fun2

# The variable __name__ for the file/module that is run will be always __main__. 
# But the __name__ variable for all other modules that are being imported
#  will be set to their module's name.

def fun1():
    print("Inside main1")

fun2()

if __name__=="__main__":
    print("Directly running main1")
else:
    print("Running main1 from import")