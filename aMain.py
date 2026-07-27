# ======================
#Abbas's code section:
# ======================
from validation import validate_date, validate_positive_integer,validate_required_input, validate_unique_id, validate_platform, validate_post_status

def subheading(option):
    print(f"\n----------------------------\n{option}\n-----------------------")   #takes less space for subheading
# ======================
#Cheng Zher's code section:
# ======================
def main_menu():
    while True:
        print("=====================================")
        print("SOCIAL MEDIA CONTENT PLANNER")
        print("=====================================")
        print("1. Add New Post")
        print("2. Update Post Status")
        print("3. Record Engagement Metrics")
        print("4. Display Content Calendar")
        print("5. Generate Performance Report")
        print("6. Export Report to File")
        print("7. Exit")
        initial_choice = input("\nEnter your choice: ").strip()
        match initial_choice: #match-case is neat compared to long if/elif chain
            case "1":
                new_post_menu()
            case "2":
                post_status_menu()
            case "3":
                engagement_entry()
            case "4":
                content_calendar_menu()
            case "5":
                generate_report_menu()
            case "6":
                export_report()
            case "7":
                print("Exiting Program...")
                break #exits the while True loop, ending the program
            case _:
                print("Enter valid choice (1-7)")

def new_post_menu():
    while True:
        subheading("Add New Post")
        print("1. Draft New Post")
        print("2. Go Back")
        first_choice = input("\nEnter your choice: ").strip()
        match first_choice:
            case "1":
                draft_new_post()
            case "2":
                return #return back to main_menu() loop
            case _:
                print("Enter valid choice (1-3)")

def draft_new_post():
   # Abbas validation file, removed try catch block previously in its place
    while True:
        post_id = validate_required_input("\nEnter Post ID: ")
        if validate_unique_id(post_id):
            break
        # end of abbas validation file

    print("\nAvailable Platforms")
    platform_list = []
    try:
        with open("platforms.txt","r") as file:
            for line in file:
                platform = line.strip().split(",")
                platform_list.append(platform[1]) #platform[1] = platform name
                print(f"- {platform[1]}")
    except FileNotFoundError:
        print("platforms.txt not found")
        return #cannot validate platform choice without file, so stop
    
    #Abbas validation file
    while True: 
        platform = input("\nEnter Platform: ").strip()
        if validate_platform(platform): # validates platform using platforms.txt
            break
        print("Invalid platform. Please choose from the list above.")

    caption = validate_required_input("Enter Caption: ") # ensures non-empty caption
    schedule_date = validate_date("Enter Scheduled Date (DD/MM/YYYY): ") # validates date format    
    #end of validation file

    status = "Draft" #every new created post starts with Draft status
    with open("posts.txt","a") as file: #"a" = append mode, add lines without erasing existing posts
        file.write(f"{post_id},{platform},{caption},{schedule_date},{status}\n") #comma separated to match read/split format in file
    print("\nPost added successfully.")
    print(f"Status: {status}")
    print("\nThen save into: ")
    print("posts.txt")
    print(f"\n{post_id}|{platform}|{caption}|{schedule_date}|{status}") #display field separation using "|"

# ======================
#Keen's code section:
# ======================

def post_status_menu():
    while True:
        subheading("Update Post Status")
        print("1. Update Status")
        print("2. Go back")
        choice = input("\nEnter your choice: ").strip()
        match choice:
            case '1':
                update_post_status()
            case '2':
                return #returns back to main menu loop
            case _:
                print("Enter a valid option (1-3)")

