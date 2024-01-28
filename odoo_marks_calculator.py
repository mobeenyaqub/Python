import time
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://odoo.cust.edu.pk/web/login")
    page.get_by_role("link", name="MS-SymbolLockup login With Microsoft").click()
    email = input('Enter your email: ').strip()
    password = input('Enter your password: ').strip()
    page.get_by_label("Enter your email, phone, or Skype.").fill(email)
    page.get_by_label("Enter your email, phone, or Skype.").press("Enter")
    time.sleep(2)
    try:
        page.locator("#i0118").fill(password)
        page.locator("#i0118").press("Enter")
        time.sleep(2)
        page.get_by_role("button", name="No").click()
        print('\nProcessing your grades...\n\n')
    except:
        print('\nSeems like an invalid email/password was entered!!\n\n')
        return
    page.wait_for_selector('h6')
    teacher_names = [i.inner_text() for i in page.query_selector_all('h6')]

    for name in teacher_names:
        page.locator(f'text={name}').click()
        page.get_by_role("link", name="Grade Book").click()
        time.sleep(2)
        actual_percentage = [float(i.inner_text().strip().replace(' %', '')) for i in
                             page.query_selector_all('.uk-badge')][1:]
        obtained_percentage = [float(i.inner_text().strip()) for i in page.query_selector_all('td[class=""]')]
        course_title = page.locator('#breadcrumbs li').nth(1).inner_text()
        ans = (f'{sum([actual_percentage[i] * obtained_percentage[i] / 100 for i in range(len(actual_percentage))])}'
               f' / {sum(actual_percentage)}')

        page.get_by_role("link", name="home").click()
        time.sleep(2)
        print(f'{course_title}: {ans}')
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
