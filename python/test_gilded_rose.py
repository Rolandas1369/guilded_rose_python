# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_check_quantity(self):
        items = [Item("not Sulfuras", 50, 50), Item("Sulfuras, Hand of Ragnaros", 50, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.check_quantity(items[0])
        self.assertEqual(49, items[0].quality)
        self.assertEqual(50, items[1].quality)
    
    def test_sell_in(self):
        items = [Item("not Sulfuras", 50, 50), Item("Sulfuras, Hand of Ragnaros", 50, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(49, items[0].sell_in)

    def test_quality_after_sell_date_expares(self):
        items = [Item("not Sulfuras", -1, 50), Item("Sulfuras, Hand of Ragnaros", 50, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(48, items[0].quality)
    
    def test_negative_quality(self):
        items = [Item("not Sulfuras", -1, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_aged_brie_value(self):
        names_list = ['+5 Dexterity Vest', 'Aged Brie', "Elixir of the Mongoose", "Sulfuras, Hand of Ragnaros", "Backstage passes to a TAFKAL80ETC concert", "Conjured Mana Cake"]
        items = [Item(name, 50, 50) for name in names_list]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        # self.assertEqual(11, items[0].quality)
        for item in range(len(items)):
            self.assertTrue(50 >= items[item].quality)

if __name__ == '__main__':
    unittest.main()
