# from fastapi import FastAPI

# obj=FastAPI()

# @obj.get('/abc')
# def x():
#     return {"name":"sathya"}


# from fastapi import FastAPI
# obj=FastAPI()


# @obj.get("/abc/{a}")
# def x(a:str):
#     return {'name':a}


# from fastapi import FastAPI
# obj=FastAPI()

# @obj.get("/{name}/{age}")
# def x(name:str,age:int):
#     return {'name is':name,"age is ":age }

# query parameter
# from fastapi import FastAPI
# obj=FastAPI()

# @obj.get('/abc')
# def x(name:str,age:int=40):
#     return {'name is':name,'age is ':age}


# from pydantic import BaseModel

# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: bool = None

# @obj.post("/items/")
# def create_item(item: Item):
#     return {"item_name": item.name, "price": item.price}




# from fastapi import FastAPI
# from pydantic import BaseModel
# obj=FastAPI()


# class Family(BaseModel):
#     name: str
#     relation: str
#     age    :int
    
# @obj.post('/family')
# def ab(family:Family):
#     return {"name is ":family.name,"relation is":family.relation,'age is':family.age}

# from typing import Optional
# from pydantic import BaseModel
# from fastapi import FastAPI
# obj=FastAPI()

# class Qt50(BaseModel):
#     name:str
#     age:int
#     city: O    =None
# class Real1(BaseModel):
#     name:str
#     age:int
# @obj.post("/abc",response_model=Real1)
# def x(qt:Qt50):
#     return {"name is":qt.name,'age is':qt.age}



# from typing import Optional
# from pydantic import BaseModel
# from fastapi import FastAPI

# obj = FastAPI()

# class Qt50(BaseModel):
#     name: str
#     age: int
#     city: Optional[str] = None

# class Real1(BaseModel):
#     name: str
#     age: int

# @obj.post("/abc", response_model=Real1)
# def x(qt: Qt50):
#     return {"name": qt.name, "age": qt.age}




# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# # Request model
# class Item(BaseModel):
#     name: str
#     price: float
#     qty: int

# # Fake database
# db = {
#     1: {"name": "Laptop", "price": 60000, "qty": 5}
  
# }
# print(db)

# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     db[item_id] = item.dict()     # Replace entire object
#     return {"message": "Item updated", "new_data": db[item_id]}

# print(db)



# from fastapi import FastAPI
# from fastapi import Depends
# obj=FastAPI()

# def x():
#     return {'a':'abc'}

# @obj.get('/t')
# def y(b:dict=Depends(x)):
#     return{'name is':b}

from fastapi import APIRouter

obj=APIRouter()


@obj.get('/ab')
def x():
    return [1,2,3,4]
