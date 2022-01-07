from words import strip_accents, get_matching_words


# ç -> c

def test_strip_accents():
    assert "factoritzacio" == strip_accents("factorització")
    assert "hubnerita" == strip_accents("hübnerita")
    assert "cal·litrique" == strip_accents("cal·lítrique")
    assert "calcapeu" == strip_accents("calçapeu")


def test_get_matching_words():
    input_words = ["fogo/_F_V_Y", "fogalleig/_E", "fogallejar/52", "foganya/_E", "fogar/78",
                   "fogarenc/_F", "fogassa/_E", "fogasser/_E", "fogassó/_G", "fogata/_E", "fogater/_E", "fogater/_F",
                   "fogatera/_E", "fogatge/_E", "fogatger/_F", "fogatina/_E", "folat"]

    matching_words = get_matching_words(input_words, "f", ["d", "o", "g", "a", "r", "n"])
    assert "fogar" in matching_words

    matching_words = get_matching_words(["folat", "fosss/_E", "foo/_F", "now/_E", "fofo/_E"], "f",
                                        ["d", "o", "g", "a", "r", "n"])
    assert "fofo" in matching_words


test_strip_accents()

test_get_matching_words()
