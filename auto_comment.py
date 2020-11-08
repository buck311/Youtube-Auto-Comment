
from selenium import webdriver
from time import sleep

my_user = "<>" #Enter your Email here!
my_pass = "<>" #Enter your password here!
noOfComments = 50
mycomment = "Subscribe to my channel :)"
search_query = "VIDEO" #Enter any keyword without spaces to get type of videos you want to comment on
count = 0

browser = webdriver.Firefox()
browser.get("https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent")

browser.implicitly_wait(1)

browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div[2]/button[1]").click()
browser.implicitly_wait(2)

username_input = browser.find_element_by_css_selector("input[name='identifier']")
browser.implicitly_wait(2)
sleep(3)
username_input.click()
sleep(3)
username_input.send_keys(my_user)
sleep(2)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
print("Entered Username")
sleep(5)
password_input = browser.find_element_by_css_selector(".I0VJ4d > div:nth-child(1) > input:nth-child(1)")
password_input.click()
sleep(2)
password_input.send_keys(my_pass)
sleep(2)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
print("Login Clicked")

sleep(2)
search_url = "https://www.youtube.com/results?search_query=" + search_query 
browser.get(search_url)

print("Searched " + search_query)

sleep(2)
browser.find_element_by_css_selector("ytd-video-renderer.ytd-item-section-renderer:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > h3:nth-child(1)").click()
browser.implicitly_wait(3)

#LOOP
while count < noOfComments:
    browser.execute_script("window.scrollTo(0,0)")
    sleep(2)

    browser.execute_script("window.scrollTo(0, 400)")
    sleep(5)


    commentbox = browser.find_element_by_css_selector("#placeholder-area")
    commentbox.click()
    sleep(2)
    commentInput = browser.find_element_by_css_selector("#contenteditable-root")
    commentInput.click()
    commentInput.send_keys(mycomment)


    sleep(2)

    submitcomment = browser.find_element_by_css_selector("#submit-button > a:nth-child(1) > paper-button:nth-child(1) > yt-formatted-string:nth-child(1)")
    submitcomment.click()

    print("Commented")

    count = count + 1

    print("Commented on Videos: ")
    print(count)

    sleep(2)
    nextvideo = browser.find_element_by_css_selector("ytd-compact-video-renderer.style-scope:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > a:nth-child(1) > h3:nth-child(1)")
    nextvideo.click()
    sleep(5)
    browser.implicitly_wait(4)
    
    print("Next Video Clicked")
