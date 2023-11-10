class Price:
    def __init__(self, ID, currentPrice, updationDate, shopId, goodId):
        self.ID = ID
        self.currentPrice = currentPrice
        self.updationDate = updationDate
        self.shopId = shopId
        self.goodId = goodId

    def __str__(self):
        return f"Price(ID={self.ID}, currentPrice={self.currentPrice}, updationDate={self.updationDate.strftime('%Y-%m-%d')}, shopId={self.shopId}, goodId={self.goodId})"