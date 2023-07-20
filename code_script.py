# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 04:24:58 2023

@author: MSI
"""

import requests
from bs4 import BeautifulSoup
import lxml
import csv

input=input('please input the date in the form MM/DD/YYYY :')
page = requests.get(f'https://www.yallakora.com/match-center/%D9%85%D8%B1%D9%83%D8%B2-%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%8A%D8%A7%D8%AA?date={input}')

def main(page):
    
    src=page.content
    soup = BeautifulSoup(src,"lxml")
    matchs_details=[]
    
    championship=soup.find_all('div',{'class' : 'matchCard'})
    
    def get_match_info(championship):
        title = championship.contents[1].find('h2').text.strip()
        kind=championship.contents[3].find('div',{'class':'date'}).text.strip()
        all_matches=championship.contents[3].find_all('li')
        number_of_matches=len(all_matches)
        
        for i in range(number_of_matches):
            #find team name
            team_A=all_matches[i].find('div',{'class':'teamA'}).find('p').text.strip()
            team_B=all_matches[i].find('div',{'class':'teamB'}).find('p').text.strip()
            
            #find scores
            match_score=all_matches[i].find('div',{'class':'MResult'}).find_all('span',{'class':'score'})
            score=f"({match_score[0].text.strip()} - {match_score[1].text.strip()})"
            
            #match time
            time=all_matches[i].find('div',{'class':'MResult'}).find('span',{'class':'time'}).text.strip()
            
            matchs_details.append({'نوع البطوله':title ,'الوصف':kind , "الفريق الاول":team_A, "الفؤسق الثانى":team_B,"النتيجه": score ,"التوقيت":time})
    for i in range(len(championship)):
        
        get_match_info(championship[i])
    
        
    
    keys=matchs_details[0].keys()

    with open("C:/Users/MSI/Desktop/web_script/yallakora.csv","w",newline='', encoding='utf-8-sig') as output:
        dic_writer=csv.DictWriter(output,keys)
        dic_writer.writeheader()
        dic_writer.writerows(matchs_details)
        print('sucess')

main(page) 