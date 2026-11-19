def get_number(msg):
    while True:
        try:
            choice = int(input(msg).strip())
            return choice
        except ValueError:
            msg = "Enter only numbers! "

def get_string(msg):
    while True: 
        choice = input(msg).strip()
        if choice:
            return choice
        else:
            msg = "Enter non-empty string! "