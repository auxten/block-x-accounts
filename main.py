#!python3
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from blacklist import BLACKLIST

# 创建 Chrome WebDriver
driver = webdriver.Chrome()

# 打开 Twitter
driver.get("https://www.twitter.com")

# 等待登录成功的元素出现
success_element = WebDriverWait(driver, 100).until(
    EC.presence_of_element_located((By.XPATH, "//a[@href='/compose/tweet']"))
)

# 打开 BLACKLIST 里的相关账号页面，选择 Block
for username in BLACKLIST:
    driver.get("https://twitter.com/" + username)

    # 点击 data-testid="userActions" 的元素
    try:
        user_actions = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@data-testid='placementTracking']"))
        )

        time.sleep(0.5)

        element = driver.find_element(By.XPATH, "//div[@data-testid='placementTracking']")
        span_element = element.find_element(By.XPATH, ".//span")
        if span_element.text == "Blocked" or span_element.text == "已屏蔽":
            print("Already blocked " + username)
            time.sleep(1)
            continue

        user_actions = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@data-testid='userActions']"))
        )
        user_actions.click()
        time.sleep(1)

        # 点击 Block data-testid="block"
        block_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@data-testid='block']"))
        )
        block_button.click()
        time.sleep(1)

        # 点击 Block data-testid="confirmationSheetConfirm" 的确认
        confirm_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@data-testid='confirmationSheetConfirm']"))
        )
        confirm_button.click()
        print("Blocked " + username)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

# 顺便关注一下作者，如果不喜欢请注释掉
try:
    driver.get("https://twitter.com/auxten")
    follow_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@data-testid='placementTracking']"))
    )
    follow_button.click()
    print("Followed @auxten")
    time.sleep(1)
except:
    pass
# 关闭浏览器
driver.quit()
