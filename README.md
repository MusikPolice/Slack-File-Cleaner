# Slack-File-Cleaner 🛁

## Usage
Download the `slack_delete.py` file and `cd` into it's directory.

```
python3 slack_delete.py --token <your-slack-token>
```
Replace `<your-slack-token>` with the [API token found here](https://api.slack.com/custom-integrations/legacy-tokens).

## Optional Flags
```
--days <number-of-days>
```
Set the script to delete files older than `<number-of-days>` days. 

The default is to delete unpinned files over 30 days old.

```
--count <max-number-of-files>
```
Set the script to delete a maximum of `<max-number-of-files>` at one time. 

The default is to delete a maximum of 1000 files.

