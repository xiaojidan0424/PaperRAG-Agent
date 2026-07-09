import streamlit as st
import tempfile

from dotenv import load_dotenv


# ==========================
# Load Environment Variables
# ==========================

load_dotenv()



from sentence_transformers import SentenceTransformer


from src.pdf_loader import load_pdf
from src.embedder import split_text

from src.vector_store import (
    build_vector_store,
    search
)

from src.rag_qa import generate_answer


# ==============================
# 页面配置
# ==============================

st.set_page_config(
    page_title="Multi Paper RAG Assistant",
    page_icon="📚",
    layout="wide"
)


st.title(
    "📚 Multi-Paper RAG Assistant"
)


st.write(
    "Upload papers and ask questions."
)



# ==============================
# Session 初始化
# ==============================


if "index" not in st.session_state:

    st.session_state.index = None



if "chunks" not in st.session_state:

    st.session_state.chunks = []



if "model" not in st.session_state:

    st.session_state.model = None



if "messages" not in st.session_state:

    st.session_state.messages = []



if "summary" not in st.session_state:

    st.session_state.summary = None



# ==============================
# Embedding模型
# ==============================


@st.cache_resource
def load_model():


    return SentenceTransformer(
        "BAAI/bge-small-en"
    )



# ==============================
# 论文总结
# ==============================


def generate_summary(chunks):


    context = "\n\n".join(

        [

            f"""
Paper:
{c.get('paper','Unknown')}

Section:
{c.get('section','Unknown')}


Content:

{c.get('text','')}
"""

            for c in chunks[:20]

        ]

    )



    prompt = f"""

You are an expert academic researcher.

Please summarize the following papers.

Structure:

## 1. Research Motivation

## 2. Main Contributions

## 3. Proposed Method

## 4. Experimental Results

## 5. Conclusion


Paper Content:

{context}

"""



    answer = generate_answer(

        "Summarize this paper",

        prompt

    )


    return answer




# ==============================
# 清空数据库
# ==============================


with st.sidebar:


    st.header(
        "Control"
    )


    if st.button(
        "🗑 Clear Session"
    ):


        st.session_state.index=None

        st.session_state.chunks=[]

        st.session_state.messages=[]

        st.session_state.summary=None


        st.success(
            "Cleared"
        )




# ==============================
# 多论文上传
# ==============================


uploaded_files = st.file_uploader(

    "📄 Upload Papers",

    type=["pdf"],

    accept_multiple_files=True

)




# ==============================
# 构建数据库
# ==============================


if uploaded_files:


    if st.button(
        "🚀 Build Multi-Paper Database"
    ):


        all_chunks=[]


        with st.spinner(
            "Processing papers..."
        ):


            for file in uploaded_files:



                with tempfile.NamedTemporaryFile(

                    delete=False,

                    suffix=".pdf"

                ) as tmp:



                    tmp.write(
                        file.read()
                    )


                    pdf_path=tmp.name




                text=load_pdf(
                    pdf_path
                )


                chunks=split_text(
                    text
                )



                # 添加metadata

                for c in chunks:


                    if isinstance(c,dict):


                        c["paper"]=file.name



                    else:


                        c={

                            "text":c,

                            "paper":file.name,

                            "section":"Unknown",

                            "page":"Unknown"

                        }



                    all_chunks.append(c)





        model=load_model()



        with st.spinner(
            "Building FAISS index..."
        ):



            index=build_vector_store(

                all_chunks,

                model

            )



        st.session_state.index=index

        st.session_state.chunks=all_chunks

        st.session_state.model=model



        st.success(

            f"✅ Loaded {len(uploaded_files)} paper(s)"

        )



        # 清空旧聊天

        st.session_state.messages=[]

        st.session_state.summary=None





# ==============================
# Summary功能
# ==============================


if st.session_state.index is not None:



    st.divider()


    st.subheader(
        "📄 Paper Analysis"
    )


    if st.button(
        "✨ Generate Summary"
    ):



        with st.spinner(

            "Generating summary..."

        ):



            summary=generate_summary(

                st.session_state.chunks

            )


        st.session_state.summary=summary




    if st.session_state.summary:


        st.markdown(
            "## 📑 Paper Summary"
        )


        st.write(

            st.session_state.summary

        )




# ==============================
# Chat历史显示
# ==============================


for message in st.session_state.messages:


    with st.chat_message(

        message["role"]

    ):


        st.markdown(

            message["content"]

        )





# ==============================
# QA
# ==============================


if st.session_state.index is not None:



    query = st.chat_input(

        "Ask something about papers..."

    )



    if query:



        # exit功能

        if query.lower()=="exit":



            st.session_state.messages=[]



            st.success(

                "✅ Conversation ended"

            )


            st.stop()




        # 用户消息


        st.session_state.messages.append(

            {

                "role":"user",

                "content":query

            }

        )



        with st.chat_message(

            "user"

        ):


            st.markdown(query)





        # AI回答


        with st.chat_message(

            "assistant"

        ):



            with st.spinner(

                "Thinking..."

            ):



                results=search(

                    st.session_state.index,

                    query,

                    st.session_state.model,

                    st.session_state.chunks,

                    top_k=8

                )



                context="\n\n".join(

                    [

                        f"""

Paper:
{r.get('paper','Unknown')}


Section:
{r.get('section','Unknown')}


Page:
{r.get('page','Unknown')}


Content:

{r.get('text','')}

"""

                        for r in results

                    ]

                )



                answer=generate_answer(

                    query,

                    context

                )



            st.markdown(

                answer

            )



            st.divider()



            st.markdown(

                "📚 **Sources**"

            )



            for i,r in enumerate(results):


                st.markdown(

                    f"""

**[{i+1}]**

📄 Paper:

`{r.get('paper','Unknown')}`


📌 Section:

`{r.get('section','Unknown')}`


📖 Page:

`{r.get('page','Unknown')}`


"""

                )





        st.session_state.messages.append(

            {

                "role":"assistant",

                "content":answer

            }

        )