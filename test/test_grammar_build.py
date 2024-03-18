from llmformat.grammar_builder import (CustomJsonFormat, JsonFormat, LLMFormat,
                                       RuleManager, gen_bnf_grammar)

with RuleManager() as manager:
    format = LLMFormat(JsonFormat())
    print(gen_bnf_grammar())

with RuleManager() as manager:
    sample_json = {"bbc_news": [{"abstract": "Today, stock A is trasferred to stock B", "price": 100.3} ], "timestamp": 100}
    format = LLMFormat(CustomJsonFormat(sample_json))
    print(gen_bnf_grammar())