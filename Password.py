import re

def check_password_strength(password):
    score=0
    feedback=[]

    if len(password)>=8:
        score+=1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        score+=1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score+=1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        score+=1
    else:
        feedback.append("Add at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score+=1
    else:
        feedback.append("Add at least one special character.")

    return score,feedback

password = input("Enter your password: ")
score, feedback = check_password_strength(password)

print("\nPassword Strength")
print("---------------------")
if score==5:
    print("Strong password!")
elif score >= 3:
    print("Medium strength password")
else:
    print("Weak password")

if feedback:
    print("\nSuggestions:")
    for f in feedback:
        print("-", f)