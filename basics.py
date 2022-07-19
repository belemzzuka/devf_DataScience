"""
variable = "Hi";
suma = 40 + 30;
print (variable);
print (suma);
"""
# Comentario de 1 linea

def run():
    print("This function runs the program");
    phrase = "This is a phrase as a string";
    phrase1 = phrase.upper().lower().capitalize();
    phrase2 = phrase.replace(" ", "💡");
    phrase3 = phrase[::-1]
    print(phrase);
    print(phrase1);
    print(phrase2);
    print(phrase3);
    
if __name__ == "__main__":
    run();