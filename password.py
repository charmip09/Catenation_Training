def checker_password(passwd):
    
    SpecialSym=['$','@','#','%']
    return_val=True
    if len(passwd) < 8:
        print('the length of password should be at least 8 char long')
        return_val=False
    if len(passwd) > 30:
        print('the length of password should be not be greater than 30')
        return_val=False
    if not any(char.isdigit() for char in passwd):
        print('the password should have at least one numeral')
        return_val=False
    if not any(char.isupper() for char in passwd):
        print('the password should have at least one uppercase letter')
        return_val=False
    if not any(char in SpecialSym for char in passwd):
        print('the password should have at least one of the symbols $@#')
        return_val=False
    if return_val:
        print('Ok')
    return return_val

passwd = input('enter the password : ')
print(checker_password(passwd))