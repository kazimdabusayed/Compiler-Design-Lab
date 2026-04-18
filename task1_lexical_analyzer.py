import re

KEYWORDS = {"int", "float", "if", "else", "return"}
OPERATORS = {"=", "+", "-", "*", "/", "==", "!=", "<=", ">="}
SEPARATORS = {";", "(", ")", "{", "}"}


def tokenize(source):
    token_re = re.compile(
        r"""\s*
        (?:(\d+)([A-Za-z_]\w*)(==|!=|<=|>=)([=+\-*/]) ([;(){}])(.))
    """,
        re.VERBOSE,
    )

    tokens = []

    for number, word, multi_op, single_op, sep, invalid in token_re.findall(source):
        if number:
            tokens.append(("INT", number))

        elif word:
            kind = "KEYWORD" if word in KEYWORDS else "IDENTIFIER"
            tokens.append((kind, word))

        elif multi_op:
            tokens.append(("OPERATOR", multi_op))

        elif single_op:
            tokens.append(("OPERATOR", single_op))

        elif sep:
            tokens.append(("SEPARATOR", sep))

        elif invalid:
            raise ValueError(f"Invalid token: {invalid}")

    return tokens


# Test
sample = "int x=10; if(x!=0){x=x*2;}"
for kind, value in tokenize(sample):
    print(f"{kind}: {value}")