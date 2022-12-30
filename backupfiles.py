from datetime import date
from shutil import copyfile

date_backup = date.today()
print(date_backup)

str_date_backup = str(date_backup).replace('-', '.')

path_input = r'C:\Users\Name\OneDrive\Desktop\Testforautofiletobackupwithpython.txt'

path_output = r'C:\Users\Name\OneDrive\Documents\Backuplocation' + \
    '\\' + str_date_backup + 'Testforautofiletobackupwithpython.txt'

print(path_output)
# for copyfile module, specify source and destination
copyfile(path_input, path_output)