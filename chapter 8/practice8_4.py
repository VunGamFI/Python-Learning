def make_shirt(size = 'L', logo = 'I love Python'):
    """制作指定尺寸和文字的衣服"""
    print(f"制作一件尺码为{size}，印上“{logo}”字样的T恤\n")


make_shirt()
make_shirt('M')
make_shirt(logo = '中国', size = 'XL')