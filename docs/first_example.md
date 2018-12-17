## First Example of Using Google Sheets API

The following is based on the instructions [here](https://developers.google.com/sheets/api/quickstart/python).

I've created a dummy account (with the following info) for use in these examples:

```json
{
    "First Name": "DummyFirstName537",
    "Last Name": "DummyLastName",
    "Email Address": "dummyfirstname537dummylastname@gmail.com",
    "Password": "DummyPassword"
}
```

1. We'll need to install the `google client library` in powershell

```powershell
PS C:\Users\bschoen\pschoen-google-sheets-api> pip install --upgrade google-api-python-client oauth2client
```

2. Run the python script `quickstart.py`:

```powershell
PS C:\Users\bschoen\pschoen-google-sheets-api> python quickstart.py
```

It should open a new tab in your internet browser, and ask you to login.

It will then read an example spreadsheet provided by google, and print out all the values in it:

```python
Name, Major:
Alexandra, English
Andrew, Math
Anna, English
Becky, Art
Benjamin, English
Carl, Art
Carrie, English
Dorothy, Math
Dylan, Math
Edward, English
Ellen, Physics
Fiona, Art
John, Physics
Jonathan, Math
Joseph, English
Josephine, Math
Karen, English
Kevin, Physics
Lisa, Art
Mary, Physics
Maureen, Physics
Nick, Art
Olivia, Physics
Pamela, Math
Patrick, Art
Robert, English
Sean, Physics
Stacy, Math
Thomas, Art
Will, Math
```

Now that we've got a basic example working, we can move on to understanding / using the API.
