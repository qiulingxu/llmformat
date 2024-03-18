python -m build .  && python -m pip uninstall llmformat -y && python -m pip install ./dist/llmformat-0.0.2.2-py3-none-any.whl && python test/test_grammar_build.py