def update_post_status():
    print("\n====== Update Post Status ======")

    post_id = validate_required_input("Enter the Post ID to update: ") #now goes to validation.py

    try:
        with open("posts.txt", "r") as file: #opens and reads posts.txt 
            lines = file.readlines() #reads posts.txt file line by line
    except FileNotFoundError: #catch cases where the posts.txt file does not exist
        print("No posts to be updated, create a post and try again.")
        return #stops after post ID cannot be found

    post_found = False #checks if desired post was found, initialise status as not found before loop begins
    new_lines = [] #list to hold lines to be written back into posts.txt

    for line in lines: #goes through each line already saved in posts.txt 
        data = line.strip().split(",") 
        if data[0].upper() == post_id.upper(): #designates data[0] as post ID
            post_found = True #check if post ID was found, status gets updated to true
            current_status = data[4] #stores the post current status and is used to check for future updates to status
            print(f'\nPost ID: {data[0]}')
            print(f'Platform: {data[1]}')
            print(f'Caption: {data[2]}')
            print(f'Scheduled Date: {data[3]}')
            print(f'Current Status: {current_status}')

            if current_status == "Draft": #allows posts with 'draft' status to update to scheduled or posted
                print("\n1. Update to Scheduled")
                print("2. Update to Posted")
                print("3. Cancel")
                status_choice = input("Enter option (1-3)\n")

                if status_choice == '1':
                    data[4] = "Scheduled" #updates the current status into scheduled from draft
                    print("Post Status has been updated to Scheduled.")
                elif status_choice == '2':
                    data[4] = "Posted" #updates current status from draft to posted
                    print("Post Status has been updated to Posted.")
                else:
                    print("Status update cancelled.")

            elif current_status == "Scheduled":
                confirm_status = input("\nUpdate status to Posted? (y/n): ").strip() #scheduled posts can only be updated to posted and not back to draft
                if confirm_status == 'y':
                    data[4] = "Posted"
                    print("Status has been updated to Posted.")
                else: 
                    print("Status update cancelled.")
            elif current_status == "Posted": #already posted, no further changes can be done
                print("\nThis post has already been posted, no updates can be made.")
            else:
                print("\nPost Status Unknown... Unable to update.")

            new_line = ",".join(data) #separates the new lines with commas
            new_lines.append(new_line + "\n")
        else:
            new_lines.append(line) #adds back lines that dont match post ID back without changes

    if not post_found: #could not find a post ID to match user input
        print("Post ID not found.")
        return #exits since there is nothing to update
    with open("posts.txt", "w") as file: #opens posts.txt in write mode
        file.writelines(new_lines) #rewrites entire updated list into posts.txt

def content_calendar_menu():
    while True:
        subheading("Content Calendar Menu")
        print("\n1. Display All Posts")
        print("2. View Full Post Details")
        print("3. Go Back")
        choice = input("\nEnter your choice: ").strip()
        match choice:
            case "1":
                display_content_calendar()
            case "2":
                view_full_details()
            case "3":
                return #returns back to main menu loop
            case _:
                print("Enter valid choice (1-4)")

def display_content_calendar():
    print("\n====== Content Calendar ======")
    try:
        with open("posts.txt", "r") as file:
            lines = file.readlines() #reads all lines in posts.txt
    except FileNotFoundError: #for cases where posts have not been created yet
        print("Post does not exist.")
        return
    if len(lines) == 0: #for cases where posts have been created but are empty
        print("Post does not exist.")
        return

    #for the column headers, formatted to ensure the table is aligned and fix the width
    print(f"{'Post ID':<10}{'Platform':<15}{'Caption':<25}{'Date':<14}{'Status':<10}")
    print("-" * 74) #prints - to match the width of the all column header width

    for line in lines:
        data = line.strip().split(",") #splits line with commas
        post_id = data[0]
        platform = data[1]
        caption = data[2]
        schedule_date = data[3]
        status = data[4]

        if len(caption) > 20: #prevent text from overflowing to next column after 20 letters
            caption = caption[0:20] + "..." #adds ... after the 20 letters

        #left aligning each column field to each respective field width
        print(f"{post_id:<10}{platform:<15}{caption:<25}{schedule_date:<14}{status:<10}")

