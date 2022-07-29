myfile = open('data.txt', 'r')  # on reading mode
file_content = myfile.read()

myfile.close()
print(file_content)

user_name = input('Enter your name: ')
my_file_write = open('data.txt', 'w')
my_file_write.write(user_name)
my_file_write.close()
