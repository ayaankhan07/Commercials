import os
import re
import sys
import urllib
from urllib import urlencode

import cookielib
import urllib2
import urlparse
import xbmc
import xbmcgui
import xbmcplugin
from urlparse import parse_qsl
import xbmcplugin, xbmcaddon, xbmcgui, xbmc
from random import shuffle

_url = sys.argv[0]
_handle = int(sys.argv[1])

addon = xbmcaddon.Addon()

addon_path = addon.getAddonInfo('path')

__addonname__ = addon.getAddonInfo('id')

__datapath__ = xbmc.translatePath('special://profile/addon_data/' + __addonname__)

avatar = xbmc.translatePath('special://profile/addon_data/' + __addonname__ + '/icon.png')

args = urlparse.parse_qs(sys.argv[2][1:])

Commercials_70 = open(addon_path + "/Links/70's Commercials.txt", "r").read().splitlines()
Commercials_80 = open(addon_path + "/Links/80's Commercials.txt", "r").read().split()
Commercials_90 = open(addon_path + "/Links/90's Commercials.txt", "r").read().split()

commercials_70_list = []
commercials_70_link = []

for row in Commercials_70:
    row = row + "11"
    row = re.findall("https://youtu.be/(.*?)11",row)[0]
    commercials_70_link.append(row)

for row in range(1,61):
    advert_dict = {'name': "",
                   'thumb': "",
                   'video': "",
                   'genre': 'Advert'
                   }
    advert_dict["name"] = "70's Commercials Vol. " + str(row)
    advert_dict["thumb"] = "https://i.ytimg.com/vi/"+ commercials_70_link[row] +"/hqdefault.jpg?sqp=-oaymwEYCKgBEF5IVfKriqkDCwgBFQAAiEIYAXAB&rs=AOn4CLAF3zZbD96XxkpPSvn7qx0lPdwj"
    advert_dict["video"] = commercials_70_link[row]
    commercials_70_list.append(advert_dict)

commercials_80_list = []
commercials_80_link = []

for row in Commercials_80:
    row = row + "11"
    row = re.findall("https://youtu.be/(.*?)11",row)[0]
    commercials_80_link.append(row)

for row in range(1,794):
    advert_dict = {'name': "",
                   'thumb': "",
                   'video': "",
                   'genre': 'Advert'
                   }
    advert_dict["name"] = "80's Commercials Vol. " + str(row)
    advert_dict["thumb"] = "https://i.ytimg.com/vi/"+ commercials_80_link[row] +"/hqdefault.jpg?sqp=-oaymwEYCKgBEF5IVfKriqkDCwgBFQAAiEIYAXAB&rs=AOn4CLAF3zZbD96XxkpPSvn7qx0lPdwj"
    advert_dict["video"] = commercials_80_link[row]
    commercials_80_list.append(advert_dict)

commercials_90_list = []
commercials_90_link = []

for row in Commercials_90:
    row = row + "11"
    row = re.findall("https://youtu.be/(.*?)11",row)[0]
    commercials_90_link.append(row)

for row in range(1,333):
    advert_dict = {'name': "",
                   'thumb': "",
                   'video': "",
                   'genre': 'Advert'
                   }
    advert_dict["name"] = "90's Commercials Vol. " + str(row)
    advert_dict["thumb"] = "https://i.ytimg.com/vi/"+ commercials_90_link[row] +"/hqdefault.jpg?sqp=-oaymwEYCKgBEF5IVfKriqkDCwgBFQAAiEIYAXAB&rs=AOn4CLAF3zZbD96XxkpPSvn7qx0lPdwj"
    advert_dict["video"] = commercials_90_link[row]
    commercials_90_list.append(advert_dict)
VIDEOS = {"70's Commercial": commercials_70_list,
          "80's Commercials": commercials_80_list,
          "90's Commercials": commercials_90_list
          }


def get_url(**kwargs):
    return '{0}?{1}'.format(_url, urlencode(kwargs))


def get_categories():
    return VIDEOS.iterkeys()


def get_videos(category):
    return VIDEOS[category]


def list_categories():
    xbmcplugin.setPluginCategory(_handle, 'Commercials')
    xbmcplugin.setContent(_handle, 'videos')
    categories = get_categories()
    for category in categories:
        list_item = xbmcgui.ListItem(label=category)
        list_item.setArt({
            'thumb': "https://cdn1.iconfinder.com/data/icons/advertising-54/512/TV-advertising-program-commercials-512.png",
            'icon': "https://cdn1.iconfinder.com/data/icons/advertising-54/512/TV-advertising-program-commercials-512.png",
            'fanart': "https://wallpaperset.com/w/full/7/0/e/96090.jpg"})
        list_item.setInfo('video', {'title': category,
                                    'genre': category,
                                    'mediatype': 'video'})
        url = get_url(action='listing', category=category)
        is_folder = True
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    list_item = xbmcgui.ListItem(label='Commercial Shuffle Loop')
    list_item.setInfo('video', {'title': "",
                                'genre': "",
                                'mediatype': 'video'})
    list_item.setArt(
        {'thumb': "https://cdn1.iconfinder.com/data/icons/advertising-54/512/TV-advertising-program-commercials-512.png", 'icon': '', 'fanart': "https://wallpaperset.com/w/full/7/0/e/96090.jpg"})
    list_item.setProperty('IsPlayable', 'true')
    url = "plugin://plugin.video.youtube/play/?playlist_id=PL6676FB688D404E2A"
    is_folder = False
    xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    xbmcplugin.endOfDirectory(_handle)



def list_videos(category):
    xbmcplugin.setPluginCategory(_handle, category)
    xbmcplugin.setContent(_handle, 'videos')
    videos = get_videos(category)
    for video in videos:
        list_item = xbmcgui.ListItem(label='')
        list_item.setInfo('video', {'title': video['name'],
                                    'genre': video['genre'],
                                    'mediatype': 'video'})
        list_item.setArt(
            {'thumb': "", 'icon': video['thumb'], 'fanart': "https://wallpaperset.com/w/full/7/0/e/96090.jpg"})
        list_item.setProperty('IsPlayable', 'true')
        url = "plugin://plugin.video.youtube/?action=play_video&videoid=" + video["video"]
        is_folder = False
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    xbmcplugin.endOfDirectory(_handle)


def play_video(path):
    play_item = xbmcgui.ListItem(path=path)
    xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)


def router(paramstring):
    params = dict(parse_qsl(paramstring))
    if params:
        if params['action'] == 'listing':
            list_videos(params['category'])
        elif params['action'] == 'play':
            play_video(params['video'])
        else:
            raise ValueError('Invalid paramstring: {0}!'.format(paramstring))
    else:
        list_categories()


if __name__ == '__main__':
    router(sys.argv[2][1:])
