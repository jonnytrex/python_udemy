#Functions with Outputs

def format_name(f_name, l_name):
  firstname = f_name.title()
  lastname = l_name.title()
  return f"{firstname} {lastname}"
formatted_string = format_name(f_name="jon",l_name="trexler")

print(formatted_string)