def is_in_list(list_search, string):
    if string.lower() in list_search:
        print("%s is already in the database!" % string)
    else:
        list_search.append(string)
        print("%s has been added in the database!" % string)

list_search = ["georges simenon", "agatha christie", "arthur conan doyle", "alice walker", "richard adams", "clarice linspector", "machado de assis"]
string = input("Type the name of a writer so we can check if it's in our database: ")
is_in_list(list_search, string)