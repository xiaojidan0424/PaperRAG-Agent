import faiss
import numpy as np



def build_vector_store(
        chunks,
        model
):


    texts=[]


    for c in chunks:

        texts.append(
            c["text"]
            if isinstance(c,dict)
            else c
        )


    embeddings=model.encode(
        texts
    ).astype(
        "float32"
    )


    dimension=embeddings.shape[1]


    index=faiss.IndexFlatL2(
        dimension
    )


    index.add(
        embeddings
    )


    return index



def search(
        index,
        query,
        model,
        chunks,
        top_k=5
):


    query_embedding=model.encode(
        [query]
    ).astype(
        "float32"
    )



    distances,indices=index.search(
        query_embedding,
        top_k
    )


    results=[]


    for idx in indices[0]:

        results.append(
            chunks[idx]
        )


    return results