import gspread
"""
STEPS TO GET API KEY FROM GOOGLE AND ACCESS TO THE GIVEN DOCUMENT

For this project to work you need to:
- go to Google Cloud
- create a project
- go to APIs
- enable the Google Drive API for the project
- then create credentials for Google Drive API with Application Data option
- go through the service account creation steps, role needed: Project/Editor (rest before doesn't matter)
- go to Credentials/Service Account, go to Keys, add a key, that is: JSON, this will download a JSON file,
  with your credentials, download and rename if you want to
- then in the nav menu, go to "API & Services" -> Enable APIs and Services
- search for "Google Sheets API", enable this as well

- "invite" your Python script via an email address -> email is in the JSON file we downloaded
  grab the e-mail -> open the Google Sheet -> use that email to share the document with editor permissions

Config completed.
"""
# -------------------------------------------------------------------
# Access the Google Services with the Service Account that we created
gc = gspread.service_account('json_key.json')

# -------------------------------------------------------------------
# Access the spreadsheet that our Service account was invited to
spreadsheet = gc.open('weather_public')

# --------------------
# Access by sheet name
# Access spreadsheet data by spreadsheet index (1st worksheet, index 0)
worksheet1 = spreadsheet.worksheet('2013')

# Access specific range of cells - Row
# Return format: List of Lists
row = worksheet1.get_values('A5:F5')
print(row)

# Return multiple rows - add diagonal start and end points (2 corners)
rows = worksheet1.get_values('A5:F7')
print(rows)

# Get row by index
row_index = worksheet1.row_values(3)
print(row_index)

# Get a column - 2 ways, 2nd is better
column = worksheet1.get_values('C2:C12')
print(column)

# Get a column - 2nd way -> index 2, then rows by index as well
column = worksheet1.col_values('2')[1:]
print(column)
