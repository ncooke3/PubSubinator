from selenium import webdriver


chromedriver = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.get("http://www.publix.com/products-services/deli/online-easy-ordering")

LogIn = driver.find_element_by_xpath("//*[@id='pblx-user']/a[1]").click()

email = driver.find_element_by_xpath("//*[@id='ctl00_DesktopView_txtLoginId']")
email.send_keys("**************")
email.send_keys("\ue004") #tab key



password = driver.find_element_by_xpath("//*[@id='ctl00_DesktopView_txtPassword']")
password.send_keys("********")

button = driver.find_element_by_xpath("//*[@id='ctl00_DesktopView_btnLogin']").click()

expected = "https://www.publix.com/products-services/deli/online-easy-ordering"

if (driver.current_url == expected):
    print("login success!")

else:
    print("login failed...")

### should be logged in at this point

startOrder = driver.find_element_by_xpath("//*[@id='main-content']/div[3]/div[2]/p[3]/a").click()

deli = driver.find_element_by_xpath("//*[@id='content_1_3fourthswidth2colright_4_LinksRepeater_LinkURL_1']/div/div/h3").click()

subs = driver.find_element_by_xpath("//*[@id='content_1_3fourthswidth2colright_4_LinksRepeater_LinkURL_0']/div/div/h3").click()

### falcons sub

riseup = driver.find_element_by_xpath("//*[@id='content_2_3fourthswidth2colright_1_LinksRepeater_ProductResultsDetail_0_ProductAddToCart_0_BuildMyProductButtonQV_0']").click()

whole = driver.find_element_by_xpath("//*[@id='content_1_3fourthswidth2colright_1_ProductQuantity_RadioButtonSection2']/div/span").click()

buildNow = driver.find_element_by_xpath("//*[@id='content_1_3fourthswidth2colright_1_ProductAddToCart_BuildMyProductButton']").click()

bread = driver.find_element_by_xpath("//*[@id='content_1_BuildSubRepeater_SectionHeader_0']/div[2]/div/span").click()

noThanks = driver.find_element_by_xpath("//*[@id='content_1_ComboSelection']/div[1]/div[2]/div[2]/div/span").click()

instr = driver.find_element_by_xpath("//*[@id='content_1_instructions']")
instr.send_keys("Thank you & have a wonderful day! Rise Up! <3")

addToOrder = driver.find_element_by_xpath("//*[@id='content_1_MyOrderButton']").click()

firstAvailable = driver.find_element_by_xpath("//*[@id='firstAvailableBtn']").click()

payInStore = driver.find_element_by_xpath("//*[@id='payInStoreLi']/div/span").click()

ans = input("Would you like to submit your order? Type 'yes' or 'no'")

if (ans == yes):
    submitOrder = driver.find_element_by_xpath("//*[@id='btnSubmitOrder']").click()
else:
    print("Order canceled!")

driver.close()
driver.quit()

