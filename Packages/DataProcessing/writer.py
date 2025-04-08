def write_data(file_name):
    with open (file_name, "w") as file:
        file.write("Hello here are the contents that I have entered into Output.txt file\n") 
    return f"Writing data to {file_name}"
