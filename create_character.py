name = input ("Enter your character name")
strength= int(input("Enter your character's strength"))
intelligence = int(input("Enter your character's intelligence"))
charisma = int(input("Enter your character's charisma"))


def valued_name(name):
    if not isinstance(name,str):
        return "Name should be in Alphabet"
    elif " " in name:
        return "Name should not cotain space"
    elif name == "":
        return "Name should not empty"
    elif len(name) >10:
        return 'The character name is too long'
    
def valued_char_values():
    for  stats in(strength,intelligence,charisma):
        if not isinstance(stats,int):
            return "Values should in number"
        elif stats < 1:
             return 'All stats should be no less than 1'
        elif stats == "":
            return "Name should not empty"
        elif stats > 4:
             return 'All stats should be no more than 4'
    if strength+intelligence+charisma != 7 :
        return "The character should start with 7 points"
valued_char_values()
    
def creat_dots(stats):
        dots = "|"*stats+"-"*(10-stats)
        return dots
def creat_char():
    valued_name(name)
    char = f"""Name:= {name}\n 
    strength:= {creat_dots(strength)}
    intelligence:= {creat_dots(intelligence)}
    charisma:= {creat_dots(charisma)}"""

    return char
print(creat_char())
