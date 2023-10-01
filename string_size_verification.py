def string_verification(string_value):
    MAX_LEN = 120
    MIN_LEN = 5
    if len(string_value) > MAX_LEN or len(string_value) < MIN_LEN:
        print("Please write a password between %d and %d digits." % (MIN_LEN, MAX_LEN)) 
    else:
        print("Your password was saved!")
        return string_value 
    
string_value = input("Password: ")
string_verification(string_value)
