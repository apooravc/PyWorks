import webbrowser

print("Searching from CMD")
while (True):
    print("\nSearch types available:")
    types_list = ["1. All results", "2. Images", "3. Videos", "4. News", "5. Maps"]
    for type_string in types_list:
        print(type_string)
    print("Enter 6 to exit script")

    input_num = None
    while (True):
        try:
            input_num = int(input("Please enter number of search type to perform or exit script: "))
            if (input_num < 1 or input_num > 6):
                print("Please enter a number b/w 1 and 6")
            else:
                break
        except ValueError:
            print("Please enter a number")
    if (input_num == 6):
        break
    else:
        print("Search type selected: ", types_list[input_num - 1])

    query_string = input("Enter your query: ")
    query_string = query_string.strip().replace(" ", "+")
    url_types = ["https://www.google.com/search?q=", "https://www.google.com/search?tbm=isch&q=", "https://www.youtube.com/results?search_query=", "https://www.google.com/search?tbm=nws&q=", "https://www.google.com/maps/place/"]
    result = webbrowser.open(url_types[input_num - 1] + query_string)
