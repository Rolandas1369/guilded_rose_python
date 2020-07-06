# -*- coding: utf-8 -*-
# 1. replace to shorthand lines item.quality = item.quality - 1
# 2. One function was moved before testing.
# 3. After a consideration I need to test code 100% before refractoring.
# 4. After test 100% pass, I need to refactor tests.
# 5. After doing this refactoring a little bit I think in this case rewriting all update quality is good


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    # Aged Brie gets quality up as it gets older
    def decrease_quality(self, item):
        item.quality -= 1
        return item.quality

    def decrease_sell_in(self, item):
        item.sell_in -= 1
        return item.sell_in

    def update_aged_brie(self, item):
        if item.sell_in < 0:
            item.quality += 2
        else:
            item.quality += 1
        return item.quality

    def update_quality(self):

        for item in self.items:
            print("namo", item.name)
            if item.name in ['+5 Dexterity Vest', "Elixir of the Mongoose", "Conjured Mana Cake"]:
                print("name is in this")
                self.decrease_sell_in(item)
                self.decrease_quality(item)

            if item.name == 'Aged Brie':
                self.update_aged_brie(item)

    def update_item(self):
        print('ok')


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
