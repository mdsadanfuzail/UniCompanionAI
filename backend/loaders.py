from langchain_community.document_loaders import Docx2txtLoader
from langchain_text_splitters.markdown import MarkdownHeaderTextSplitter
from langchain_text_splitters.character import CharacterTextSplitter

def initial_load_and_split(docx_file):

    loader_docx = Docx2txtLoader(docx_file)
    pages = loader_docx.load()
    
    md_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on = [("#", "All courses"),
                           ("##", "Course Title"), 
                           ("###", "Unit Title")]
    )

    pages_md_split = md_splitter.split_text(pages[0].page_content)

    for i in range(len(pages_md_split)):
        pages_md_split[i].page_content = ' '.join(pages_md_split[i].page_content.split())

    char_splitter = CharacterTextSplitter(separator = '', chunk_size = 150, chunk_overlap = 20)

    pages_char_split = char_splitter.split_documents(pages_md_split)

    return pages_char_split