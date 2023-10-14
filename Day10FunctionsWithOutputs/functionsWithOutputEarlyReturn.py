#Functions with Outputs

def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  firstname = f_name.title()
  lastname = l_name.title()
  return f"Result: {firstname} {lastname}"

#formatted_string = format_name(f_name="jon",l_name="trexler")
#print(formatted_name)

print(format_name(input("What is your first name? "),input("What is your last name? ")))