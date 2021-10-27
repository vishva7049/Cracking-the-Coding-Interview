def unique_char(string):
    if string is None:
        return False
    
    for i in string:
        if string.count(i) > 1:
            return False
    
    return True
print(unique_char("cat"))

print(unique_char("foo"))