def view_full_details(): #to check the specific details of a post, since some may be cut off for being too lengthy in the table
    print("\n====== View Post Details ======")

    # Abbas - validation file
    post_id = validate_required_input("\nEnter Post ID: ")
    

    try:
        with open("posts.txt", "r") as file:
            lines = file.readlines() #read saved post lines in posts.txt
    except FileNotFoundError: 
        print("No posts found.")
        return

    for line in lines: #search for matching post ID in posts.txt
        data = line.strip().split(",") #split line with comma to match their respective fields/columns
        if data[0] == post_id: #check for a match in the post ID column
            print(f"\nPost ID: {data[0]}")
            print(f"Platform: {data[1]}")
            print(f"Caption: {data[2]}")
            print(f"Scheduled Date: {data[3]}")
            print(f"Status: {data[4]}")
            return #post ID was found and printed so it stops searching
    print("Post ID not found.") #match was not found for the post ID

# ======================
#Yao Teng's code section:
# ======================

#----------------smaller functions-----------------
def engagement_file_check():
    #checks whether engagement.txt exists
    print("\nChecking if file exists...")
    try:
        with open("engagement.txt", "r") as file:   #try to open engagement.txt in read mode,
            print("File exists, no changes made.")  #if successful, it means the file exists
            pass
    except FileNotFoundError:   #if an error occurred, that means the file does not exists
        print("File does not exists, creating a new file.")     #opens a new file called engagement.txt
        with open("engagement.txt", "w") as file:
            pass
def posted_check():
    #checks and creates a list of post IDs that have the "Posted" status
    posted_posts= []
    with open("posts.txt", "r") as file:
        for row in file:
            data = row.strip().split(",")   #splits each row based on separator ","
            if data[4] == "Posted":         #reads the 4th index, which is the "Status" column
                posted_posts.append(data[:4])   #if is "Posted", appends to list while omitting the status itself
            else:
                pass
    return posted_posts     #returns the list
def posts_data_extraction(userin):
    #returns the data for the entire row of post ID based on user specified ID
    valid_posts = posted_check()
    for row in valid_posts:
        if row[0] == userin.upper():
            return row      #returns the entire row of data
def id_verification(userin):
    #checks whether user input is inside engagement.txt
    with open("engagement.txt", "r") as file:
        for row in file:
            data = row.strip().split(",")
            if data[0] == userin.upper():
                return True
    return False
    #remvoed int_validity and replaced with validate_positive_integer - Abbas

def interaction_formula(view,like,comment,shares):
    #calculate interaction score
    view_score = view * 0.001
    like_score = like * 0.002
    comment_score = comment * 0.004
    shares_score = shares * 0.003
    interaction_score = view_score + like_score + comment_score + shares_score
    return interaction_score    #returns the interaction score
def total_interaction(platform):
    #calculate total interactions from the specified platform
    views = 0
    likes = 0
    comments = 0
    shares = 0
    with open("engagement.txt", "r") as file:
        for row in file:
            data = row.strip().split(",")
            if data[1] == platform:
                views += int(data[2])
                likes += int(data[3])
                comments += int(data[4])
                shares += int(data[5])
    return(f"Total Views -- {views}"
           f"\nTotal Likes -- {likes}"
           f"\nTotal Comments -- {comments}"
           f"\nTotal Shares -- {shares}")
