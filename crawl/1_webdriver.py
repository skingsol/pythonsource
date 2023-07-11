from chrome import set_chrome_driver # chrome.py에 만들어 놓은 set_chrome_driver 모듈을 사용하겠다는 소리
import time

# 모듈 웹드라이버 사용
driver = set_chrome_driver()
driver.get("https://www.daum.net")
time.sleep(2)
driver.quit()

# ~~~.py : 모듈파일
#          다른 곳에서 모듈 import 후 사용 가능
# ~~~.ipynb : 셀단위로 실행
