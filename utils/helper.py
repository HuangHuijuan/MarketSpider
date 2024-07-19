def getPriceTag(item_name, price):
    tag = '-'
    if '蒸' in item_name:
        if '12' in item_name and price < 650:
            tag = '低价'
        if '20' in item_name and price < 1300:
            tag = '低价'
        if '24' in item_name and price < 1000:   
            tag = '低价'
        if '32' in item_name and price < 1500:   
            tag = '低价'
    return tag