#--------------------------------------------------
def engagement_entry():
    #allows user to record engagement metrics
    engagement_file_check()     #runs the function to check whether engagement.txt exists
    subheading("Record Engagement Metrics")
    valid_posts = posted_check()    #gets a list of posts with "Posted" status
    print("Please choose from one of these posts to log engagement data.\n")
    for i in valid_posts:       #prints out every valid posts
        print(i)
    print("======================================================================")
    while True:
        inputID = input("Enter your post ID [Q to quit]: ")
        if inputID.strip().upper() != "Q":      #if user input is not "Q", proceed with next line, otherwise break from this function
            if not id_verification(inputID):    #if inputted ID is already inside engagement.txt, tells user to enter another ID
                if posts_data_extraction(inputID) is not None:  #if the returned value is not None, or contains something, proceed with next line, otherwise tells user to enter a valid ID
                    data = posts_data_extraction(inputID)       #gets the data of the inputted post ID
                    post_ID = data[0]
                    platform = data[1]
                    print(f"\nYou are currently adding entry for {post_ID}.")
                    #use int_validity(userin) to check whether user input is an integer without causing an error

                    # now using the validation file to verify instead
                    views = validate_positive_integer("Enter the number of views: ")
                    likes = validate_positive_integer("Enter the number of likes: ")
                    comments = validate_positive_integer("Enter the number of comments: ")
                    shares = validate_positive_integer("Enter the number of shares: ")
                    #end of abbas contribution

                    with open(f"engagement.txt", "a") as file:      #opens engagement.txt and appends the data inputted inside
                        file.write(f"{post_ID},{platform},{views},{likes},{comments},{shares}\n")
                    print(f"\n========================================"
                          f"\nEngagement data successfully logged.\n"
                          f"\nPostID, Platform, Views, Likes, Comments, Shares"
                          f"\n{post_ID},{platform},{views},{likes},{comments},{shares}\n")
                    break
                else:
                    print("\n============================="
                          "\nPlease enter a valid post ID.")
            else:
                print("\n==========================================================="
                      "\nThis ID already has a record, please enter another post ID.")
        else:
            print("\n===================="
                  "\nOperation cancelled.\n")
            break
def generate_report_menu():
    #generates a menu to print performance report
    while True:
        subheading("Performance Report")
        print("\n1. Total Posts"
              "\n2. Best Performing Post"
              "\n3. Highest Interacted Platform"
              "\n4. Print All"
              "\n5. Return")
        choice = input("\nEnter your choice: ")
        match choice.strip():
            case "1":
                print(total_posts())
            case "2":
                print(best_performing())
            case "3":
                print(highest_interaction())
            case "4":
                print(total_posts())
                print(best_performing())
                print(highest_interaction())
            case "5":
                break
            case _:
                print("Enter a valid choice (1-5)")
def total_posts():   #calculates the total posts from each platform
    fb, ig, tt, x = 0
    data = posted_check()       #gets the data of all posts with "Posted" status
    for row in data:            #sort each row of data by platform
        platform = row[1]
        if platform.lower()== "facebook":
            fb += 1
        elif platform.lower()== "instagram":
            ig += 1
        elif platform.lower()== "tiktok":
            tt += 1
        elif platform.lower()== "x":
            x += 1
    total_posted = ig + fb + ig + tt + x
    return(f"\n\nTotal Posts From All Platforms"
           f"\n=============================="
           f"\nFacebook -- {fb}"
           f"\nInstagram -- {ig}"
           f"\nTikTok -- {tt}"
           f"\nX -- {x}"
           f"\nTotal Posted -- {total_posted}"
           f"\n==============================\n")
def best_performing():      #calculate and find the best performance post
    try:
        best_score = 0
        best_post = None        #sets the current best post as none to prevent error
        with open("engagement.txt", "r") as file:       #try to open engagement.txt in read mode, if file does not exists, prompt user to enter engagement metrics
            for row in file:        #go through each row in engagement.txt
                data = row.strip().split(",")
                post_id = data[0]
                view_score = int(data[2]) * 0.004       #based on the number of views, likes, comments, and shares, calculate the performance score
                like_score = int(data[3]) * 0.003
                comment_score = int(data[4]) * 0.001
                shares_score = int(data[5]) * 0.002
                performance_score = view_score + like_score + comment_score + shares_score
                if performance_score > best_score:      #compare current performance score with previous best score
                    best_score = performance_score      #if current score is greater than previous score,
                    best_post = post_id                 #sets the current post as best performing post
                    best_view = data[2]
                    best_like = data[3]
                    best_comment = data[4]
                    best_share = data[5]
        if best_post is None:   #if engagement.txt contains no data, prompt user to enter engagement metrics
            return("\n\n================================================================"
                   "\nNo engagement data found, please enter engagement metrics first.\n")
        return(f"\n\nBest Performing Post"
               f"\n=============================="
               f"\nPost ID -- {best_post}"
               f"\nNo. Views -- {best_view}"
               f"\nNo. Likes -- {best_like}"
               f"\nNo. Comments -- {best_comment}"
               f"\nNo. Shares -- {best_share}"
               f"\nPerformance Score -- {best_score:.2f}"
               f"\n==============================\n")
    except FileNotFoundError:
        return("\n\n======================================================================"
               "\nengagement.txt does not exists, please enter engagement metrics first.\n")
