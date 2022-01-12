class car:
    def __init__(self, cname, uPrice,qty_hand):
        self.carName=cname
        self.unitPrice=uPrice
        self.qty_hand=qty_hand

class Store:
    def __init__(self, carInventory):
        self.carInventory=carInventory

    def buyItem(self,name,quan_order):
        for i in self.carInventory:
            if i.carName.lower()==name.lower() and i.qty_hand==0:
                return 0
                
            elif i.carName.lower()==name.lower() and i.qty_hand >= quan_order:
                bill= (i.unitPrice*quan_order)
                i.qty_hand =(i.qty_hand- quan_order)
                return bill
                
            elif i.carName.lower()==name.lower() and i.qty_hand < quan_order:
                bill = (i.unitPrice*i.qty_hand)
                i.qty_hand =0
                return bill
        return 0


if __name__ ==  "__main__":
    car1 = []
    n = int(input())
    if(n<0):
        print("Invalid Input")
        exit()
    for i in range(n):
        carName=input()
        unitPrice=int(input())
        stock=int(input())
        car1.append(car(carName, unitPrice,stock))

    b=Store(car1)
    
    dict1={}
    n2=int(input())
    if(n2<0):
        print("Invalid Input")
        exit()
    for i in range(n2):
        preqd=input()
        pqty=int(input())
        if(pqty<0):
            print("Invalid Input")
            exit()
        dict1[preqd]=pqty
    Total = 0
    for i in dict1:
        x=b.buyItem(i,dict1[i])
        Total +=x
        if x==0:
            print(f'{i} is not available')
            
        else:
            print(f'Bill of the item {i} =',x,"Lakh")
    print("Total Amount: ",Total,"Lakh\n")
    
    print('Stock in Hand:')        
    for i in b.carInventory:
        print(i.carName,i.qty_hand)


