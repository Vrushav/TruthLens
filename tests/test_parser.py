from src.modules.parser import ResponseParser

parser = ResponseParser()

sample_response = """
Python was created by Guido van Rossum in 1991.
It is an interpreted programming language.
Python supports multiple programming paradigms.
"""

claims = parser.get_claims(sample_response)

print("Extracted Claims:\n")

for index, claim in enumerate(claims, start=1):
    print(f"{index}. {claim}")