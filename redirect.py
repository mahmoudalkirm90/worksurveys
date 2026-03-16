import random
import string
from datetime import datetime
from urllib.parse import quote

# Simulated input data
form_data = {
    'email': 'user@example.com',
    'fname': 'John',
    'lname': 'Doe',
    'state': 'California',  # For UK, this is the city
    'currentRegion': 'UK'   # Change to 'US' or 'UK'
}

# Simulated US states list

# Random string generator
def random_string(length):
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    return ''.join(random.choice(chars) for _ in range(length))

# Random number generator
def random_number(length):
    return ''.join(str(random.randint(0, 9)) for _ in range(length))

usStates = {
  "Alabama": "AL",
  "Alaska": "AK",
  "Arizona": "AZ",
  "Arkansas": "AR",
  "California": "CA",
  "Colorado": "CO",
  "Connecticut": "CT",
  "Delaware": "DE",
  "Florida": "FL",
  "Georgia": "GA",
  "Hawaii": "HI",
  "Idaho": "ID",
  "Illinois": "IL",
  "Indiana": "IN",
  "Iowa": "IA",
  "Kansas": "KS",
  "Kentucky": "KY",
  "Louisiana": "LA",
  "Maine": "ME",
  "Maryland": "MD",
  "Massachusetts": "MA",
  "Michigan": "MI",
  "Minnesota": "MN",
  "Mississippi": "MS",
  "Missouri": "MO",
  "Montana": "MT",
  "Nebraska": "NE",
  "Nevada": "NV",
  "New+Hampshire": "NH",
  "New+Jersey": "NJ",
  "New+Mexico": "NM",
  "New+York": "NY",
  "North+Carolina": "NC",
  "North+Dakota": "ND",
  "Ohio": "OH",
  "Oklahoma": "OK",
  "Oregon": "OR",
  "Pennsylvania": "PA",
  "Rhode+Island": "RI",
  "South+Carolina": "SC",
  "South+Dakota": "SD",
  "Tennessee": "TN",
  "Texas": "TX",
  "Utah": "UT",
  "Vermont": "VT",
  "Virginia": "VA",
  "Washington": "WA",
  "West+Virginia": "WV",
  "Wisconsin": "WI",
  "Wyoming": "WY"
}
ukStates = [
    "England",
    "Scotland",
    "Wales",
    "Northern Ireland",
    "Greater London",
    "West Midlands",
    "Greater Manchester",
    "Merseyside",
    "West Yorkshire",
    "South Yorkshire",
    "Kent",
    "Surrey",
    "Essex",
    "Lancashire",
    "Devon",
    "Cornwall",
    "Norfolk",
    "Suffolk",
    "Cambridgeshire",
    "Oxfordshire",
    "Gloucestershire",
    "Hampshire",
    "Dorset",
    "Somerset",
    "Cheshire",
    "Derbyshire",
    "Nottinghamshire",
    "Leicestershire",
    "Staffordshire",
    "Warwickshire",
    "North Yorkshire",
    "East Yorkshire",
    "South Ayrshire",
    "Highland",
    "Dumfries and Galloway",
    "Tyne and Wear",
    "West Lothian",
    "Fife",
    "Aberdeenshire",
    "Perthshire and Kinross",
    "Moray",
    "Inverclyde",
  ]
# US-specific logic
def go_us(data):
  
    email = data.get('email', '').strip()
    fname = data.get('first_name', '').strip()
    lname = data.get('last_name', '').strip()
    city = data.get('state' , '').strip()
    
    region_code = usStates[city]
    date_str = datetime.now().strftime('%Y-%m-%d')
    transaction_id = "102" + random_string(27)
    ran = random_number(9)

    """link = (
        "https://app.lifepointspanel.com/registration"
        f"?city={city}&country_code=US&date={date_str}&file_id=%7Bfile_id%7D&file_name=&mobile_carrier=%3F"
        f"&ran={ran}&referer=&region_code={region_code}&source=&user_agent={quote('Python/3.x')}"
        "&advertiser_id=1&advertiser_ref=&aff_click_id=&aff_id=1466&aff_sub=&aff_sub2=1098_1_3062"
        f"&aff_sub3={random_string(30)}&aff_sub4=&aff_sub5=&aff_unique1=&aff_unique2=&aff_unique3=&aff_unique4=&aff_unique5="
        "&affiliate_id=1466&affiliate_name=ARROYO&affiliate_ref=617979"
        "&offer_file_id=0&offer_id=1237&offer_name=ARROYO_API_DOI_US_EN_1"
        f"&offer_ref=&offer_url_id=0&transaction_id={transaction_id}"
        "&xp_utm_source=&xp_utm_medium=&xp_utm_campaign=&xp_utm_term="
        f"&title=f&state={region_code}&lang=EN&country=US"
        f"&contactEmail={quote(email)}"
        f"&firstName={quote(fname)}&lastName={quote(lname)}"
        f"&streetAddress=&streetAddress2=&contactCity={city}"
        "&doi_token=MzAwOTUxNmU5NWQ3MzM1MWM3YWJkMzlmYzNhY2QxYjMzMzMwMmJkNzgyNjNkZDJmMDgzODU4Mjc2MTUyMDA1ZA%3D%3D"
    )"""

    link = (
        f"""https://app.lifepointspanel.com/registration?city={city}&country_code=US&date={date_str}&file_id=%7Bfile_id%7D&file_name=&mobile_carrier=%3F&ran={ran}&referer=&region_code={region_code}&source=&user_agent=&advertiser_id=1&advertiser_ref=&aff_click_id=&aff_id=1466&aff_sub=&aff_sub2=1098_4_3692&aff_sub3=10290288fab041f912eb6f14aa92c9&aff_sub4=&aff_sub5=&aff_unique1=&aff_unique2=&aff_unique3=&aff_unique4=&aff_unique5=&affiliate_id=1466&affiliate_name=ARROYO&affiliate_ref=617979&offer_file_id=0&offer_id=1237&offer_name=ARROYO_API_DOI_US_EN_1&offer_ref=&offer_url_id=0&transaction_id={transaction_id}&xp_utm_source=%7BXP_utm_source%7D&xp_utm_medium=%7BXP_utm_medium%7D&xp_utm_campaign=%7BXP_utm_campaign%7D&xp_utm_term=%7BXP_utm_term%7D&title=%7Btitle%7D&state=%7Bstate%7D&lang=EN&country=US&contactEmail={quote(email)}&firstName={quote(fname)}&lastName={quote(lname)}&contactCity={city}"""
    )

    return link
