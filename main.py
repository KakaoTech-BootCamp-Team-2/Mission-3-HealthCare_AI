# main.py
import sys, logging
from fastapi import FastAPI
from pydantic import BaseModel

import database
from Food_Classification.FoodClassifier import classify_food

class FoodClassifyQuery(BaseModel):
    image_path: str
    diet_id: int

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(asctime)s - %(message)s')

response_db = database.request_connect_db('mission3')
if (response_db['connect']):
    db = response_db['DB']
else:
    sys.exit(1)


app = FastAPI()

@app.get('/')
async def root():
    return {"message": "Hello, World!"}

@app.post('/classify')
async def classify_router(item: FoodClassifyQuery):
    food = classify_food(item.image_path)

    query = f'INSERT INTO food(diet_id, food_name, created_at, created_by, modified_at, modified_by) VALUES ({item.diet_id}, "{food}", CURDATE(), "system", CURDATE(), "system")'
    db.execute(query)

    return {'message': 'success', 'category': food}
