from flask import Flask
import chromadb

app = Flask(__name__)
chroma_client = chromadb.Client()

#Chroma DB using this format to store data into it:
# Collections are where you'll store your embeddings, documents, and any additional metadata. 
# You can create a collection with a name:
collection = chroma_client.create_collection(name="my_collection")

# or if we have embbeded already we can use this code:
# collection.add(
#     embeddings=[[1.2, 2.3, 4.5], [6.7, 8.2, 9.2]],
#     documents=["This is a document", "This is another document"],
#     metadatas=[{"source": "my_source"}, {"source": "my_source"}],
#     ids=["id1", "id2"]
# )

def addChroma(
        documents=["This is a document", "This is another document"], 
        metadatas=[{"source": "my_source"}, {"source": "my_source"}], 
        ids=["id1", "id2"]
    ):
    # embeddings is vectorize result of your document (refer to tf-idf as one of the way to vectorize the data)
    # if you don't provide any embeddings chromadb will automatically doing it for you, isn't great ?
    isValid=False
    try:
        lengthDocuments=len(documents)
        lengthMetadatas=len(metadatas)
        lengthIDs=len(ids)

        isValid=lengthDocuments==lengthMetadatas==lengthIDs
        
        if isValid:
            collection.add(
                documents=documents,
                metadatas=metadatas,
                ids= ids
            )
        
        return isValid
    except:
        print("Error: add data to chroma failed")
        return isValid

def addChromaWithEmbedding(
        documents=["This is a document", "This is another document"], 
        metadatas=[{"source": "my_source"}, {"source": "my_source"}], 
        ids=["id1", "id2"],
        embeddings=[[1.2, 2.3, 4.5], [6.7, 8.2, 9.2]]
    ):
    isValid=False
    try:
        lengthDocuments=len(documents)
        lengthMetadatas=len(metadatas)
        lengthIDs=len(ids)
        lengthEmbeddings=len(embeddings)

        isValid=lengthDocuments==lengthMetadatas==lengthIDs==lengthEmbeddings

        if isValid:
            collection.add(
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
                ids=ids
            )
        return isValid
    except:
        print("Error: add data to chroma with embedding failed")
        return isValid

def queryCollection(query_texts=["This is a query document"], number_of_result=2):
    # by default chromadb will use all-MiniLM-L6-v2 as LLM engine to query the data
    result=[]
    try:
        result=collection.query(
            query_texts=query_texts,
            n_results=number_of_result
        )
    except:
        print("Error: query collection failed")
    
    return result

@app.route("/")
def main():
    result=[]
    isValid=True

    isValid=addChroma()
    if isValid:
        result=queryCollection()

    return result

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 
    #run it by typing "python main.py" in terminal of this root project