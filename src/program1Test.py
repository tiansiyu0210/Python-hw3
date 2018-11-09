import unittest
from src import program1


class Program1Test(unittest.TestCase):
    def test_case_1(self):
        case_1 = program1.StockTrade();
        stock_name = 'test_name_1'
        self.assertEqual(stock_name, case_1.get_stock_name(stock_name))
        case_1.get_info(5, 4, 3, 2, 1)
        self.assertEqual(20, case_1.calculate_paid_stock(case_1.shareBuy, case_1.purchasePrice))
        self.assertEqual(6, case_1.calculate_sold_stock(case_1.shareSold, case_1.sellingPrice))
        self.assertEqual(-14.26,
                         case_1.calculate_profit(case_1.calculate_sold_stock(case_1.shareSold,case_1.sellingPrice),
                                                  case_1.calculate_paid_stock(case_1.shareBuy, case_1.purchasePrice),
                                                  case_1.calculate_paid_commission(float(case_1.commission), case_1.calculate_paid_stock(case_1.shareBuy, case_1.purchasePrice)),
                                                  case_1.calculate_sold_commission(float(case_1.commission), case_1.calculate_sold_stock(case_1.shareSold,case_1.sellingPrice))))
        
    def test_case_2(self):
        case_2 = program1.StockTrade();
        stock_name = 'test_name_1'
        self.assertEqual(stock_name, case_2.get_stock_name(stock_name))
        case_2.get_info(6, 5, 4, 3, 2)
        self.assertEqual(30, case_2.calculate_paid_stock(case_2.shareBuy, case_2.purchasePrice))
        self.assertEqual(12, case_2.calculate_sold_stock(case_2.shareSold, case_2.sellingPrice))
        self.assertEqual(-18.84,
                         case_2.calculate_profit(case_2.calculate_sold_stock(case_2.shareSold,case_2.sellingPrice),
                                                  case_2.calculate_paid_stock(case_2.shareBuy, case_2.purchasePrice),
                                                  case_2.calculate_paid_commission(float(case_2.commission), case_2.calculate_paid_stock(case_2.shareBuy, case_2.purchasePrice)),
                                                  case_2.calculate_sold_commission(float(case_2.commission), case_2.calculate_sold_stock(case_2.shareSold,case_2.sellingPrice))))

    def test_case_3(self):
        case_3 = program1.StockTrade();
        stock_name = 'test_name_1'
        self.assertEqual(stock_name, case_3.get_stock_name(stock_name))
        case_3.get_info(7,6,5,4,3)
        self.assertEqual(42, case_3.calculate_paid_stock(case_3.shareBuy, case_3.purchasePrice))
        self.assertEqual(20, case_3.calculate_sold_stock(case_3.shareSold, case_3.sellingPrice))
        self.assertEqual(-23.86,
                         case_3.calculate_profit(case_3.calculate_sold_stock(case_3.shareSold,case_3.sellingPrice),
                                                  case_3.calculate_paid_stock(case_3.shareBuy, case_3.purchasePrice),
                                                  case_3.calculate_paid_commission(float(case_3.commission), case_3.calculate_paid_stock(case_3.shareBuy, case_3.purchasePrice)),
                                                  case_3.calculate_sold_commission(float(case_3.commission), case_3.calculate_sold_stock(case_3.shareSold,case_3.sellingPrice))))

    def test_case_4(self):
        case_4 = program1.StockTrade();
        stock_name = 'test_name_1'
        self.assertEqual(stock_name, case_4.get_stock_name(stock_name))
        case_4.get_info(8,7,6,5,4)
        self.assertEqual(56, case_4.calculate_paid_stock(case_4.shareBuy, case_4.purchasePrice))
        self.assertEqual(30, case_4.calculate_sold_stock(case_4.shareSold, case_4.sellingPrice))
        self.assertEqual(-29.44,
                         case_4.calculate_profit(case_4.calculate_sold_stock(case_4.shareSold,case_4.sellingPrice),
                                                  case_4.calculate_paid_stock(case_4.shareBuy, case_4.purchasePrice),
                                                  case_4.calculate_paid_commission(float(case_4.commission), case_4.calculate_paid_stock(case_4.shareBuy, case_4.purchasePrice)),
                                                  case_4.calculate_sold_commission(float(case_4.commission), case_4.calculate_sold_stock(case_4.shareSold,case_4.sellingPrice))))

    def test_case_5(self):
        case_5 = program1.StockTrade();
        stock_name = 'test_name_1'
        self.assertEqual(stock_name, case_5.get_stock_name(stock_name))
        case_5.get_info(9,8,7,6,5)
        self.assertEqual(72, case_5.calculate_paid_stock(case_5.shareBuy, case_5.purchasePrice))
        self.assertEqual(42, case_5.calculate_sold_stock(case_5.shareSold, case_5.sellingPrice))
        self.assertEqual(-35.70,
                         case_5.calculate_profit(case_5.calculate_sold_stock(case_5.shareSold,case_5.sellingPrice),
                                                  case_5.calculate_paid_stock(case_5.shareBuy, case_5.purchasePrice),
                                                  case_5.calculate_paid_commission(float(case_5.commission), case_5.calculate_paid_stock(case_5.shareBuy, case_5.purchasePrice)),
                                                  case_5.calculate_sold_commission(float(case_5.commission), case_5.calculate_sold_stock(case_5.shareSold,case_5.sellingPrice))))


if __name__ == '__main__':
    unittest.main()
    p1t= Program1Test()
    p1t.test_case_1()
    p1t.test_case_2()
    p1t.test_case_3()
    p1t.test_case_4()
    p1t.test_case_5()
