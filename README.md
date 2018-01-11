# Slack-File-Cleaner 🛁
Frees up space by mass-deleting old, unpinned files in Slack channels and DM's.
## Usage
Download the `slack_delete.py` file and `cd` into it's directory.

```
python3 slack_delete.py --token <your-slack-token>
```
Replace `<your-slack-token>` with the [API token found here](https://api.slack.com/custom-integrations/legacy-tokens).
```
[*] Fetching file list..
    Filename2.jpg is pinned to #general.
    Filename1.pdf is pinned to a private direct message.
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
The sript will show you each `file_id` and whether or not the file could be deleted.


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
