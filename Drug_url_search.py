# Thanks Torvalds
# Thanks Jadi
# Thanks Stallman

import os
import sys
import requests
import re
from googlesearch import search
from colorama import init, Fore, Back, Style
from bs4 import BeautifulSoup
import json
from time import sleep

print("""

                        ██╗  ██╗██╗   ██╗ ██████╗ ███╗   ██╗██╗   ██╗███████╗    ███╗   ███╗███████╗██████╗ ██╗ ██████╗ █████╗ ██╗     
                        ██║ ██╔╝╚██╗ ██╔╝██╔════╝ ████╗  ██║██║   ██║██╔════╝    ████╗ ████║██╔════╝██╔══██╗██║██╔════╝██╔══██╗██║     
                        █████╔╝  ╚████╔╝ ██║  ███╗██╔██╗ ██║██║   ██║███████╗    ██╔████╔██║█████╗  ██║  ██║██║██║     ███████║██║     
                        ██╔═██╗   ╚██╔╝  ██║   ██║██║╚██╗██║██║   ██║╚════██║    ██║╚██╔╝██║██╔══╝  ██║  ██║██║██║     ██╔══██║██║     
                        ██║  ██╗   ██║   ╚██████╔╝██║ ╚████║╚██████╔╝███████║    ██║ ╚═╝ ██║███████╗██████╔╝██║╚██████╗██║  ██║███████╗
                        ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝    ╚═╝     ╚═╝╚══════╝╚═════╝ ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝

""")

text = "\t\t\t\t\t\t >>>>       KYGnus-Medical       <<<<   \n \t\t\t\t\t>>> I Try to Transfer Linux Philosophy to MSWindows Users <<< \n \t\t\t\t\t\t>> I hope I'm successful at this way. << \n\n\t"
for character in text:
    sleep(0.1)
    sys.stdout.write(character)
    sys.stdout.flush()


print("                 =======================================================================================================                 \n")
drugname = input("Enter Drugname (That's Better to Type Persian): ")



# https://dadardaru.com

dadardaru = requests.get(f"https://dadardaru.com/?s={drugname}&post_type=product&cat_id=")

dadardaru_soup = BeautifulSoup(dadardaru.text,"html.parser")

val = dadardaru_soup.find_all('p' , attrs={'class':"stock out-of-stock"})
if (re.search("در انبار موجود نمی باشد",str(val))):
    print(f"{drugname} [ Not Found ] => https://dadardaru.com/")
elif (re.search("در انبار موجود می باشد",str(val))):
    print(f"{drugname} [ Found ] => https://dadardaru.com/")
else:
    print("[ unknown ] Response From darardaru.com")



# https://darookhaneonline.com

darooboom = requests.get(f"https://darookhaneonline.com/index.php?route=product/search&search={drugname}")
#
darooboom_soup = BeautifulSoup(darooboom.text,"html.parser")
#
val = darooboom_soup.find_all('div' , attrs={'class':"main-products-wrapper"})
if (re.search("وجود ندارد",str(val))):
    print(f"{drugname} [ Not Found ] => https://darookhaneonline.com/")
elif (re.search(f"{drugname}",str(darooboom_soup))):
    print(f"{drugname} [ Found ] => https://darookhaneonline.com/")
else:
    print("[ unknown ] Response From darookhaneonline.com")




# https://www.darukade.com

darukade = requests.get(f"https://www.darukade.com/products?w={drugname}")

darukade_soup = BeautifulSoup(darukade.text,"html.parser")

val = darukade_soup.find_all('div' , attrs={'class':"readonly-rating-star"})
if val:
    print(f"{drugname} [ Found ] => www.darukade.com/")
else:
    print(f"{drugname} [ Not Found ] => www.darukade.com/")





#https://hatamdrug.com

hatamdrug = requests.get(f"https://hatamdrug.com/shop?keyword={drugname}")

hatamdrug_soup = BeautifulSoup(hatamdrug.text,"html.parser")

val = hatamdrug_soup.find_all('div' , attrs={'class':"product_img"})

if val:
    print(f"{drugname} [ Found ] => https://hatamdrug.com")
else:
    print(f"{drugname} [ Not Found ] => https://hatamdrug.com")







# https://daroodrug.com

daroodrugـpayload = {'searchkey':drugname}
session = requests.Session()
daroodrug_response = session.post('https://daroodrug.com/search.cfm',data=daroodrugـpayload)
daroodrug_soup = BeautifulSoup(daroodrug_response.text,"html.parser")

daroodrug_not_found = daroodrug_soup.find_all('div' , attrs={'class':"s_result"})
daroodrug_found = daroodrug_soup.find_all('div' , attrs={'class':"find_rec"})

if daroodrug_found:
    print(f"{drugname} [ Found ] => https://daroodrug.com")
elif daroodrug_not_found:
    print(f"{drugname} [ Not Found ] => https://daroodrug.com")






#https://darooboom.com

darooboom = requests.get(f"https://darooboom.com/search?controller=search&orderby=position&orderway=desc&search_query={drugname}&submit_search=")

darooboom_soup = BeautifulSoup(darooboom.text,"html.parser")

darooboom_found = darooboom_soup.find_all('div' , attrs={'class':"clearfix selector1"})
darooboom_not_found = darooboom_soup.find_all('small' , attrs={'class':"heading-counter"})
if darooboom_found:
    print(f"{drugname} [ Found ] => https://darooboom.com")
elif darooboom_not_found:
    print(f"{drugname} [ Not Found ] => https://darooboom.com")







# https://daroo.com

daroo = requests.get(f"https://daroo.com/search?keyword={drugname}&sort=7")

daroo_soup = BeautifulSoup(daroo.text,"html.parser")

daroo_not_found = daroo_soup.find_all('div' , attrs={'class':"p-3 rtl text-justify search-p"})
daroo_found = daroo_soup.find_all('div' , attrs={'class':"rate"})
if daroo_found:
    print(f"{drugname} [ Found ] => https://daroo.com")
elif daroo_not_found:
    print(f"{drugname} [ Not Found ] => https://daroo.com")
    
    
    
    

# https://www.daruclick.com
    
daruclick = requests.get(f"https://www.daruclick.com/?s={drugname}")

daruclick_soup = BeautifulSoup(daruclick.text,"html.parser")

daruclick = daruclick_soup.find_all('div' , attrs={'class':"products columns-4"})
daruclick_found = daruclick_soup.find_all('div' , attrs={'class':"item-box fullsize"})
if daruclick_found:
    print(f"{drugname} [ Found ] => https://www.daruclick.com")
elif re.search("محصولی با عبارت مورد نظر شما یافت نشد",str(daruclick)):
    print(f"{drugname} [ Not Found ] => https://www.daruclick.com")

