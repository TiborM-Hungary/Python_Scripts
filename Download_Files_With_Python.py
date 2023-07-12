import requests

# Get the url for the file you want to download
url = 'URL_Of_The_File_You_Want_To_Download'

# Using requests establish a GET request
req = requests.get(url)
# Save the content from the GET request
content = req.content

# The content is binary data, has to write it back into a file
# filename, wb - write-binary
with open('download.mp3', 'wb') as file:
    file.write(content)
