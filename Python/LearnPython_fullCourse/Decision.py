is_male = True
is_tall = False

if is_male or is_tall:
    print("You are a male or tall")
else:
    print("You neither tall and male")


if is_male or is_tall:
    print("You are a male or tall")
else:
    print("You neither tall and male")


if is_male or is_tall:
    print("You are a male or tall")
elif is_male and not(is_tall): # tambem conhecido como elseif
    print("you are a short male")
else:
    print("You neither tall and male")
