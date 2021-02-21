# JSON_Nav

JSON_Nav is a project that lets you navigate through a chosen .json file.

## Installation

Clone the repository

```bash
git clone https://github.com/Adeon18/JSON_Nav
```

## Usage

```bash
json_nav/json_navigation.py
---------------
Starting...
Give the .json file path: data/user_timeline_obama.json
---------------
This is a list. Print all the 20 options?(y is usually a bad idea) (y/n) n
Choose an option index: 1
---------------
This is an object. Here are all the avalible keys:
created_at
id
id_str
text
truncated
entities
extended_entities
in_reply_to_status_id
in_reply_to_status_id_str
in_reply_to_user_id
in_reply_to_user_id_str
in_reply_to_screen_name
user
geo
coordinates
place
contributors
is_quote_status
retweet_count
favorite_count
favorited
retweeted
possibly_sensitive
lang
---------------
Choose a key: created_at
Sun Feb 14 14:01:17 +0000 2021
Exit? (y/n) n
Choose a key: id
1360952254627520512
Exit? (y/n) y
```


## License

[MIT](https://choosealicense.com/licenses/mit/)