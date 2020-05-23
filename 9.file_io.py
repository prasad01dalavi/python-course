# File Writing
file_obj = open("my_file.txt", "w")
content = """
these are my file contents
this is line #2
this is line #3
bla bla bla
"""
file_obj.write(content)
file_obj.close()

# File Reading
file_obj = open("my_file.txt", "r")
my_data = file_obj.read()
print(f'file contents: {my_data}')
file_obj.close()

# another easy and widely used method
with open("my_file.txt", "r") as file_obj:
	print('reading using with:',file_obj.read())

# File Appending
file_obj = open("my_file.txt", 'a')
new_contents = "\n\n\tthese are my new contents"
file_obj.write(new_contents)
file_obj.close()

with open("my_file.txt", 'a') as f:
	f.write(new_contents)

