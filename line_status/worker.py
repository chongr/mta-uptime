import datetime
import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from line_status.models import LineStatus

from django.utils.timezone import utc


ALL_LINES = ["7", "1", "4"]


def populate_line_statuses():
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    LineStatus.objects.bulk_create([
        LineStatus(line_name=line, created_at=now, delayed_time=0) for line in ALL_LINES
    ])


def get_subway_status():
    delayed_lines = []
    sess = HTMLSession()
    mta_status_page = sess.get("https://new.mta.info/")
    # possibly check status with mta_status_page.status_code
    mta_status_page.html.render()
    soup = BeautifulSoup(mta_status_page.html.html)
    # maybe error if this does not exists?
    status_div = soup.find(id='status-subway')
    status_sections = soup.find_all('div', {'class': 'by-status'})

    for status_section in status_sections:
        if "Delays" in status_section.h5.text:
            for line in status_sections[1].ul.children:
                if line.text in ALL_LINES:
                    delayed_lines.append(line.text)

    return delayed_lines



def update_status():
    delayed_lines = get_subway_status()
    for line in delayed_lines:
        obj = LineStatus.objects.get(line_name=line)
        obj.delayed = True
        obj.save()

    for line in [not_delayed_line for not_delayed_line in ALL_LINES if not_delayed_line not in delayed_lines]:
        obj = LineStatus.objects.get(line_name=line)
        obj.delayed = False
        obj.save()

    # TODO: could optimize this queryset bulk update
    # LineStatus.objects.filter(line_name__in=delayed_lines).update(delayed=True)
    # LineStatus.objects.exclude(line_name__in=delayed_lines).update(delayed=False)
