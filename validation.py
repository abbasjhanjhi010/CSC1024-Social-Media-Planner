import datetime
# ======================
# Abbas's contirbution, adding validation functions
# ======================

def validate_required_input(prompt):   # validates against empty fields
    while True:
        value = input(prompt).strip()
        if value != "":
            return value
        print("--> Input cannot be empty. Please try again.")

def validate_date(prompt):   # efnorces proper date fromat 
    while True:
        date_input = input(prompt).strip()
        try:
            datetime.datetime.strptime(date_input, "%d/%m/%Y")
            return date_input
        except ValueError:
            print("-> Invalid date. Please enter date in DD/MM/YYYY format.")

def validate_positive_integer(prompt):   # makes sure all inputs for record engagement metrics are positive
    while True:
        try:
            number = int(input(prompt))
            if number >= 0:
                return number
            else:
                print("--> Number cannot be negative.")
        except ValueError:
            print("--> Enter only a positive integer.")


def validate_unique_id(post_id):    # Checks if POSTID is unique and numeric
    if not post_id.isdigit():
        return print("--> Only positive integer ID's are accepted")

    try:
        with open("posts.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0].upper() == post_id.upper():
                    return print("--> The ID you entered isn't unique, enter unique ID.")
    except FileNotFoundError:
        # File does not exist yet, therefore no duplicates
        pass
    return True

def validate_platform(platform_input):   # runs check if user input of platofrm exists, if yes True, otheriwse its False
    try:
        with open("platforms.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                # platform name is stored at index 1
                if data[1].lower() == platform_input.lower():
                    return True
    except FileNotFoundError:
        print("--> platforms.txt not found.")
    return False

# ==========    Yao Tengs Contribution    ========== 
def file_check(file_name):  #checks whether core files exists 
    try:
        with open(f"{file_name}", "r") as file:   #try to open the file in read mode,
            pass
    except FileNotFoundError:   #if an error occurred, that means the file does not exist
        print(f"{file_name} does not exists, creating a new file.")
        if file_name == "platforms.txt":     #adds valid platforms to new file
            with open(f"{file_name}", "a") as file:
                file.write("1,Facebook\n"
                           "2,Tiktok\n"
                           "3,Instagram\n"
                           "4,X")
            print("All valid platforms automatically filled in")
        else:
            with open(f"{file_name}", "w") as file:
                pass
        pass
        
