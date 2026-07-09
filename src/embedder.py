from langchain_text_splitters import RecursiveCharacterTextSplitter
import re



def detect_section(text):

    """
    自动检测论文章节
    """

    patterns={

    "Abstract":
    r"abstract",

    "Introduction":
    r"(i\.|1\.|I\.)?\s*introduction",

    "Related Work":
    r"(ii\.|2\.|II\.)?\s*related",

    "Method":
    r"(iii\.|3\.|III\.)?\s*(method|approach|framework)",

    "Experiment":
    r"(iv\.|4\.|IV\.)?\s*(experiment|results)",

    "Conclusion":
    r"(v\.|5\.|V\.)?\s*conclusion"

    }


    for section, pattern in patterns.items():

        if re.search(pattern, text, re.I):

            return section


    return "Unknown"



def split_text(documents):

    """
    Section-aware chunking

    输入:
        PDF Document对象

    输出:
        带章节信息chunk
    """



    splitter = RecursiveCharacterTextSplitter(

        chunk_size=1500,

        chunk_overlap=300,

        separators=[
            "\n\n",
            "\n",
            ". ",
            " "
        ]

    )



    chunks=[]



    for doc in documents:


        text = doc.page_content


        section = detect_section(text)


        splits = splitter.split_text(text)


        for s in splits:


            chunks.append({

                "text": s,

                "section": section,

                "page": doc.metadata.get("page",0)

            })



    return chunks