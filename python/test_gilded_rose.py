# -*- coding: utf-8 -*-
# Will separate each test for each decision
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    @staticmethod
    def create_update_items(items_list, sell_in, quality):
        """Creates items with sell in and quality from provided names list"""
        items = [Item(items_list[i], sell_in, quality) for i in range(len(items_list))] 
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        return items

    def test_quality_decreases_by_1(self):
        names_list = ['+5 Dexterity Vest',
                      "Elixir of the Mongoose"]
        items = self.create_update_items(names_list, 45, 45)
        for item in range(len(names_list)):
            self.assertEqual(44, items[item].quality)

    def test_sell_in_decreases_by_1(self):
        names_list = ['+5 Dexterity Vest', "Sulfuras, Hand of Ragnaros",
                      "Elixir of the Mongoose", "Conjured Mana Cake"]
        items = self.create_update_items(names_list, 45, 45)
        for item in range(len(items)):
            self.assertEqual(44, items[item].sell_in,
                             f"Item failing {items[item].name}")

    def test_negative_sell_in_returns_0(self):
        names_list = ['+5 Dexterity Vest', "Elixir of the Mongoose",
                      "Backstage passes to a TAFKAL80ETC concert", "Conjured Mana Cake"]
        items = self.create_update_items(names_list, -1, 0)
        for item in range(len(items)):
            self.assertEqual(0, items[item].quality, f"Testing item {items[item].name}")

    def test_quality_cant_increase_more_than_50(self):
        names_list = ['+5 Dexterity Vest', 'Aged Brie', "Elixir of the Mongoose",
                      "Backstage passes to a TAFKAL80ETC concert", "Conjured Mana Cake"]
        items = self.create_update_items(names_list, 50, 50)
        for item in range(len(items)):
            self.assertTrue(50 >= items[item].quality,
                            f"Item failing {items[item].name}")

    def test_representation_of_item(self):
        item = Item("Name", 50, 60)
        self.assertEqual(str(item), "Name, 50, 60")

    def test_backstage_value_at_day_below_eleven(self):
        names_list = ["Backstage passes to a TAFKAL80ETC concert"]
        items = self.create_update_items(names_list, 10, 10)
        self.assertEqual(12, items[0].quality)

    def test_backstage_value_at_day_below_six(self):
        names_list = ["Backstage passes to a TAFKAL80ETC concert"]
        items = self.create_update_items(names_list, 3, 10)
        self.assertEqual(13, items[0].quality)

    def test_backstage_at_day_zero(self):
        names_list = ["Backstage passes to a TAFKAL80ETC concert"]
        items = self.create_update_items(names_list, 0, 10)
        self.assertEqual(0, items[0].quality)

    def test_aged_bried_sell_in_is_negative(self):
        names_list = ["Aged Brie"]
        items = self.create_update_items(names_list, -2, 10)
        self.assertEqual(items[0].quality, 12)
    
    def test_cojured_item_quality_decreases_by_two(self):
        names_list = ["Conjured Mana Cake"]
        items = self.create_update_items(names_list, 10, 10)
        self.assertEqual(items[0].quality, 8)

    def test_sulfuras_quality_doesnt_change(self):
        names_list = ["Sulfuras, Hand of Ragnaros"]
        items = self.create_update_items(names_list, -1, 80)
        self.assertEqual(items[0].quality, 80)


if __name__ == '__main__':
    unittest.main()
