from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .redis_manager import redis, Product


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
)


def format(pk: str):
    product = Product.get(pk)

    return {
        'id': product.pk,
        'name': product.name,
        'price': product.price,
        'quantity': product.quantity
    }


@app.get('/products')
def all():
    return [format(pk) for pk in Product.all_pks()]


@app.post('/products')
def create(product: Product):
    result = product.save()

    return {
        'id': result.pk,
        'name': result.name,
        'price': result.price,
        'quantity': result.quantity
    }


@app.get('/products/{pk}')
def get(pk: str):
    
    return format(pk=pk)


@app.delete('/products/{pk}')
def delete(pk: str):
    
    return Product.delete(pk=pk)
