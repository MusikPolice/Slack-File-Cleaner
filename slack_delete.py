from urllib.parse import urlencode
from urllib.request import urlopen
import argparse
import time
import json
import codecs

reader = codecs.getreader("utf-8")

def main():
    """
    Entry point of the application
    :return: void
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--token", required=True, help="Specifies the OAuth token used for authentication, created at (https://api.slack.com/docs/oauth-test-tokens)")
    parser.add_argument("-d", "--days", type=int, default=30, help="Delete files older than x days (optional)")
    parser.add_argument("-c", "--count", type=int, default=1000, help="Max amount of files to delete at once (optional)")
    options = parser.parse_args()

    # Initialize Deletion

    try:
        print("\n[*] Fetching file list..")
        files = list_files(token=options.token, count=options.count, days=options.days)
        unpinned_files = ignore_pinned(token=options.token, files=files)

        if(len(unpinned_files) > 0):
            file_ids = [f['id'] for f in unpinned_files]
            delete_files(token=options.token, file_ids=file_ids, days=options.days)
        else:
            print("\n[*] There are no unpinned files older than", options.days, "days to be deleted!")


        print("\n[*] Done\n")

    except KeyboardInterrupt:
        print("\b\b[-] Aborted")
        exit(1)

def calculate_days(days):
    """
    Calculate days to unix time
    :param days: int
    :return: int
    """
    return int(time.time()) - days * 24 * 60 * 60

def list_files(token, count, days):
    """
    Get a list of all file
    :param token: string
    :param count: int
    :param days: int
    :return: list
    """
    params = {'token': token, 'ts_to': calculate_days(days), 'count': count}
    uri = 'https://slack.com/api/files.list'
    response = reader(urlopen(uri + '?' + urlencode(params)))
    return json.load(response)['files']

def get_channel_name(token, channel_id):
    """
    Get a list of all file
    :param token: string
    :param channel_id: string
    :return: list
    """
    #channel_type = channel_id[0:1] == 'C' ? 'channel' : 'conversation'
    params = {'token': token, 'channel': channel_id}
    #if(channel_type == 'channel'):
    #    uri = 'https://slack.com/api/channels.info'
    #else:
    #    uri = 'https://slack.com/api/conversations.info'
    uri = 'https://slack.com/api/conversations.info'
    response = reader(urlopen(uri + '?' + urlencode(params)))
    channel = json.load(response)['channel']
    if 'name' in channel:
        return '#' + channel['name']
    else:
        return 'a private direct message.'

def delete_files(token, file_ids, days):
    """
    Delete a list of files by id
    :param token: string
    :param file_ids: list
    :param days: int
    :return: void
    """
    confirm = input("\n[*] Delete the unpinned files? (y/n): ");
    if(confirm == 'y' or confirm == 'Y'):
        print("\n[*] Deleting files older than", days, "days ...")
        count = 0
        num_files = len(file_ids)
        for file_id in file_ids:
            count += 1
            params = {
              'token': token,
              'file': file_id,
            }
            uri = 'https://slack.com/api/files.delete'
            response = reader(urlopen(uri + '?' + urlencode(params)))
            print("\t", count, "of", num_files, "-", file_id, json.load(response)['ok'])
    else:
        print("\n[*] Files will not be deleted.")

def ignore_pinned(token, files):
    """
    Get a list of all files that are not pinned
    :param token: string
    :param files: list
    :return: list
    """
    count = 0
    num_files = len(files)
    unpinned_files = []
    for f in files:
        if 'pinned_to' in f:
            channelNames = []
            for c in f['pinned_to']:
                channelNames.append(get_channel_name(token=token, channel_id=c))
            print("\t", f['name'], "is pinned to", ' & '.join(channelNames))
        else:
            count += 1;
            unpinned_files.append(f)
    print("\t", count, "unpinned files.")
    return unpinned_files

if __name__ == '__main__':
    main()
