import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service





@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will be executing last")

@pytest.fixture()
def DataLoad():
    print("user profile Data is being created")
    return ["rahul", "shetty", "rahulshettyacademy.com"]

@pytest.fixture(params=[("chrome", "rahul", "shetty"), ("Firefox", "rahul"), "IE"])
def crossBrowser(request):
    return request.param

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser addition"
    )


@pytest.fixture(scope="function")
def browserInstance(request):
    global driver
    browser_name = request.config.getoption("--browser_name")


    if browser_name == "chrome":
        options = Options()
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "autofill.profile_enabled": False
        }
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--disable-save-password-bubble")
        options.add_argument("--incognito")
        options.add_argument("--user-data-dir=C:/Temp/ChromeProfile")


        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(10)

    elif browser_name == "firefox":
        service_obj = Service()
        driver = webdriver.Firefox(service=service_obj)
        driver.implicitly_wait(10)

    else:
        raise ValueError("Unsupported browser: {browser_name}")


    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    yield driver #before the test function execution
    driver.quit()  #post your test function execution





@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in HTML report,
    whenever a test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, 'extras', [])

    if report.when == 'call' or report.when == 'setup':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join(os.path.dirname(__file__), 'reports')
            if not os.path.exists(reports_dir):
                os.makedirs(reports_dir)

            file_name = os.path.join(os.path.dirname(item.config.option.htmlpath),
                         report.nodeid.replace("::", "_") + ".png")
            print("file name is " + file_name)

            # Capture screenshot using your custom function
            driver = item.funcargs.get("browserInstance")
            if driver is not None:
                try:
                    driver.save_screenshot(file_name)
                except Exception as e:
                    print(f"Screenshot capture failed: {e}")
                rel_path = os.path.join('reports', os.path.basename(file_name))
                html = (
                    f'<div><img src="{rel_path}" alt="screenshot" '
                    'style="width:304px;height:228px;" onclick="window.open(this.src)" align="right"/></div>'
                )
                extras.append(pytest_html.extras.html(html))
        report.extras = extras


