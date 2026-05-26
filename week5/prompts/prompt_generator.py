from langchain_core.prompts import PromptTemplate

# prompt Template
template=PromptTemplate(
    template='''Please summarize the research paper titled {paper_input} with the following specifications: Explanation style: {style_input} and Explanation length: {length_input}. Include relevant mathematical equations if present in the paper. Explain the mathematical concepts using simple intuitive code snippets where applicable. Also add analogies that are relatable. If any piece of information is not available, then instead of hallucinating, simply put 'insufficient information available'. Also, ensure the summary is clear, accurate, and aligned with the provided style and length''',
    input_variables=['paper_input','style_input','length_input','name'],
    validate_template=True
)

template.save('template.json')