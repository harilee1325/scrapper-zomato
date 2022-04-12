from base64 import decodestring
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xlsxwriter 
import itertools
from xlsxwriter.workbook import WorksheetMeta

from xlsxwriter.worksheet import Worksheet  

PATH = "C:\MobileApps\driver\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.zomato.com/bangalore/go-native-hsr-bangalore/order")

workbook = xlsxwriter.Workbook('Go Native hsr.xlsx') 

try:
    print(driver.title)
    driver.implicitly_wait(10) # seconds
    sectionCountArray = []
    menutTitle = driver.find_elements_by_class_name("sc-1hp8d8a-0")
    foodName = driver.find_elements_by_class_name("sc-1s0saks-16")
    actualPrice = driver.find_elements_by_class_name("sc-17hyc2s-0")
    actualPriceBCafe = driver.find_elements_by_class_name("sc-17hyc2s-1")
    tag = driver.find_elements_by_class_name("sc-1tx3445-0")
    description = driver.find_elements_by_class_name("sc-1s0saks-13")
    print (description)

    sections = len(menutTitle)
    for i in range(1,sections+1,1):
        sectionCounts = driver.find_element_by_xpath("//*[@id=\"root\"]/div/main/div/section[4]/section/section[1]/p["+str(i)+"]").text[-3:-1].replace("(", "")
        sectionCountArray.append(int(sectionCounts))

    totalItem = 0
    for items in sectionCountArray:
        totalItem = totalItem + items
    count = 1
    titleCount = 0;
    start = 0
    for title in menutTitle:
        worksheet = workbook.add_worksheet(title.text.replace("/", ","))
        row = 0
        col = 0
        print (start)
        print(sectionCountArray[titleCount])
        for i in range (start, start+sectionCountArray[titleCount], 1):
            worksheet.write(row, col, foodName[i].text)
            worksheet.write(row, col+1, actualPriceBCafe[i].text)
            worksheet.write(row, col+2, description[i].text)
            worksheet.write(row, col+3, tag[i].get_attribute('type')) 
            row +=1
        start = start + sectionCountArray[titleCount]
        titleCount +=1
            # if (i == sectionCountArray[titleCount]):
            #     worksheet.write(row, col, foodName[i].text)
            #     worksheet.write(row, col+1, actualPrice[i].text)
            #     worksheet.write(row, col+2, description[i].text)
            #     worksheet.write(row, col+3, tag[i].get_attribute('type')) 
            #     start = sectionCountArray[titleCount]
            #     titleCount +=1
            #     break
            # else:
            #     worksheet.write(row, col, foodName[i].text)
            #     worksheet.write(row, col+1, actualPrice[i].text)
            #     worksheet.write(row, col+2, description[i].text)
            #     worksheet.write(row, col+3, tag[i].get_attribute('type')) 

        
    workbook.close()   
    #     for (food, price, t, desc) in zip(foodName, actualPrice, tag, description):
    #         if (count+1 == sectionCountArray[titleCount]):
    #             worksheet.write(row, col, food.text)
    #             foodName.remove(food)

    #             worksheet.write(row, col+1, price.text)
    #             actualPrice.remove(price)

    #             worksheet.write(row, col+2, desc.text)
    #             description.remove(desc)

    #             worksheet.write(row, col+3, t.get_attribute('type'))
    #             tag.remove(t)
    #             titleCount +=1
    #             count = 0
    #             break
    #         else:
    #             worksheet.write(row, col, food.text)
    #             foodName.remove(food)

    #             worksheet.write(row, col+1, price.text)
    #             actualPrice.remove(price)

    #             worksheet.write(row, col+2, desc.text)
    #             description.remove(desc)

    #             worksheet.write(row, col+3, t.get_attribute('type'))
    #             tag.remove(t)

    #             count +=1
    #         row +=1    
    # workbook.close() 
    # row = 0
    # col = 0
    # sectionCount = 0
    # worksheetObj = None  
    # #for i in range(0, totalItem, 1):
    # for food in foodName:
    #     print(food.text)
          
    # for (food, price, t, desc) in zip(foodName, actualPrice, tag, description):
        
    #     if (count == 0 ):
    #        # print(menutTitle[sectionCount].text.replace("/", ","))
    #         #print("---------------------------------------------------")
    #         worksheetObj = workbook.get_worksheet_by_name(menutTitle[sectionCount].text.replace("/", ","))    
    #     if (count == sectionCountArray[sectionCount]):
    #         count = 0
    #         row = 0
    #         col = 0
    #         sectionCount+=1
    #         continue
    #     else:
    #         count +=1
    #     worksheetObj.write(row, col, food.text)
    #    # print(food.text+" "+t.get_attribute('type'))
    #     worksheetObj.write(row, col+1, price.text)
    #     worksheetObj.write(row, col+2, desc.text)
    #     worksheetObj.write(row, col+3, t.get_attribute('type'))

    #     row += 1
    # workbook.close()
finally:
    print("finish")
