# README.md
## Summary
This script will scrape together jobs from Indeed.com and create Trello cards in the following format. Heavily based on this [article.](https://medium.com/@msalmon00/web-scraping-job-postings-from-indeed-96bd588dcb4b)

![](README/Screenshot%202017-09-19%2022.16.27.png)

## Requirements
	- BeautifulSoup4
	- [py-trello](https://github.com/sarumont/py-trello)

```
pip3 install beautifulsoup4
pip3 install py-trello
```

	- Trello Account with active boards
		- Trello API key can be found [here](https://trello.com/app-key)
		- Trello Token can be found [here](https://trello.com/1/authorize?expiration=never&scope=read,write,account&response_type=token&name=Server%20Token&key=c2a651f7b6e40d55ac59a8aa3e6a113a)

## Changes to be made
	- Fix pulling company name