# import the function that gets us an authenticated
# google spreadsheets api client. We'll need this to
# make calls to read / write data.
from my_google_spreadsheets_client import get_client


def create_spreadsheet(client, spreadsheet_title):
    """
    Create a spreadsheet with the given title.

    Args:
        client: Google spreadsheets client
        spreadsheet_title: Title to give to new spreadsheet.

    References:
        https://developers.google.com/sheets/api/guides/create?refresh=1

    """
    print("Creating a spreadsheet with title: ", spreadsheet_title)

    # A spreadsheet is represented by a dictionary
    #
    # The complete reference to what this dictionary can look like (if you want to add more complex
    # fields): https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets?refresh=1
    spreadsheet = {'properties': {'title': spreadsheet_title}}

    # Now we'll use the client to actually create the new spreadsheet on Google Sheets
    #
    # The reference for what the `spreadsheets().create` call can do (with examples) is here:
    # https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/create?refresh=1
    new_spreadsheet = client.spreadsheets().create(
        body=spreadsheet, fields='spreadsheetId').execute()

    # Now the client gave us back all the info about our newly created spreadsheet
    new_spreadsheet_id = new_spreadsheet['spreadsheetId']

    print('Created new spreadsheet with spreadsheet ID: ', new_spreadsheet_id)


def main():
    client = get_client()
    new_spreadsheet_title = "my_new_spreadsheet"
    create_spreadsheet(client, new_spreadsheet_title)


if __name__ == "__main__":
    main()