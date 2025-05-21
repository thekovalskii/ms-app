from fastapi import FastAPI

from src.redis import redis, Product


app = FastAPI()


@app.get('/products')
def all():
    return Product.all_pks()
