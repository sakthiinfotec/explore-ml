import chromadb

client = chromadb.Client()
collection = client.create_collection("test")

collection.add(documents=["This is a document-1", "This is a document-2"],
               metadatas=[{"source": "notion"}, {"source": "google-docs"}],
               ids=["doc1", "doc2"]
               )

results = collection.query(query_texts=["This is query document"], n_results=2)

print(results)
