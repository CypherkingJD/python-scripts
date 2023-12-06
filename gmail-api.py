import os
import google_auth_oauthlib.flow
from googleapiclient.discovery import build

# Define the Gmail API scope
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

# Create a flow object which handles the OAuth 2.0 authentication.
# This requires an open project with google cloud to get OAuth.
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    'your-credentials.json', SCOPES)

# Run the OAuth 2.0 authorization flow
creds = flow.run_local_server(port=0)

# Build the Gmail API service
service = build('gmail', 'v1', credentials=creds)

# Define the subject of the emails you want to list
subject_query = 'lingerie'

# List emails with the specified subject
results = service.users().messages().list(userId='me', q=f'subject:{subject_query}').execute()

# Check if there are any matching emails
if 'messages' in results:
    messages = results['messages']
    print(f'Found {len(messages)} emails with the subject: {subject_query}')

    # Loop through the list of email IDs
    for message in messages:
        email_id = message['id']
        # Fetch the email details if needed
        email = service.users().messages().get(userId='me', id=email_id).execute()
        print(f'Subject: {email["subject"]}, From: {email["from"]}')
else:
    print(f'No emails found with the subject: {subject_query}')
