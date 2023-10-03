SPACES_TO_THE_RIGHT = 4

def print_list_element(x, level=0):
  space = ' ' * SPACES_TO_THE_RIGHT * level
  if type(x) == list:
    for _ in x:
      print_list_element(_, level + 1)
  else:
    print(space, x)

variable_type_list1 = ["A", [12, 15, [6, 7, 8, 9]]]
variable = "B"

print_list_element(variable_type_list1)
print_list_element(variable)
