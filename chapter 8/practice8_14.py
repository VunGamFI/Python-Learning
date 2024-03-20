def make_car(manufacturer, model, **car_info):
    """存储汽车信息"""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info


car_profile = make_car('奥迪', 'e-tron GT',
                         color = '黑色',
                         accessory = '碳纤维车顶')

print(car_profile)