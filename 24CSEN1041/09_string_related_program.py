password = "Py@1234"

has_upper = False
has_lower = False
has_digit = False
has_special = False

for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    else:
        has_special = True

print("Password:", password)

if has_upper and has_lower and has_digit and has_special:
    print("Password Strength: Strong")
else:
    print("Password Strength: Weak")

#output
Password: Py@1234
Password Strength: Strong
