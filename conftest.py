import pytest
from selenium import webdriver
from datetime import datetime
import os
url =""
@pytest.fixture
def driver:
  driver = webdriver.Chrome()
  driver.implicitly_wait(10)
  yield driver
  driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
  outcome=yield
  result=outcome.get_result()

if result.when =="call" and result.failed:
  driver = item.funcargs.get("driver")
  if driver :
      timestr = datetime.now().strftime("%y_%m_%d_%H_%M_%S)
      screenshots_dir = os.path.join(os.getcwd(),"screenshots")
      os.makedirs(screenshots_dir,exist_ok=True)
      file_name = f"failed_{item.name}_{timestr}.png"
      filepath = os.path.join(screenshots_dir,file_name)
      driver.save_screenshot(filepath)
      pytest_html = item.config.pluginmanager.get_plugin("html")
      if pytest_html:
          extra = getattr(result,"extra",[])
          extra.append(pytest_html.extras.image(filepath)
          result.extra =extra
    
      
