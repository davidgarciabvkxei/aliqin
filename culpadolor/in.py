# Import the Options class
from selenium.webdriver.chrome.options import Options

# Create an instance of Options
options = Options()

# Set the headless mode to True
options.headless = True

# Set the window size to 800x600
options.add_argument("--window-size=800,600")

# Set the user agent to "example"
options.add_argument("--user-agent=example")

# Create a Chrome driver with the options
driver = webdriver.Chrome(options=options)

# Navigate to a website
driver.get("https://www.example.com Quit the driver
driver.quit()
