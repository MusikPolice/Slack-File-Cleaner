# Slack-File-Cleaner 🛁
Frees up space by mass-deleting old, unpinned files in Slack channels and DM's.

## Getting a Token
Unfortunately, Slack apps are not allowed to delete files that were uploaded by other users, even if they have been granted the `files:write` scope.

To get around this limitation, you'll need to authenticate using OAuth so that the script can act on behalf of your Slack user account. 

This means that the script will have the same permissions as your Slack user, and will only be able to delete files that your user account can delete. In other words, it is best to run the script as the workspace administrator, otherwise it will only be able to delete files that were uploaded by your user account.

If you prefer to follow the official docs for this process, see https://api.slack.com/legacy/oauth. Otherwise, read on.

### Creating a Slack App
Before you can do anything, you'll need to create a Slack App.

Navigate to https://api.slack.com/apps and click on the green "Create New App" button in the top-right hand corner of the page.

In the dialog box that appears, give the App a name, and choose the target workspace from the Development Slack Workspace dropdown box. Click the green Create App button.

### Getting a Client ID and Client Secret
Next, we'll get the client id and secret for your new app. This will be used during the authentication process.

Navigate to https://api.slack.com/apps/. The App that you just created should be listed under Your Apps. Click on its name.

On the page that appears, scroll down to the App Credentials section and copy the Client ID and Client Secret. You'll need these later.

### Creating a Redirect URL
From the left-hand sidebar, select OAuth & Permissions from under the Features header.

On the page that appears, scroll down to the Redirect URLs section, and click on the Add New Redirect URL button.

In the text box, enter any valid URL. Ideally, it would be the URL for a website that you own, but for the purposes of this exercise, it doesn't really matter what it is. Click Add and then Save.

Make sure that you note the Redirect URL that you created. We'll need it in the next step.

### Getting an OAuth Token
#### Getting a Code
With your Client ID, Client Secret, and Redirect URL in hand, you can (finally!) generate a [User Token](https://api.slack.com/authentication/token-types#user) that will allow the script to act on your behalf.

Paste the following URL into your web browser, replacing `xxx-my-client-id-xxx` with the Client ID from above, and `xxx-my-redirect-url-xxx` with the *url encoded* Redirect Url from above:
https://slack.com/oauth/authorize?client_id=xxx-my-client-id-xxx&scope=files%3Aread%20files%3Awrite%3Auser%20channels%3Aread%20channels%3Awrite&redirect_uri=xxx-my-redirect-url-xxx

> Note: this URL grants the script the `files:read`, `files:write:user`, `channels:read`, and `channels:write` scopes. For an explanation of what each of these scopes does, see https://api.slack.com/legacy/oauth-scopes

When you press enter, the browser will pop up a Slack login form. 
 * If you are not logged in to the target workspace, it will prompt you to enter your username and password
 * If/once you are logged in, it will ask you if you want to install the App that you created above in your workspace. Click the green Allow button.

 Your browser will now redirect to the Redirect URL that you created above, and will have appended a `code` URL parameter to the address. Your address bar should contain something like this:
 http://xxx-my-redirect-url-xxx?code=129875155511.1624231732978.78798b8f128f40198eca8fd6dfd296932ea9d00427d419e1db632bf68167e597&state=

 Copy the text between `code=` and `&state`. This is your Code.

 #### Exchanging the Code for a User Token
 We finally have everything that we need to get a [User Token](https://api.slack.com/authentication/token-types#user) that the script can authenticate with!

 Paste the following URL into your web browser, replacing `xxx-my-client-id-xxx` with the Client ID from above, `xxx-my-client-secret-xxx` with the Client Secret from above, `xxx-code-xxx` with the Code from the previous step, and `xxx-my-redirect-url-xxx` with the *url encoded* Redirect Url from above:
 https://slack.com/api/oauth.access?client_id=xxx-my-client-id-xxx&client_secret=xxx-my-client-secret-xxx&code=xxx-code-xxx&redirect_uri=xxx-my-redirect-url-xxx

If all goes well, your browser should show you a chunk of JSON. Copy the `access_token` attribute. It should be a string that starts with the letters `xoxp-`. This is your [User Token](https://api.slack.com/authentication/token-types#user).

## Using the Script
```
python3 slack_delete.py --token <your-user-token>
```
Replace `<your-user-token>` with the token generated via the steps above.
```
[*] Deleting files older than 30 days from general..
    3 unpinned files.
  
[*] Delete the unpinned files? (y/n): y
```
Confirm if you want to delete the unpinned files by typing `y` or `n`.
```
[*] Deleting files older than 30 days ...
    1 of 3 - F8R1W9P7S True
    2 of 3 - F9R1X8P7S True
    3 of 3 - F7R1W9P7Z True

[*] Done
```
The script will show you each `file_id` and whether or not the file could be deleted.


## Optional Flags
Set the script to delete files older than `<number-of-days>` days. <br>The default is to delete unpinned files over 30 days old.
```
--days <number-of-days>
```
Set the script to delete a maximum of `<max-number-of-files>` at one time. <br>The default is to delete a maximum of 1000 files.
```
--count <max-number-of-files>
```

#### Credits: Forked from [this gist by jamescmartinez](https://gist.github.com/jamescmartinez/909401b19c0f779fc9c1).
