
def inputVerb():
    verb = ""
    while verb == "":
        user_input = input("Entrez un verbe du 1er groupe: ").lstrip().rstrip()
        if user_input == "":
            print("Le verbe ne peut être vide\n veillez réessayer!")
        else:
            if len(user_input) > 3:
                if user_input.isalpha:
                    if user_input.lower().endswith("er"):
                        verb = user_input
                    else:
                        print("Le verbe entré n'est pas un verbe du 1er groupe")
                
                else:
                    if user_input.isnumeric:
                        print("le verbe ne peut être un nombre, veillez réessayer!")
                    print("Le verbe entré n'est pas correct")
            else:
               print('Hum??? Il semblerait que le verbe entré ne soit pas correct')
               if user_input.isnumeric:
                    print("le verbe ne peut être un nombre, veillez réessayer!")
    return verb
