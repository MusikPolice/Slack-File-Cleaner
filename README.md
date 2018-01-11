# Slack-File-Cleaner 🛁
Frees up space by mass-deleting old, unpinned files in Slack channels and DM's.
## Usage
Download the `slack_delete.py` file and `cd` into it's directory.

```
python3 slack_delete.py --token <your-slack-token>
```
Replace `<your-slack-token>` with the [API token found here](https://api.slack.com/custom-integrations/legacy-tokens).

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
