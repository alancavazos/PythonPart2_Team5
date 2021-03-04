#Imports
from urllib.request import urlretrieve
import re
import datetime

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'
total_requests = 0
year_count = 0

local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE);

FILE_NAME = 'path/to/file'

#counts and matches for dates
oct94_count = 0
nov94_count = 0
dec94_count = 0
jan94_count = 0
feb94_count = 0
mar94_count = 0
apr94_count = 0
may94_count = 0
jun94_count = 0
jul94_count = 0
aug94_count = 0
sep94_count = 0
oct95_count = 0
jan_match = 0
feb_match = 0
mar_match = 0
apr_match = 0
may_match = 0
jun_match = 0
jul_match = 0
aug_match = 0
sep_match = 0
oct_match = 0
oct95_match = 0
nov_match = 0
dec_match = 0

f = open(LOCAL_FILE)    #opens local file
for line in f:          #goes through line by line to check for requests per date
    if 'Oct/1994' in line:
        oct94_count += 1
    elif 'Nov/1994' in line:
        nov94_count += 1
    elif 'Dec/1994' in line:
        dec94_count += 1
    elif 'Jan/1995' in line:
        jan94_count += 1
    elif 'Feb/1995' in line:
        feb94_count += 1
    elif 'Mar/1995' in line:
        mar94_count += 1
    elif 'Apr/1995' in line:
        apr94_count += 1
    elif 'May/1995' in line:
        may94_count += 1
    elif 'Jun/1995' in line:
        jun94_count += 1
    elif 'Jul/1995' in line:
        jul94_count += 1
    elif 'Aug/1995' in line:
        aug94_count += 1
    elif 'Sep/1995' in line:
        sep94_count += 1
    else:
        oct95_count += 1
#Prints request number per month/year
print(f'Oct/1994 requests:', oct94_count)
print(f'Nov/1994 requests:', nov94_count)
print(f'Dec/1994 requests:', dec94_count)
print(f'Jan/1995 requests:', jan94_count)
print(f'Feb/1995 requests:', feb94_count)
print(f'Mar/1995 requests:', mar94_count)
print(f'Apr/1995 requests:', apr94_count)
print(f'May/1995 requests:', may94_count)
print(f'Jun/1995 requests:', jun94_count)
print(f'Jul/1995 requests:', jul94_count)
print(f'Aug/1995 requests:', aug94_count)
print(f'Sep/1995 requests:', sep94_count)
print(f'Oct/1995 requests:', oct95_count)
print()
print()

pages = {}

f = open(LOCAL_FILE)
mon = 0
tue = 0
wed = 0
thur = 0
fri = 0
sat = 0
sun = 0

f = open(LOCAL_FILE)    #opens file
for line in f:
  pieces = re.split('.+ \[(.+) .+\] "[A-Z]{3,4} (.+) HTTP/1.0" ([0-9]{3})', line)   #splits line
  if len(pieces) < 4:
    continue
  date = pieces[1].split(':')
  date = date[0]
  days = datetime.datetime.strptime(date, '%d/%b/%Y')

  weekday = datetime.datetime.weekday(days)

        #counts day of week
  if weekday == 0:
    mon += 1  
  elif weekday == 1:
    tue += 1
  elif weekday == 2:
    wed += 1
  elif weekday == 3:
    thur += 1
  elif weekday == 4:
    fri += 1
  elif weekday == 5:
    sat += 1
  elif weekday == 6:
    sun += 1
        #counts months
  if 'Jan' in line:
      jan_match += 1
  if 'Feb' in line:
      feb_match += 1
  if 'Mar' in line:
      mar_match += 1
  if 'Apr' in line:
      apr_match += 1
  if 'May' in line:
      may_match += 1
  if 'Jun' in line:
      jun_match += 1
  if 'Jul' in line:
      jul_match += 1
  if 'Aug' in line:
      aug_match += 1
  if 'Sep' in line:
      sep_match += 1
  if 'Oct/1994' in line:
      oct_match += 1
  if 'Oct/1995' in line:
      oct95_match += 1
  if 'Nov' in line:
      nov_match += 1
  if 'Dec' in line:
      dec_match += 1

  filename = pieces[2]

  if filename in pages:
    pages[filename] += 1
  else:
    pages[filename] = 1
    
#finds average number of requests per day
ave_mon = mon / 52
ave_tue = tue / 52
ave_wed = wed / 52
ave_thur = thur / 52
ave_fri = fri / 52
ave_sat = sat / 52
ave_sun = sun / 52

#formats output for printing
formatted_mon = "{:.2f}".format(ave_mon)
formatted_tue = "{:.2f}".format(ave_tue)
formatted_wed= "{:.2f}".format(ave_wed)
formatted_thur = "{:.2f}".format(ave_thur)
formatted_fri = "{:.2f}".format(ave_fri)
formatted_sat = "{:.2f}".format(ave_sat)
formatted_sun = "{:.2f}".format(ave_sun)

#prints avg number of requests per day
print(f'The number of requests on Monday averaged {formatted_mon}')
print(f'The number of requests on Tuesday averaged {formatted_tue}')
print(f'The number of requests on Wednesday averaged {formatted_wed}')
print(f'The number of requests on Thursday averaged {formatted_thur}')
print(f'The number of requests on Friday averaged {formatted_fri}')
print(f'The number of requests on Saturday averaged {formatted_sat}')
print(f'The number of requests on Sunday averaged {formatted_sun}')

