# David Prato CIS 276 Movie Guide Part 1

#Heading and List---------------------------------#

def display():
    print("Choose your Movie!\n")
    print("Menu Options\n")
    print("1: Movie List")
    print("2: Add a movie")
    print("3: Delete a movie")
    print("4: Exit")

# List Function -----------------------------------#

def list(movie_list):
    for i, title in enumerate(movie_list,start = 1): # Remember thata enumerates count the iterations and gives each list item an assoicted number. "Start is where that number begins 
        print(f'{i}. {title}\n')

# Add Function -------------------------------------#
def add(movie_list):

    title = input("Movie title: ")
    movie_list.append(title)# Once movie_list is created below, this will add movie to that list
    print("Your movie was added!")

# Delete Function ----------------------------------#
def delete(movie_list):
    movie_num = int(input("Choose the movie number from your list you wish to delete: "))
    if movie_num > 1 or movie_num < len(movie_list): #Remember that the list will be indexed, it's not going to count words or the like)
        title = movie_list.pop(movie_num -1)#pop deletes, remember since indexes start with 0, you must -1 from your intended target
        print(f'{title} was removed.\n')
    else:
        print("Invalid selection")

# Main Program ----------------------------------------#

def main():
    movie_list = ["The Boondock Saints",
                  "Fear and Loathing in Las Vegas",
                  "Trainspotting",
                  "It's a Wonderful Life",
                  "Scarface",
                  "Ben-Hur"] #Remember when we ue'll this is where that magic happens
    command = 0
    
    display()# displays our command menue

    while True: #"While True" is used to make a while loop operate until the given boolean condition becomes false
        try:
            command = int(input("Enter your choice number: \n"))
        except:
            print("Invalid input")
        if command == 1: 
            list(movie_list)
        elif command == 2:
            add(movie_list)
        elif command == 3:
            delete(movie_list)
        elif command == 4:
            break
        else:
            print("Invalid input, try again: \n")

    print("Thank you for using our service!")

if __name__ == "__main__": #This is used to call a "main()" function
    main()
