import os

filenames = os.listdir('../cap1')

print('VERBOSE FILENAMES VARIABLE')
print(filenames)

txt_files = [filename for filename in filenames if filename.endswith('.txt') ]
print('TXT FILES')
print(txt_files)

any_py_on_filename = any(filename.endswith('.py') for filename in filenames)
print('ANY EXAMPLE')
print(any_py_on_filename)

