import string
import urllib.request
import urllib.parse

import pandas as pd
from bs4 import BeautifulSoup


def populate_df_with_game_links(df, cdir, sound_track_container):
    for c in sound_track_container.contents:
        if c.name == 'b':
            gname = c.text.strip()
            page_end = c.find('a', href=True)['href']
            page_link = GAME_BROWSE_BASE + page_end
            df = df.append({'name': gname,
                            'page': page_link,
                            'directory': cdir}, ignore_index=True)
    return df


def get_game_list_page(page='http://snesmusic.org/v2/select.php?view=sets&char=n1-9&limit=0'):
    r = urllib.request.urlopen(page)
    soup = BeautifulSoup(r, 'html.parser')
    return soup


def get_container(page_soup):
    return page_soup.find(attrs={'id': 'contContainer'})


def main():
    global GAME_BROWSE_BASE
    GAME_BROWSE_BASE = 'http://snesmusic.org/v2/'
    dirs = ['n1-9'] + list(string.ascii_uppercase)

    game_df = pd.DataFrame(columns=['name', 'page', 'directory'])

    page = get_game_list_page()
    container = get_container(page)
    cdir = dirs.pop(0)
    # http://snesmusic.org/v2/select.php?view=games&char=n1-9&limit=0
    up = urllib.parse.urlsplit('http://snesmusic.org/v2/select.php?view=games&char=n1-9&limit=0')
    query = urllib.parse.parse_qs(up.query)
    query['char'] = dirs.pop()
    game_df = populate_df_with_game_links(game_df, cdir, container)
    main()


if __name__ == '__main__':
    main()