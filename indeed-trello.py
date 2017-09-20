#!/usr/bin/python
import requests
import bs4
from bs4 import BeautifulSoup

import time
from trello import TrelloClient

def getSoup():
    location1 = "location"

    keyword1 = str("job+title")
    url = "https://www.indeed.com/jobs?q=%s&!%s" % (keyword1,location1)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')


    return soup

def getTitle(soup):
    #This function will grab all of the job titles from the page

    title = {}
    j_num = 0
    for div in soup.find_all(name='div',attrs={'data-tn-component':'organicJob'}):
        for a in soup.find_all(name='a', attrs={'data-tn-element':'jobTitle'}):
            j_num += 1
            title[j_num]= (a['title'])

    return title

def getCity(soup):
    #Grabs the location of the position and adds it to a list

    city = {}
    j_num = 0
    for div in soup.find_all(name='div',attrs={'data-tn-component':'organicJob'}):
        for span in soup.find_all(name='span',attrs={'class':'location'}):
            j_num += 1
            city[j_num] = (span.text)

    return city

def getCompany(soup):
    #Grabs the company name and adds it to a list

    company = {}
    j_num = 0
    for div in soup.find_all(name='div',attrs={'data-tn-component':'organicJob'}):
        for span in soup.find_all(name='span',attrs={'itemprop':'hiringOrganization'}):
            company_name = span.text
            print(company_name)
            for l in company_name:
                if l == '':
                    pass
                else:
                    j_num +=1
                    company[j_num] = l

    return company


def getSummary(soup):
    #Pulls the summary and appends it to a list



    summary = {}
    j_num = 0
    for div in soup.find_all(name='div',attrs={'data-tn-component':'organicJob'}):
        for span in soup.find_all(name='span',attrs={'class':'summary'}):
            j_num += 1
            summary[j_num]= (span.text)
    return summary


def getUrl(soup):
    #THis function will pull the url and append it to a list


    url = {}
    j_num = 0
    for div in soup.find_all(name='div',attrs={'data-tn-component':'organicJob'}):
        for a in soup.find_all(name='a',attrs={'data-tn-element':'jobTitle'}):
            j_num += 1
            url[j_num]=("https://indeed.com"+a['href'])

    return url
def getTrello():
    #This function connects to the trello API
    client = TrelloClient(api_key='your_trello_api_key',token='your_trello_token')

    return client
def selectList(client):
    #This function takes the trello client and selects the board id and list_id you would like to work with
    all_boards = client.list_boards()
    job_board_name = 'your_board_name'
    for i in all_boards:
        board_name = str(i)
        if job_board_name in board_name:
            job_board_id = i
        else:
            pass

    list_id = job_board_id.list_lists()[0]

    return list_id

def createCards(job):
    #This function creates Trello cards based off of the information pulled from indeed
        client = getTrello()
        list_id = selectList(client)
        title, city, summary, url = job
        num = "number of jobs you want added"
        for i in range(1,num):
            list_id.add_card("%s | %s" % (title[i],city[i]))
            newest_card = list_id.list_cards()[-1]
            newest_card.set_description(summary[i])
            newest_card.attach(url=url[i])



def getPage(soup):
    #This function will pull the page and remove unnecissary HTML
    title = getTitle(soup)
    city = getCity(soup)
    #Need to fix up grabbing the company name
    #company = getCompany(soup)
    summary = getSummary(soup)
    url = getUrl(soup)

    job = [title, city, summary, url]

    createCards(job)


def main():
    soup = getSoup()
    getPage(soup)


main()
