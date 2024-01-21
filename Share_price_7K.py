def share_price(invested, changes):
    for change in changes:
        invested = invested * (100 + change) / 100.0
    return format(invested, '.2f')


print(share_price(100, []))
print(share_price(100, [-50, 50]))
print(share_price(100, [-20, 30]))
print(share_price(1000, [0, 2, 3, 6]))



















