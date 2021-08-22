# Functions 
#def my_function():
    #do this
    #then do this
    #finally do this

#Function with Inputs
#def my_function2(something):
    #do this with SOMETHING
    #then do this
    #finally do this

#Function with Outpus
#def my_function3():
   #result = 3 * 2
    #return result

def format_name(f_name,l_name): # f_name & l_name are parameters
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs." #escape the function if empty values
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title() #.title() has an output
    return f"Result: {formatted_f_name} {formatted_l_name}" #outputs can be returned
    #note that return is end of function

print(format_name(input("What is your first name? "), 
input("What is you last name? ")))

#print(format_name("jUlye", "yahI")) # shortned version of:
#formatted_name = format_name("keY", "jUke")
#print(formatted_name)