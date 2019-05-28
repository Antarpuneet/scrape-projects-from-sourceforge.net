# -*- coding: utf-8 -*-
"""
Created on Tue May 28 20:35:10 2019

@author: Antarpuneet
"""

from bs4 import BeautifulSoup
import  requests
import re


for i in range(1,10): #Select the page numbers from which projects are needed
        
            page = requests.get(f'https://sourceforge.net/directory/?page={i}') 
            soup = BeautifulSoup(page.content, 'html.parser')
        
            productLinks = soup.findAll('a', attrs={'class' : 'button green hollow see-project'})
            for link in productLinks:
                a=link['href']
                l=a[10:-1]
               
               
                with open(f'names.txt','a') as f:
                    f.write(l)
                    f.write('\n')
        

                    