def highest_interaction():
    #finds the platform with the highest interaction
    try:
        best_score = 0
        best_platform = None
        fb_score = 0
        ig_score = 0
        tt_score = 0
        x_score = 0
        with open("engagement.txt", "r") as file:   #try to open engagement.txt in read mode, if file does not exists, prompt user to enter engagement metrics
            for row in file:                        #sorts each row in engagement.txt by platform
                data = row.strip().split(",")
                platform = data[1]
                match platform:                     #calculates interaction score based on each platform
                    case "Facebook":
                        fb_score += interaction_formula(int(data[2]),int(data[3]),int(data[4]),int(data[5]))
                    case "Instagram":
                        ig_score += interaction_formula(int(data[2]),int(data[3]),int(data[4]),int(data[5]))
                    case "TikTok":
                        tt_score += interaction_formula(int(data[2]),int(data[3]),int(data[4]),int(data[5]))
                    case "X":
                        x_score += interaction_formula(int(data[2]),int(data[3]),int(data[4]),int(data[5]))
        #compares score of each platform to determine the highest
        if fb_score > ig_score and fb_score > tt_score and ig_score > x_score:
            best_platform = "Facebook"
            best_score = fb_score
        elif ig_score > fb_score and ig_score > tt_score and ig_score > x_score:
            best_platform = "Instagram"
            best_score = ig_score
        elif tt_score > fb_score and tt_score > ig_score and tt_score > x_score:
            best_platform = "TikTok"
            best_score = tt_score
        elif x_score > fb_score and x_score > ig_score and x_score > ig_score:
            best_platform = "X"
            best_score = x_score
        platform_interaction = total_interaction(best_platform)     #calculates the total interactions from said platform
        return(f"\n\nHighest Interacted Platform"
               f"\n=============================="
               f"\nPlatform -- {best_platform}"
               f"\n{platform_interaction}"
               f"\nInteraction Score -- {best_score:.2f}"
               f"\n==============================\n")
    except FileNotFoundError:
        return("\n\n======================================================================"
               "\nengagement.txt does not exists, please enter engagement metrics first.\n")
def export_report():
    #export performance report with user specified name
    try:
        with open("engagement.txt", "r") as file:       #try to open engagement.txt in read mode, if file does not exists, prompt user to enter engagement metrics
            pass
        total_posts_report = total_posts()                  #print out and assign every mini report to their own unique variable
        best_performing_report = best_performing()
        highest_interaction_report = highest_interaction()
        subheading("Exporting Performance Report..")  
        while True:
            report_name = input("\nEnter the name of the file [Q to quit]: ")       #prompts user to enter name of report
            if report_name.strip() != "":       #checks if user entered nothing, if yes then prompt user to enter again
                if report_name.strip().upper()!= "Q":       #checks if user entered "Q", if yes then break from this function
                    with open(f"{report_name}.txt", "w") as file:       #open a new file with user specified name
                        for i in [total_posts_report.lstrip(), best_performing_report, highest_interaction_report]:
                            file.write(i)       #writes the mini reports into it
                    print(f"\n\nPerformance Report successfully exported as {report_name}.txt"
                          f"\n=================================================================\n")
                    break
                else:
                    print("\n===================="
                          "\nOperation cancelled.\n")
                    break
            else:
                print("Please enter a valid file name.")
    except FileNotFoundError:
        print("\n\n======================================================================"
              "\nengagement.txt does not exists, please enter engagement metrics first.\n")

if __name__ == "__main__":
    main_menu()

# Final program testing by Abbas & Cheng Zher
