from konlpy.tag import Okt
from rank_bm25 import BM25Okapi
import streamlit as st

class SparseRetriever():
    def __init__(self, corpus, tokenizer=Okt()):
        self.tokenizer = tokenizer
        self.corpus = corpus
        # self.tokenized_corpus = [tokenizer.morphs(text) for text in corpus]
        self.tokenized_corpus = list()
        n = len(corpus)
        my_bar = st.progress(0. , text=f'0 / {n}')
        for i, text in enumerate(corpus):
            my_bar.progress((i+1)/n, text=f'{i+1} / {n}')
            self.tokenized_corpus.append(tokenizer.morphs(text))
        self.bm25 = BM25Okapi(self.tokenized_corpus)
        my_bar.empty()
        
    def retrieve(self, query, k=5):
        tokenized_query = self.tokenizer.morphs(query)
        contexts = self.bm25.get_top_n(tokenized_query, self.corpus, n=k)
        context_scores = []
        for context in contexts:
            tokenized_context = self.tokenizer.morphs(context)
            common_terms = set(tokenized_query).intersection(set(tokenized_context))
            score = len(common_terms) / len(set(tokenized_query).union(set(tokenized_context))) 
            context_scores.append(score)

        # 유사도 점수에 따라 컨텍스트 재정렬
        reranked_contexts = [context for _, context in sorted(zip(context_scores, contexts), key=lambda x: x[0], reverse=True)]
        
        return reranked_contexts