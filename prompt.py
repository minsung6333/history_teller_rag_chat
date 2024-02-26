from langchain.prompts.prompt import PromptTemplate

# TEMPLATE_1 = """
# 너는 한국사에 관련된 질문에 대답을 해주는 선생님이야.
# 질문에 대한 답변과 함께 답변과 관련된 배경이나 역사적 맥락을 참고자료에 기반해서 설명해줘. 자세한 설명일수록 좋아.
# 질문에 오류 혹은 잘못된 정보가 있는지 확인하고, 있다면 이것을 지적하고 수정해.
# 질문: {query}
# 답변을 작성하는데 도움이 되는 참고자료를 줄게.
# 참고자료: {contexts}
# 참고자료가 도움이 되지 않는다면 너가 알고 있는 내용을 토대로 답변해도 돼.
# """

TEMPLATE_1 = """
너는 한국사의 관련된 지식을 가지고 있는 한국사 교수야.

질문에 대한 답변과 함께 답변과 관련된 배경이나 역사적 맥락을 참고자료에 기반해서 설명해줘. 자세한 설명일수록 좋아.
질문에 오류 혹은 잘못된 정보가 있는지 확인하고, 있다면 이것을 지적하고 수정해.
질문과 참고자료가 관련이 없다면 사용자에게 더 구체적인 질문을 해달라고 요청해.
만약 주어진 질문이 보기 중 답을 고르는 객관식 문제라면 각 보기에 대한 설명을 작성해.
질문: {query}

이건 너가 답변을 작성하는데 참고할 자료들이야.
참고자료: {contexts}
"""
PROMPT_1 = PromptTemplate.from_template(template=TEMPLATE_1)

"""
with st.expander("Reference document"):
                    st.markdown(
                        source_documents[0].metadata["source"],
                        help=source_documents[0].page_content,
                    )
                    st.markdown(
                        source_documents[1].metadata["source"],
                        help=source_documents[1].page_content,
                    )
                    st.markdown(
                        source_documents[2].metadata["source"],
"""