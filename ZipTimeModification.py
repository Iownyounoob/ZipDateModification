'''
This code processes a zip file located at zip_path, modifying the date and time of each file in the archive to 1980 and 
adding it to a new zip archive located at output_zip_path. The file processing loop is run in multiple threads to improve 
performance. If an error occurs while processing a file or the zip file itself, an error message is printed to the console. Once 
all files have been processed, a message is printed indicating that the new zip file has been created.
'''

import zipfile
import threading
import os

zip_path = ''
output_dir = ''
output_zip_path = os.path.join(output_dir, '')

def process_file(file):
    try:
        # Create a new ZipInfo object with the same values as the original, but with a modified date and time
        new_zipinfo = zipfile.ZipInfo(file.filename)
        new_zipinfo.date_time = (1980, 1, 1, 0, 0, 0)

        # Read the contents of the file
        file_contents = zip.read(file.filename)

        # Add the file with the modified date and time to a new zip archive
        with zipfile.ZipFile(output_zip_path, 'a') as new_zip:
            new_zip.writestr(new_zipinfo, file_contents)
    except Exception as e:
        print(f"An error occurred while processing {file.filename}: {e}")

try:
    # Open the zip file for reading
    with zipfile.ZipFile(zip_path, 'r') as zip:

        # Get a list of all files in the zip archive
        files = zip.infolist()

        # Create a thread for each file in the zip archive
        threads = []
        for file in files:
            t = threading.Thread(target=process_file, args=(file,))
            threads.append(t)
            t.start()

        # Wait for all threads to complete before exiting
        for t in threads:
            t.join()

    print(f"New zip file created: {output_zip_path}")
except Exception as e:
    print(f"An error occurred while processing the zip file: {e}")
