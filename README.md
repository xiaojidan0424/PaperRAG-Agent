```markdown
# 📚 PaperRAG-Agent

<div align="center">

**An Intelligent Academic Paper Assistant Based on Retrieval-Augmented Generation (RAG)**

Support multi-paper retrieval, citation-aware question answering and automatic paper summarization.

</div>


---

## 📌 Overview

PaperRAG-Agent is an intelligent academic paper assistant built with **Retrieval-Augmented Generation (RAG)** technology.

The system allows users to upload one or multiple research papers, automatically analyze and index the documents, and interact with them through natural language questions.

Different from traditional document question-answering systems, PaperRAG-Agent introduces:

- Section-aware document chunking
- Dense semantic retrieval based on BGE embedding
- FAISS vector database
- Citation-aware response generation
- Multi-paper knowledge retrieval
- Automatic academic paper summarization


The system is designed for researchers and students who need to efficiently understand and analyze large-scale academic literature.


---

# ✨ Features


## 1. 📄 Multi-paper Upload

Support uploading multiple academic papers simultaneously.

Example:

```

Mamba.pdf
TransFG.pdf
AA-Trans.pdf

```

The system automatically:

```

PDF
↓
Text Extraction
↓
Chunking
↓
Embedding
↓
FAISS Index
↓
Retrieval

````


---

## 2. 🧩 Section-aware Chunking

Instead of naive character-level splitting, PaperRAG-Agent preserves academic paper structures.

The system extracts:

- Abstract
- Introduction
- Methodology
- Experiments
- Conclusion


Each chunk maintains metadata:

```json
{
    "paper": "Mamba.pdf",
    "section": "Method",
    "page": 5,
    "text": "..."
}
````

This improves retrieval accuracy for academic queries.

---

## 3. 🔎 Semantic Retrieval

The system uses:

* BGE-small embedding model
* FAISS vector database

Workflow:

```
User Query

      ↓

Query Embedding

      ↓

FAISS Similarity Search

      ↓

Top-K Relevant Chunks

      ↓

LLM Generation
```

---

## 4. 🤖 RAG-based Question Answering

The retrieved paper contents are provided as context to the LLM.

Example:

Question:

```
What is the main contribution of this paper?
```

Answer:

```
The paper proposes a multi-domain feature enhancement framework...
```

The model is instructed to only answer based on retrieved documents to reduce hallucination.

---

## 5. 📑 Automatic Paper Summarization

The system provides:

```
✨ Generate Summary
```

Automatically generates:

### Research Motivation

### Main Contributions

### Proposed Method

### Experimental Results

### Conclusion

---

## 6. 📚 Citation-aware Generation

Each answer provides source information:

Example:

```
Sources:

[1]

Paper:
Mamba.pdf

Section:
Method

Page:
6
```

Users can trace answers back to the original paper.

---

## 7. 💬 Multi-turn Conversation

Support continuous academic discussion:

Example:

```
User:
What is MBEM?


AI:
MBEM is a multi-branch enhancement module...


User:
What are its advantages?


AI:
Based on the previous context...
```

Input:

```
exit
```

to terminate the current conversation.

---

# 🏗 System Architecture

```
              User

               |
               |

        Streamlit Interface

               |

               |

        PDF Document Loader

               |

               |

      Section-aware Chunking

               |

               |

        BGE Embedding Model

               |

               |

       FAISS Vector Database

               |

               |

        Similarity Retrieval

               |

               |

       DeepSeek LLM Generation

               |

               |

        Final Answer + Citation

```

---

# 🛠 Tech Stack

## Programming Language

* Python

## Frontend

* Streamlit

## Document Processing

* PyPDF

## Embedding Model

* BAAI/bge-small-en

## Vector Database

* FAISS

## Large Language Model

* DeepSeek API

## Framework

* LangChain

---

# 📂 Project Structure

```
PaperRAG-Agent

│
├── app.py                    # Streamlit application

│
├── requirements.txt          # Dependencies

│
├── .env.example              # API configuration template

│
├── src

│   ├── pdf_loader.py         # PDF parsing

│   │

│   ├── embedder.py           # Chunking and embedding

│   │

│   ├── vector_store.py       # FAISS retrieval

│   │

│   └── rag_qa.py             # LLM generation

│
├── data

│   └── README.md             # PDF storage instruction

│
└── cache

    └── .gitkeep

```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/xiaojidan0424/PaperRAG-Agent

cd PaperRAG-Agent
```

---

## 2. Create Environment

```bash
conda create -n paperrag python=3.10

conda activate paperrag
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 API Configuration

Create:

```
.env
```

Add your DeepSeek API key:

```env
DEEPSEEK_API_KEY=your_api_key
```

---

# 🚀 Run

Start Streamlit:

```bash
streamlit run app.py
```

Open browser:

```
http://localhost:8501
```

---

# 📖 Usage

## Step 1

Upload papers:

```
Upload Papers

↓

Select PDF files
```

---

## Step 2

Build knowledge base:

```
🚀 Build Multi-Paper Database
```

---

## Step 3

Ask questions:

Example:

```
What is the main contribution of this paper?
```

```
Compare the methods of these papers.
```

```
Explain the proposed architecture.
```

---

# 🎯 Example Applications

## Literature Review

Quickly understand multiple papers.

## Method Comparison

Compare different approaches.

## Paper Reading Assistant

Ask questions without manually searching PDFs.

---

# 🔮 Future Improvements

Possible extensions:

* Hybrid Retrieval (BM25 + Dense Retrieval)

* Query Rewrite

* Conversation Memory

* Knowledge Base Management

* Agent-based workflow

* Local LLM deployment

---

# 📌 Resume Description

**PaperRAG-Agent: Intelligent Academic Paper Assistant Based on RAG**

* Developed a Retrieval-Augmented Generation (RAG) system for academic paper understanding using Python, FAISS, BGE Embedding and DeepSeek LLM.
* Implemented multi-paper document retrieval with section-aware chunking and metadata-based citation tracking.
* Built a Streamlit interactive interface supporting paper summarization, multi-turn question answering and knowledge retrieval.
