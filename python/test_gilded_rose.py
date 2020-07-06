# -*- coding: utf-8 -*-
# Will separate each test for each decision
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def test_quality_decreases_by_1(self):
        names_list = ['+5 Dexterity Vest',
                      "Elixir of the Mongoose", "Conjured Mana Cake"]
        items = [Item(name, 45, 45) for name in names_list]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        for item in range(len(items)):
            self.assertEqual(44, items[item].quality)

    def test_sell_in_decreases_by_1(self):
        names_list = ['+5 Dexterity Vest',
                      "Elixir of the Mongoose", "Conjured Mana Cake"]
        items = [Item(name, 45, 45) for name in names_list]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        for item in range(len(items)):
            self.assertEqual(44, items[item].sell_in,
                             f"Item failing {items[0].name}")

    def test_negative_sell_in_returns_0(self):
        names_list = ['+5 Dexterity Vest', "Elixir of the Mongoose",
                      "Sulfuras, Hand of Ragnaros", "Backstage passes to a TAFKAL80ETC concert", "Conjured Mana Cake"]
        items = [Item(name, -1, 0) for name in names_list]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        for item in range(len(items)):
            self.assertEqual(0, items[item].quality)

    def test_quality_cant_increase_more_than_50(self):
        names_list = ['+5 Dexterity Vest', 'Aged Brie', "Elixir of the Mongoose",
                      "Sulfuras, Hand of Ragnaros", "Backstage passes to a TAFKAL80ETC concert", "Conjured Mana Cake"]
        items = [Item(name, 50, 50) for name in names_list]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        for item in range(len(items)):
            self.assertTrue(50 >= items[item].quality)

    def test_representation_of_item(self):
        item = Item("Name", 50, 60)
        self.assertEqual(str(item), "Name, 50, 60")

    # def test_backstage_pass(self):
    #     items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 10)]
    #     gilded_rose = GildedRose(items)
    #     gilded_rose.update_quality()
    #     self.assertEqual(12, items[0].quality)

    def test_backstage_value_at_day_below_eleven(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(12, items[0].quality)

    def test_backstage_value_at_day_below_six(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 3, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(13, items[0].quality)

    def test_backstage_at_day_zero(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_aged_bried_sell_in_is_negative(self):
        items = [Item("Aged Brie", -2, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 12)


if __name__ == '__main__':
    unittest.main()
