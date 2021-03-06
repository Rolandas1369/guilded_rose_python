# -*- coding: utf-8 -*-
# 1. replace to shorthand lines item.quality = item.quality - 1
# 2. One function was created before testing.
# 3. After a consideration I need to test code 100% before refractoring.
# 4. After test 100% pass, I need to refactor tests.
# 5. After doing this refactoring a little bit,
# I think in this case rewriting all update quality is good
# 6. Most of code are in functions, not fully tested functionality,
# need improvement to 100% test coverage
# 7. After some code refactoring, and test are 100% passing can add new feature
# 8. GuildedRose class doesnt represent anything, it will be better to remove it and leave only item class


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose:

    def __init__(self, items):
        self.items = items

    def update_min_max_quality(self, item):
        """Updates min and max values of items"""
        if item.quality >= 50:
            item.quality = 50
        if item.quality < 0:
            item.quality = 0
        return item.quality

    def decrease_quality_check_boundaries(self, item):
        """Decreases item value by 1, check for min max values"""
        self.update_min_max_quality(item)
        item.quality -= 1
        return item.quality

    def decrease_sell_in(self, item):
        """Decreases item sell in by 1"""
        item.sell_in -= 1
        return item.sell_in

    def update_aged_brie(self, item):
        """Updates Aged Brie sell in and quality"""
        if item.sell_in < 0:
            item.quality += 2
        return item.quality

    def update_backstage(self, item):
        """Updates Backstage quality"""
        if item.sell_in <= 0:
            item.quality = 0
            return item.quality
        elif item.sell_in < 6:
            item.quality += 3
            return item.quality
        elif item.sell_in < 11:
            item.quality += 2
            return item.quality
        else:
            return item.quality

    def update_conjured(self, item):
        """Updates conjured items sell in and quality"""
        item.quality -= 2
        item.sell_in -= 1
        return item.quality, item.sell_in

    def update_sulfuras(self, item):
        """Update sulfuras sell in"""
        item.sell_in -= 1
        return item.sell_in

    def update_quality(self):
        """Updates quality and sell in of provided item"""
        for item in self.items:
            if item.name == 'Aged Brie':
                self.update_aged_brie(item)
            if item.name == 'Backstage passes to a TAFKAL80ETC concert':
                self.update_backstage(item)
            if item.name == "Conjured Mana Cake":
                self.update_conjured(item)
            if item.name == "Sulfuras, Hand of Ragnaros":
                self.update_sulfuras(item)
            if item.name in ['+5 Dexterity Vest', "Elixir of the Mongoose"]:
                self.decrease_sell_in(item)
                self.decrease_quality_check_boundaries(item)
            if (item.sell_in < 1 or item.quality == 50) and item.name != "Sulfuras, Hand of Ragnaros":
                self.update_min_max_quality(item)



