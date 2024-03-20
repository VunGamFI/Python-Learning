def make_album(singer, album_name):
    """描述音乐专辑的字典"""
    album = {'singer' : singer, 'album name' : album_name}
    return album


while True:
    print("\n专辑信息")
    print("（输入'q'退出）")

    singer = input("歌手名：")
    if singer == 'q':
        break

    album_name = input("专辑名：")
    if album_name == 'q':
        break

    album_info = make_album(singer, album_name)

    print(album_info)