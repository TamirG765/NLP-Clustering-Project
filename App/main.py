# uvicorn main:app --reload
# curl -X GET "http://127.0.0.1:8000/group_paragraphs?groups=2"

import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from embeddings import load_model_and_tokenizer, get_embeddings
from csv_handling import read_preprocess_csv
from clustering import perform_clustering, get_top_words

app = FastAPI()
tokenizer, model = load_model_and_tokenizer()

@app.get("/group_paragraphs")
async def group_paragraphs(groups: int):
    try:
        # Get the directory of the current script
        current_script_path = os.path.dirname(os.path.abspath(__file__))

        # Construct the path to the CSV file
        csv_path = os.path.join(current_script_path, '..', 'data_files', 'normalized_patent_claims.csv')

        # Read and preprocess CSV
        texts = read_preprocess_csv(csv_path)
        
        # Generate embeddings
        embeddings = [get_embeddings(text, tokenizer, model) for text in texts]
        
        # Perform clustering
        labels, counts = perform_clustering(embeddings, groups)
        
        # Get top words for each cluster
        top_words = get_top_words(texts, labels)
        
        # Prepare and send response
        response = [{"title": top_words[i], "number_of_claims": int(counts[i])} for i in range(groups)]
        return JSONResponse(status_code=200, content={"groups": response})
    
    # Error handling
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": str(e)})
