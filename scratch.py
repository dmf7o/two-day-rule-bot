import arrow
import astral
from astral import geocoder, sun
import datetime
import zoneinfo

db = geocoder.database()
city = geocoder.lookup("Moscow", db)
print(city)

golden_hour = sun.golden_hour(
                    city.observer,
                    date=datetime.date(2023, 11, 7),
                    direction=astral.SunDirection.SETTING,
                    tzinfo=city.tzinfo)

time_start = arrow.get(golden_hour[0])

print(time_start)

# при начале диалога по установке - спросить сколько времени сейчас
# сузить круг возможных городов по разнице с UTC и выкатить список, чтобы указать точно
# как вести цепь сообщений
# https://sffjunkie.github.io/astral/package.html#module-astral.geocoder
# https://github.com/arrow-py/arrow/blob/master/docs/guide.rst
# https://stackoverflow.com/questions/48288124/how-to-send-message-in-specific-time-telegrambot


