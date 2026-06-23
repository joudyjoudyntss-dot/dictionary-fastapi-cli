from fastapi import FastAPI,HTTPException,status
from typing import List
from app.database import word_db
from app.schemas import wordcreate,wordresponse
app=FastAPI(title='dictionary for API',version='1.0.0')
@app.get('/words',response_model=List[wordresponse],status_code=status.HTTP_200_OK)
def get_all_words():
    return List(word_db.values())
@app.get('/words/{word_name}',response_model=wordresponse)
def get_by_name(word_name:str):
    for item in word_db.values():
        if item['word'].lower()==word_name.lower():
            return item
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'word{word_name}not found in the dictionary'
    )
@app.post('/words',response_model=wordresponse,status_code=status.HTTP_201_CREATED)
def create_word(payload:wordcreate):
    new_id=max(word_db.keys(),default=0)+1
    new_word={
        'id':new_id,
        'word':payload.word.lower(),
        'definition':payload.definition,
        'example':payload.example
    }
    word_db[new_id]=new_word
    return new_word

