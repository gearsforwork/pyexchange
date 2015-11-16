from pyexchange import Exchange2010Service, ExchangeNTLMAuthConnection

URL = u'https://mail.vanroey.be/EWS/Exchange.asmx'
USERNAME = u'DOMAIN\\yenthe'
PASSWORD = u"mypass"
from datetime import datetime
from pytz import timezone





































# Set up the connection to Exchange
connection = ExchangeNTLMAuthConnection(url=URL,
                                        username=USERNAME,
                                        password=PASSWORD)

service = Exchange2010Service(connection)


# You can set event properties when you instantiate the event...
contact = service.contact().new_contact(
  name=u"80s Movie night",
  company_name = u"My house",
)

# ...or afterwards
contact.name = u"Yenthe"
contact.company_name = u"Van Roey"

# Connect to Exchange and create the event
contact.create()
