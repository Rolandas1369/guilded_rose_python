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
    

if __name__ == '__main__':
    unittest.main()
