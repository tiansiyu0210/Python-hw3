class StockTrade:

    def __init__(self):
        self.stockName = ''
        self.shareBuy = 0
        self.shareSold = 0
        self.purchasePrice = 0.0
        self.sellingPrice = 0.0
        self.commission = 0.0
        self.paidStock = 0.0
        self.paidCommission = 0.0
        self.soldStock = 0.0
        self.soldCommission = 0.0
        self.profit = 0.0


    def get_stock_name(self, stockname:str) -> (str):
        self.stockName = stockname
        return self.stockName

    def get_info(self, share_buy:int, purchase_price:float, share_sold:int, selling_price:float, broker_commission:float):
        self.shareBuy = share_buy
        self.purchasePrice = purchase_price
        self.shareSold = share_sold
        self.sellingPrice = selling_price
        self.commission = broker_commission

    def calculate_paid_stock(self, share_buy: int, purchase_price: float) -> float:
        self.paidStock = share_buy * purchase_price
        return self.paidStock

    def calculate_paid_commission(self, broker_commission: float, paid_stock: float) -> float:
        self.paidCommission = broker_commission * paid_stock/100
        return self.paidCommission

    def calculate_sold_stock(self, share_sold: int, selling_price: float) -> float:
        self.soldStock = share_sold * selling_price
        return self.soldStock

    def calculate_sold_commission(self, broker_commission: float, sold_stock: float) -> float:
        self.soldCommission = broker_commission * sold_stock/100
        return self.soldCommission

    def calculate_profit(self, sold_stock: float, paid_stock: float, paid_commission: float, sold_commission: float) -> float:
        self.profit = round(sold_stock - paid_stock - paid_commission - sold_commission, 2)
        return self.profit;

    def print_state(self, profit: float):
        print("the profit is ${:.2f}".format(profit))



if __name__ == '__main__':
    stockList = []
    print("Welcome!")
    while True:

        joe_trade = StockTrade()
        stockName = input("please enter the stock name(enter [!] to quit stock system)")
        joe_trade.get_stock_name(stockName)

        if joe_trade.stockName == '':
            print("the stock name cannot empty, please re-enter the stock name")
            continue
        elif joe_trade.stockName == '!':
            print('Printing transaction.....')
            print("=============================================")
            break

        shareBuy = input("please enter the share Joe bought")
        purchasePrice = input("please enter the purchase price")
        shareSold = input("please enter the share Joe sold")
        sellingPrice = input("please enter the selling price")
        commission = input("please enter the broker commission")
        joe_trade.get_info(shareBuy, purchasePrice, shareSold, sellingPrice, commission)

        #the money you got after selling stock
        soldStock = joe_trade.calculate_sold_stock(int(shareSold), float(sellingPrice))
        # the money you spend after buying stock
        paidStock = joe_trade.calculate_paid_stock(int(shareBuy), float(purchasePrice))

        # profit you got after paid commission
        profit = joe_trade.calculate_profit(soldStock,
                                   paidStock,
                                   joe_trade.calculate_paid_commission(float(commission), paidStock),
                                   joe_trade.calculate_sold_commission(float(commission), soldStock)
                                   );

        joe_trade.print_state(float(profit));

        #save stock transcation into a list
        stockList.append(joe_trade);

    for stock in stockList:
        print("Stock name is [{}]".format(stock.stockName))
        print("you brought [{}] shares at [${:.2f}]".format(stock.shareBuy, float(stock.purchasePrice)))
        print("you sold [{}] shares at [${:.2f}]".format(stock.shareSold, float(stock.sellingPrice)))
        print("commission for broker is [{:.2f}]%". format(float(stock.commission)))
        print("you total profit for this transaction is [${:.2f}]".format(float(stock.profit)))

    print('Goodbye')