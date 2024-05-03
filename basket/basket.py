    


class Basket():
    
    def __init__(self,request):
        
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket    
        
        
    def add(self,car_detail):
        
        """  
        Adding and updating the users basket session data
        """ 
        car_id = car_detail.id
        
        if car_id not in self.basket:
            self.basket[car_id] = {'price':str(car_detail.price_car)}
            
            
        self.session.modified = True  
        
           
        
        
        