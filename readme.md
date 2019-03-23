About
-----------------
I looked everywhere for an easy to use list of companies for some ML stuff I'm
toying around with. So I figured while I'm building this out I mine as well share it.

Contributing
-----------------
You need both `requests` and `lxml` installed via pip on Python 3.
If you add a new list, please create it similiar to `companies_list.py` but 
name it specific to what the list represents, eg: (sp500_list.py).

* Add a new URL to the list of `urls`
* Add the name of the file to the `fileName` list
* Add the xpath string to `urlXpath` list

Submit a PR.