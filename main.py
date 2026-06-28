import os
from time import sleep
from typing import Coroutine, Any

from playwright.sync_api import Playwright, sync_playwright, expect, Page, Browser, BrowserContext

day: str = os.getenv("DAY_NUM", "29")
center: str = os.getenv("CENTER", "вул. Чупринки, 85 Терпідрозділ ЦНАП")
time_hours: str = os.getenv("TIME_HOUR", "14:30")
phone_number: str = os.getenv("PHONE_NUM", "631111111")
first_name: str = os.getenv("FIRST_NAME", "Плейврайт")
last_name: str = os.getenv("LAST_NAME", "Пайтон")
father_name: str = os.getenv("FATHER_NAME", "Майкрософтович")
contact_email: str = os.getenv("CONTACT_EMAIL", "no@email.com")

def run(playwright: Playwright) -> None:
    browser: Browser = playwright.chromium.launch(headless=False)
    context: BrowserContext = browser.new_context()
    page: Page = context.new_page()
    page.goto("https://cnap_lviv.qsolutions.com.ua:2657/index")
    #Pre-fill in details
    page.get_by_role("textbox", name="Прізвище").fill(last_name)
    page.get_by_role("textbox", name="Ім’я").fill(first_name)
    page.get_by_role("textbox", name="По батькові").fill(father_name)
    page.get_by_role("textbox", name="Email").fill(contact_email)
    page.get_by_role("textbox", name="Номер телефону (+380)").fill(phone_number)
    page.locator(".mat-checkbox-inner-container").first.click()
    page.locator("#mat-checkbox-2 > .mat-checkbox-layout > .mat-checkbox-inner-container").click()
    #Select service group
    page.get_by_role("listbox", name="Група послуг").click()
    page.get_by_role("option", name="Інші послуги").click()
    #Select service
    page.get_by_role("listbox", name="Послуга").click()
    page.get_by_role("option", name="Паспорт громадянина України (ID-картка) / для виїзду за кордон").click()
    #Select a center
    page.get_by_role("listbox", name="Центр").click()
    page.get_by_role("option", name=center).click()
    #Select date
    page.get_by_role("button", name="Open calendar").click()
    page.get_by_text(day, exact=True).click()
    # Select time
    page.get_by_role("listbox", name="Доступний час реєстраціі").click()
    page.get_by_role("option", name=time_hours).get_by_text(time_hours).click()
    page.get_by_role("button", name="Зареєструватися").click()
    sleep(1)
    page.pause()

with sync_playwright() as playwright:
    run(playwright)
