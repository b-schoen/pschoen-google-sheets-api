# PSchoen Google Sheets API

## Getting Started

First, check out the [getting started](docs/getting_started.md) section to get everything we need installed.

## First Example of Using Google Sheets API

Next, we'll run an [example using the google sheets api](docs/first_example.md). Don't worry about understanding the code here, this is just making sure everything is setup / that we're all signed in.

## Using the Google Sheets API

### Creating Spreadsheets
---

In `sublime`, open the file `create_spreadsheets.py`.

You should see a main function that looks like:

```python
def main():
    client = get_client()
    new_spreadsheet_title = "my_new_spreadsheet"
    create_spreadsheet(client, new_spreadsheet_title)
```

Change `my_new_spreadsheet` to a new name. We'll create a spreadsheet with the new name.

Run `python create_spreadsheets.py` to create a new spreadsheet:

```powershell
PS C:\Users\bschoen\pschoen-google-sheets-api> python create_spreadsheets.py
```

You should see output that looks something like this (with different spreadsheet name and id):

```bash
Authentication successful.
Authenticated! Building client...
Built client!
('Creating a spreadsheet with title: ', 'my_new_spreadsheet')
('Created new spreadsheet with spreadsheet ID: ', u'1MdJlMIQGylFIxXnconuc1HoDliBE77XjvWUXos6BSQY')
```

Now you should see a new spreadsheet on your Google Sheets page with the name you gave!

Now let's break down the `create_spreadsheet` function to get an idea of what happened here:

```python
def create_spreadsheet(client, spreadsheet_title):
    """
    Create a spreadsheet with the given title.

    Args:
        client: Google spreadsheets client
        spreadsheet_title: Title to give to new spreadsheet.

    References:
        https://developers.google.com/sheets/api/guides/create?refresh=1

    """
```

So our `create_spreadsheet` function takes in a `client` (the thing that actually connects to google and reads / writes data) and a `spreadsheet_title` (what we want to name our new spreadsheet).

Now, we need to specify to google what we want our new spreadsheet to look like:

```python
    # A spreadsheet is just represented by a dictionary
    spreadsheet = {
        'properties': {
            'title': spreadsheet_title
        }
    }
```

To do this, we just create a dictionary describing our new spreadsheet. The complete reference on what fields that dictionary can have is [here](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets?refresh=1).

This line specifies that we want our new spreadsheet to be titled `spreadsheet_title`.

```python
'title': spreadsheet_title
```

Now we'll send this information to google:

```python
new_spreadsheet = client.spreadsheets()
    .create(body=spreadsheet, fields='spreadsheetId')
    .execute()
```

The `client.spreadsheets().create()` call is how we tell google to create a new spreadsheet (full documentation [here](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/create?refresh=1)).

Here, `body=spreadsheet` is us saying "create the spreadsheet I described in the dictionary `spreadsheet`":

```python
create(body=spreadsheet
```

Then, `fields='spreadsheetId'` says which fields we want google to give us back (after it creates the new spreadsheet):

```python
create(..., fields='spreadsheetId')
```

Finally, `.execute()` tells the client that we're ready to send the request to google.

Now the client will send the request to google, and give us back the `spreadsheetId` field we asked for:

```python
# new_spreadsheet is a dictionary that looks like:
#
# {
#   'spreadsheetId': '1MdJlMIQGylFIxXnconuc1HoDliBE77XjvWUXos6BSQY'
# }
new_spreadsheet_id = new_spreadsheet['spreadsheetId']
```

Now we've successfully created a spreadsheet!
