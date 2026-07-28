age:int

age=4

name:str

is_human:bool

def police_check(age:int)->bool:
    if age >= 18:
        can_drive=True
    else:
        can_drive=False
    return can_drive

print(police_check(age))