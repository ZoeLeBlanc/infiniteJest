# Infinite Jest Networks Project

Built from Ciera Martinez @iamciera [Infinite Jest Repo](https://github.com/iamciera/infiniteJest)
- license: [GNU GPL v2.0](http://choosealicense.com/licenses/gpl-2.0/)


## Directories

1. `data` - Data files organized by type.  Either made directly from text or scraped from the internet
2. `py` - python scripts
3. csv files hold the output of the scripts

## Requirements
- install python
- install pipenv
- `pipenv install pandas`

## To run scripts:
first argument book text file, second argument character list
eg.
```
pipenv run python ./py/char.parser.py ./data/bookText/David-Foster-Wallace-Infinite-Jest-v2.0.chptags.txt ./data/character/samantha_characters_list.txt
```
