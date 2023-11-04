from operator import attrgetter


class ContentService:
    
    def filterByEpik(goodsDtos):        
        filtered = [good for good in goodsDtos if "epicentrk" in good.url]
        return filtered
        
    def filterByFora(goodsDtos):        
        filtered = [good for good in goodsDtos if "fora" in good.url]
        return filtered
    
    def filterByEva(goodsDtos):        
        filtered = [good for good in goodsDtos if "eva" in good.url]
        return filtered
    
    def showCurrentPriceByGoodId(prices, productId, shopSort):
    # Filter prices by productId
        filtered_prices = [price for price in prices if price.goodId == productId]

        if shopSort == 'asc':
            # Sort filtered prices by shopId in ascending order
            sorted_prices = sorted(filtered_prices, key=attrgetter('shopId'))
        else:
            # Sort filtered prices by shopId in descending order
            sorted_prices = sorted(filtered_prices, key=attrgetter('shopId'), reverse=True)

        return sorted_prices

        
