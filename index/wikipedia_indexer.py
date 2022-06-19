from indexer import *
from structure import *

if __name__ == "__main__":
    HTMLIndexer.cleaner = Cleaner(stop_words_file="stopwords.txt",
                        language="portuguese",
                        perform_stop_words_removal=True,
                        perform_accents_removal=True,
                        perform_stemming=False)

    obj_index = HashIndex()
    #obj_index.str_idx_file_name = 'wiki.idx'
    html_indexer = HTMLIndexer(obj_index)
    html_indexer.index_text_dir("index/ri-tp-wiki-data-master")
    