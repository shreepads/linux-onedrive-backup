# linux-onedrive-backup webapp

A tool that can be used to compare hashes to check the encrypted files were stored properly



## Setup

1. Use your MS Live login and register an app as per the instructions at: https://docs.microsoft.com/en-us/graph/auth-register-app-v2

1. Setup the app permissions and redirect URI

1. Note down the following values for your app:
   * App/ Client Id
   * App/ Client Secret
   * Tenant Id

1. Clone this repository:

   `$ git clone https://github.com/shreepads/linux-onedrive-backup.git`
   
1. cd into the directory, create a Python 3 virtual environment and activate it:

   `$ cd linux-onedrive-backup`
   
   `$ python3 -m venv venv`
   
   `$ source venv/bin/activate`
   
1. Install the requirements

   `(venv)$ pip install -r requirements.txt`
   

## Run

1. cd into the webapp/ folder and check the virtual environment is active

1. Setup the App/ Client Id, App/ Client Secret and Tenant Id as environment variables

   `(venv)$ read CLIENT_ID`
   
   `(venv)$ read CLIENT_SECRET`
   
   `(venv)$ read TENANT_ID`
   
   `(venv)$ export CLIENT_ID CLIENT_SECRET TENANT_ID`
   
1. Run the webapp

   `(venv)$ flask run --port 5000`
   
1. Open in browser as http://localhost:5000 (don't use the IP based URL output by Flask)

1. Click on the 'Sign In' link. Sign-in and provide consent for your app to access your
   MS Live account details (only needed the first time)

1. Click on the 'OneDrive files' link

