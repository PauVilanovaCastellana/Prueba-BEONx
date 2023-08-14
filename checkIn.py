from datetime import datetime, date


class CheckIn:
    def __init__(self, check_in: datetime, check_out: datetime, los: int, count: int, 
                 rate_price: float, entity_name: str, entity_latitude: float, entity_longitude: float,
                 entity_city: str, entity_type: str, entity_stars: int, rate_name: str, rate_id: int, adults: int, 
                 children: int, meal_plan: str, currency: str):
        self.check_in =  datetime.strptime(check_in, '%Y-%m-%d').date()
        self.check_out = datetime.strptime(check_out, '%Y-%m-%d').date()
        self.los = int(los)
        self.count = int(count)
        self.rate_price = float(rate_price)
        self.entity_name = entity_name
        self.entity_latitude = float(entity_latitude)
        self.entity_longitude = float(entity_longitude)
        self.entity_city = entity_city
        self.entity_type = entity_type
        self.entity_stars = int(entity_stars)
        self.rate_name = rate_name
        self.rate_id = int(rate_id)
        self.adults = int(adults)
        self.children = int(children)
        self.meal_plan = meal_plan
        self.currency = currency
        
    

