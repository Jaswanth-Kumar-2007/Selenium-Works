from Booking.booking import Booking
import time

with Booking() as bot:
    bot.land_first_page()
    time.sleep(3)
    bot.change_currency(currency='USD')
    bot.select_place_to_go('New York')
    bot.select_dates(check_in_date='02-03-2026',check_out_date='12-03-2026')
    bot.select_adults(5)
    bot.click_search()

    bot.apply_filtrations()
    print(len(bot.report_results()))

    bot.refresh() # A workaround to let our bot to grab the data properly
    
    bot.report_results()


    time.sleep(10)    
    bot.quit()