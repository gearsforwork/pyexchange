from pyexchange import Exchange2010Service, ExchangeNTLMAuthConnection

URL = u'https://mail.vanroey.be/EWS/Exchange.asmx'
USERNAME = u'domain\\yenthe'
PASSWORD = u"superpasswd"
from datetime import datetime
from pytz import timezone





































# Set up the connection to Exchange
connection = ExchangeNTLMAuthConnection(url=URL,
                                        username=USERNAME,
                                        password=PASSWORD)

service = Exchange2010Service(connection)


# You can set event properties when you instantiate the event...
event = service.contact().new_contact(
  subject=u"80s Movie night",
  attendees=[u'yenthe.vanginneken@vanroey.be'],
  location = u"My house",
)

# ...or afterwards
event.start=timezone("US/Pacific").localize(datetime(2015,11,16,15,0,0))
event.end=timezone("US/Pacific").localize(datetime(2015,11,16,21,0,0))

event.html_body = u"""<html>
    <body>
        <h1>80s Movie night</h1>
        <p>We're watching Spaceballs, Wayne's World, and
        Bill and Ted's Excellent Adventure.</p>
        <p>PARTY ON DUDES!</p>
    </body>
</html>"""

# Connect to Exchange and create the event
event.create()
