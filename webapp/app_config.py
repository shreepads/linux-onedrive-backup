import os


CLIENT_SECRET = os.getenv("CLIENT_SECRET")
if not CLIENT_SECRET:
     raise ValueError("Need to define CLIENT_SECRET environment variable")

CLIENT_ID = os.getenv("CLIENT_ID")
if not CLIENT_ID:
     raise ValueError("Need to define CLIENT_ID environment variable")

TENANT_ID = os.getenv("TENANT_ID")
if not TENANT_ID:
     raise ValueError("Need to define TENANT_ID environment variable")


AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app
# AUTHORITY = "https://login.microsoftonline.com/" + TENANT_ID


REDIRECT_PATH = "/getAToken"  # It will be used to form an absolute URL
    # And that absolute URL must match your app's redirect_uri set in AAD


# You can find more Microsoft Graph API endpoints from Graph Explorer
# https://developer.microsoft.com/en-us/graph/graph-explorer
ENDPOINT = 'https://graph.microsoft.com/v1.0/users'  # This resource requires no admin consent
DRIVE_ENDPOINT = "https://graph.microsoft.com/v1.0/me/drive"

CLOUDBACKUP_FOLDER_NAME = "CloudBackup"   # Must be present in the OneDrive root folder

# You can find the proper permission names from this document
# https://docs.microsoft.com/en-us/graph/permissions-reference
SCOPE = ["User.Read", "Files.Read"]


SESSION_TYPE = "filesystem"  # So token cache will be stored in server-side session
