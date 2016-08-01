import os
import sys
import urllib
import urlparse
import xbmcgui
import xbmcplugin
import xbmcaddon

def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
#
args = urlparse.parse_qs(sys.argv[2][1:])
mode = args.get('mode', None)
#
addon = xbmcaddon.Addon()
pwd = addon.getAddonInfo('path')
#
xbmcplugin.setContent(addon_handle, 'movies')
if mode is None:
	with open(os.path.join(pwd, 'data/cat_list.txt'), 'r') as fin:
		for i in fin:
			if i.startswith('Y'):
				Y, cat, sym = i.split()
				url = build_url({'mode': 'folder', 'foldername': cat,
					'symbol': sym })
				li = xbmcgui.ListItem(cat, iconImage=pwd+'/'+'icon.png')
				xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
						listitem=li, isFolder=True)
	xbmcplugin.endOfDirectory(addon_handle)
elif mode[0] == 'folder':
	foldername = args['foldername'][0]
	symbol = args['symbol'][0]
	print 'cat='+foldername+' symbol='+symbol
	#
	tv_listing = []
	with open(os.path.join(pwd, 'data/tv_list.txt'), 'r') as fin:
		for i in fin:
			if i and i[0].isalpha():
				id_, label, url = i.split()
				if symbol in id_ and 'N' not in id_:
					tv_listing.append([label, url])
	tv_listing.sort()
	for i in tv_listing:
		li = xbmcgui.ListItem(i[0], iconImage='icon.png')
		xbmcplugin.addDirectoryItem(handle=addon_handle, url=i[1],
				listitem=li)
	xbmcplugin.endOfDirectory(addon_handle)
