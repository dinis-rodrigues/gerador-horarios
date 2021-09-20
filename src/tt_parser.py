import bs4
import urllib.request, urllib.error, urllib.parse
import urllib.parse
import string
from tt_generator import *

class HTMLCourseParser:

    def __init__(self, url):
        self.url = fix_url(url)

    def parse(self):
        course = Course(extract_name_from_url(self.url))

        html = urllib.request.urlopen(self.url)
        # print(html.read().decode(html.headers.get_content_charset()))
        soup = bs4.BeautifulSoup(html.read().decode(html.headers.get_content_charset()),"html.parser")
        table = soup.body.find('table', attrs={'class' : 'table'})
        rows = table.find_all('tr')
        rows = rows[1:]

        shifts = []
        current_shift = Shift('None')

        for tr in rows:

            tds = tr.find_all('td')

            shift_name = str(tds[0].contents[0].strip())
            shift_time = str(tds[2].contents[0].strip())

            day        = parse_day(shift_time[0:3])
            start      = parse_time(shift_time[5:10])
            end        = parse_time(shift_time[13:])
            room       = str(tds[3].a.contents[0].strip()) \
                           if tds[3].find_all('a') else ""


            if shift_name != current_shift.name:   # new shift
                current_shift = Shift(shift_name)
                shifts.append(current_shift)

            current_shift.add_lesson_slot( \
                LessonSlot(day, start, end, room))


        blocks = {}
        for shift in shifts:
            category = extract_category(course.name, shift.name)
            if not category in list(blocks.keys()):
                blocks[category] = LessonBlock(category)
            blocks[category].add_shift(shift)
        for block in list(blocks.values()):
            course.add_lesson_block(block)

        course.name = course.lesson_blocks[0].shifts[0].name[:len(course.name)]
        course.long_name = str(soup.body.find('h2').contents[0]).strip()

        return course


def extract_category(course_name, shift_name):
    return shift_name[len(course_name) : len(shift_name)-2]

def extract_name_from_url(url):
    splitted = url.split('/')
    return splitted[4]

def parse_day(day):
    dictionary = { 'Mon' : Weekday.MONDAY,
                   'Tue' : Weekday.TUESDAY,
                   'Wed' : Weekday.WEDNESDAY,
                   'Thu' : Weekday.THURSDAY,
                   'Fri' : Weekday.FRIDAY,
                   'Sat' : Weekday.SATURDAY,
                   'Seg' : Weekday.MONDAY,
                   'Ter' : Weekday.TUESDAY,
                   'Qua' : Weekday.WEDNESDAY,
                   'Qui' : Weekday.THURSDAY,
                   'Sex' : Weekday.FRIDAY,
                   'Sab' : Weekday.SATURDAY}
    return dictionary[day[:3]]

def parse_time(time):
    components = time.split(':')
    return Time(int(components[0]), int(components[1]))

def fix_url(url):
    parser = urllib.parse.urlparse(url)
    components = parser.path.split('/')[:5]
    #fixed_path = '/'.join(components) + "/turnos"
    fixed_path = "/".join(components) + "/turnos"
    return urllib.parse.urlunparse(parser[:2] + (fixed_path,) + parser[3:])
