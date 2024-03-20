def make_album(singer, album_name, num = None):
    """描述音乐专辑的字典"""
    album = {'singer' : singer, 'album name' : album_name}
    if num:
        album['number'] = num
    return album


album_1 = make_album('陈奕迅', 'Solidays', 5)
album_2 = make_album('YuNi', 'Peridot')
album_3 = make_album('李克勤', '30克', 8)

print(album_1)
print(album_2)
print(album_3)