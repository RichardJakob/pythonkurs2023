var_tekst = "Sommeren lar vente på seg"

def oppgave(textdata):
    reversed_string = ""
    for letter in textdata:
        reversed_string = letter + reversed_string
    return reversed_string

print(oppgave(var_tekst))

print ("ferdig oppgave")
print("her kommer en ny linje")
print("her kommer enda en ny linje")
print("enda en endring")