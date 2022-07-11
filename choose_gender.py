prompt = "\n---> "

def ask_gender():
    sex = input(prompt).lower().split(" ")
    gender_list = []
    
    for i in sex:
        new = i.strip(' "" .!? ')
        gender_list.append(new)

    if "boy" in gender_list:
        return ("he" , "him" , "his", "Onii-chan" , "boy")
    elif "girl" in gender_list:
        return ("she" , "her" , "her", "Onee-chan" , "girl")
    else:
        print("Invalid input. Just choose either boy or girl for now.")

print("Is Alex a boy or a girl?")

session = 1
while session == 1:
    try:
        pronoun1 , pronoun2 , pronoun3 , pet_name , gender = ask_gender()
        session = 0
    except TypeError:
        session = 1

print(f"""Alex is a {gender}.
{pronoun1} has 3 siblings who all calls {pronoun2} {pet_name}.Even {pronoun3} mom calls {pronoun2}
{pet_name}.""")
