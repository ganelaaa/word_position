# File Analyst
# April 13th, 2025

import os
    
#Startup information
print ("This is your current working directory\n")
print (os.getcwd())
print ("This is the list of contents in your directory\n")
print (os.listdir())

#Directory validation
directory_path = input("Choose which directory you wish to enter: ")

if os.path.exists(directory_path) and os.path.isdir(directory_path):
    print (f"You're now in {directory_path}")
else:
    print("Error: The provided path is not valid. Please try again.")
    exit()

#Determining quarter function
def determine_quarter(position, length):
     quarter_size = length // 4
     if position < quarter_size:
        return "first"
     elif position < 2 * quarter_size:
        return "second"
     elif position < 3 * quarter_size:
         return "third"
     else:
         return "fourth"
    
#Main Search
search_words = input("Please type what word you wish to find in this directory.")
user_input = ""
while user_input != "end":
    files = os.listdir(directory_path)
    for file_name in files:
        file_path = os.path.join(directory_path, file_name)

        if os.path.isfile(file_path):
            print(f"Searching in file {file_name}")
            try:
                with open(file= file_path, mode ='r') as file:
                    contents = file.read()
                    position = contents.find(search_words)
                    
                    if position != -1:
                        word_percent = (position / len(contents)) * 100
                        quarter = determine_quarter(position, len(contents))
                        print(f"The words '{search_words}' was found in file '{file_name}' at {word_percent:10.4f}% through the file.")
                        print(f"Quarter: {quarter}")

                        with open('fileanalyst_results.txt', 'a') as result_file:
                            result_file.write(
                                f"File: {file_name}, Word: {search_words}, Position: {position}, "
                                f"Percentage: {word_percent:10.4f}%, Quarter: {quarter}\n"
                            )

                        result_info = (file_name, position, word_percent, quarter)
                        print("Result tuple:", result_info)

            except Exception as e:
                print("An error occurred while reading the file:", e)

    user_input = input("Type 'end' to exit or press Enter to search again: ")
  