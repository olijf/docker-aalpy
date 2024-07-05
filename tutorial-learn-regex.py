from aalpy.SULs import RegexSUL
from aalpy.oracles import StatePrefixEqOracle
from aalpy.learning_algs import run_Lstar
from aalpy.utils import visualize_automaton

def regex_example(regex, alphabet):
    """
    Learn a regular expression.
    :param regex: regex to learn
    :param alphabet: alphabet of the regex
    :return: DFA representing the regex
    """
    regex_sul = RegexSUL(regex)

    eq_oracle = StatePrefixEqOracle(alphabet, regex_sul, walks_per_state=2000,
                                    walk_len=15)

    # or replace run_Lstar with run_KV
    learned_regex = run_Lstar(alphabet, regex_sul, eq_oracle, automaton_type='dfa')

    return learned_regex


if __name__ == "__main__":
    regex = 'a*b'
    alphabet = ['a', 'b']

    learned_regex = regex_example(regex, alphabet)

    print(f"Learned regex: {learned_regex}")
    #learned_regex.visualize(file_path='learned_regex')
    visualize_automaton(learned_regex)
    assert learned_regex == "a*b$"