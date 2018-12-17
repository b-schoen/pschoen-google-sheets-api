"""
This file takes care of setting up a google spreadsheets api `service`.
"""
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'


def get_client():
    """Get a client (that has been authenticated) for google sheets."""
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    print("Looking for credentials...")
    store = file.Storage('token.json')
    creds = store.get()

    if not creds or creds.invalid:

        print("Credentials not found locally, authenticating via google...")
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)

    print("Authenticated! Building client...")
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    print("Built client!")
    return service
