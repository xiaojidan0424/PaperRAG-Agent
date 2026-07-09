# 📚 PaperRAG-Agent

## 简介

PaperRAG-Agent 是一个基于 **RAG（Retrieval-Augmented Generation，检索增强生成）** 技术构建的智能论文知识问答系统。

该项目支持用户上传论文 PDF，通过文本解析、语义向量检索以及大语言模型生成，实现论文内容理解、智能问答、论文总结等功能。

主要功能包括：

- 📄 PDF论文解析
- 🔍 语义检索
- 🧠 大模型智能问答
- 📝 论文自动总结
- 📚 多论文知识库管理
- 💬 多轮对话交互
- 📌 回答来源追踪

# 🛠️ 技术架构
Python

├── 文本处理
│ ├── PDF解析
│ └── Section-aware Chunking

├── 向量检索
│ ├── SentenceTransformer
│ └── FAISS

├── 大模型调用
│ └── DeepSeek API

├── Web应用
│ └── Streamlit

└── 项目管理
└── Git
