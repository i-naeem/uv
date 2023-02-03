from selenium import webdriver
from selenium.webdriver import EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService


DRIVER_PATH = "./msedgedriver.exe"
START_URL = "https://derajobs.pk"

service = EdgeService(executable_path=DRIVER_PATH)

options = EdgeOptions()
options.add_argument('--log-level=3')
options.add_argument('--inprivate')


driver = webdriver.Edge(service=service, options=options)

driver.get(START_URL)

input("Enter any key to quit...")

driver.close()