def go_uk(data):
    print(data)
    email = data.get('email', '').strip()
    fname = data.get('first_name', '').strip()
    lname = data.get('last_name', '').strip()
    city = data.get('state' , '').strip().replace(' ','+')
    
    region_code = city[:2].upper()
    date_str = datetime.now().strftime('%Y-%m-%d')
    transaction_id = "102" + random_string(27)
    ran = random_number(9)

    link = (
    f"https://app.lifepointspanel.com/en-gb/registration"
    f"?city={city}&country_code=UK&date={date_str}&file_id={{file_id}}&file_name=&mobile_carrier=att"
    f"&ran={ran}&referer=&region_code={region_code}&source=&user_agent=GuzzleHttp%2F7"
    f"&advertiser_id=1&aff_click_id=&aff_id=1006&aff_sub=4368&aff_unique1=l-e7e7138a-8992-4aab-99b4-238ccfb97fce"
    f"&affiliate_id=1006&affiliate_name=Leadgency+Performance+B.V.&affiliate_ref=624507"
    f"&offer_file_id=0&offer_id=1637&offer_name=LEADGENCY_API_DOI_US_EN_NULL"
    f"&transaction_id={transaction_id}&title=f&state={city}&lang=&country=UK"
    f"&contactEmail={email}&firstName={fname}&lastName={lname}"
    f"&streetAddress={{streetAddress}}&streetAddress2={{streetAddress2}}&contactCity={{contactCity}}"
    f"&doi_token=OTViM2IzM2JkMGY0NzI1MDI2YTlmN2I5MjczZTQwYTJlNDE3YjEyMWQ2NjNjZjA2ZTlmMjUxZmYwNzVkMDA4MQ%3D%3D"
)
    return link

def go_de():
    link = 'https://app.lifepointspanel.com/en-GB/registration?gclsrc=aw.ds&gad_source=1&gad_campaignid=16561899106&gbraid=0AAAAABfNzzOWhT8dFG7JUbNY3iKrb5guw&gclid=EAIaIQobChMIn-aWsfytjwMVzZ6DBx1Wkx52EAAYASAAEgK_2_D_BwE'
    return link
# UK-specific logic
#def go_uk(data):

    email = data.get('email', '').strip()
    fname = data.get('fname', '').strip()
    lname = data.get('lname', '').strip()
    city_raw = data.get('state', '').strip()

    if not all([email, fname, lname, city_raw]):
        raise ValueError("الرجاء إدخال جميع البيانات المطلوبة")

    city = '+'.join(w.capitalize() for w in city_raw.split())
    region_code = city[:2].upper()
    date_str = datetime.now().strftime('%Y-%m-%d')
    transaction_id = "102" + random_string(27)
    ran = random_number(9)

    link = (
        "https://app.lifepointspanel.com/en-gb/registration"
        f"?city={city}&country_code=UK&date={date_str}&file_id=%7Bfile_id%7D&file_name=&mobile_carrier=att"
        f"&ran={ran}&referer=&region_code={region_code}&source=&user_agent=GuzzleHttp%2F7"
        "&advertiser_id=1&aff_click_id=&aff_id=1006&aff_sub=4368"
        "&aff_unique1=l-e7e7138a-8992-4aab-99b4-238ccfb97fce"
        "&affiliate_id=1006&affiliate_name=Leadgency+Performance+B.V.&affiliate_ref=624507"
        "&offer_file_id=0&offer_id=1637&offer_name=LEADGENCY_API_DOI_US_EN_NULL"
        f"&transaction_id={transaction_id}&title=f&state={city}&lang=&country=UK"
        f"&contactEmail={quote(email)}&firstName={quote(fname)}&lastName={quote(lname)}"
        "&streetAddress=%7BstreetAddress%7D&streetAddress2=%7BstreetAddress2%7D&contactCity=%7BcontactCity%7D"
        "&doi_token=OTViM2IzM2JkMGY0NzI1MDI2YTlmN2I5MjczZTQwYTJlNDE3YjEyMWQ2NjNjZjA2ZTlmMjUxZmYwNzVkMDA4MQ%3D%3D"
    )

    return link

# Run the form submission
# req = {
#     'first_name':'mahmoud',
#     'last_name': 'alkirm',
#     'email':'mahmoudalkirm@gmail.com',
#     'state': 'South+Dakota',
# }
# print(go_us(req))
