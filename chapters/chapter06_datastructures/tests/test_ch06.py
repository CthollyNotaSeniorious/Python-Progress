from ..exercises.exercise_40 import is_anagram
from ..exercises.exercise_41 import remove_duplicates
from ..exercises.exercise_42 import count_letters
from ..exercises.exercise_43 import unique_elements
from ..exercises.exercise_44 import sum_of_freq_tuples
from ..exercises.exercise_45 import count_words
from ..exercises.exercise_46 import valid_parentheses
from ..exercises.exercise_47 import record_x_in_matrix
from ..exercises.exercise_48 import is_target_duplicate_in_matrix
from ..exercises.exercise_49 import rolling_sum


def test_e40():
    assert is_anagram("apple", "papel") is True
    assert is_anagram("banana", "ananab") is True
    assert is_anagram("hello", "world") is False
    assert is_anagram("rat", "cat") is False


def test_e41():
    assert remove_duplicates([]) == []
    assert remove_duplicates([1, 2, 2, 3, 3, 3]) == [1, 2, 3]
    assert remove_duplicates([1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1]
    assert remove_duplicates([1, 2, 3, 4, 4, 5, 6, 6, 7]) == [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
    ]
    assert remove_duplicates([1, 2, 3, 4, 5, 6, 7]) == [1, 2, 3, 4, 5, 6, 7]


def test_e42():
    assert count_letters("") == {}
    assert count_letters("hello") == {"h": 1, "e": 1, "l": 2, "o": 1}
    assert count_letters("apple") == {"a": 1, "p": 2, "l": 1, "e": 1}
    assert count_letters("banana") == {"b": 1, "a": 3, "n": 2}
    assert count_letters("word") == {"w": 1, "o": 1, "r": 1, "d": 1}


def test_e43():
    assert unique_elements([], []) == set()
    assert unique_elements([1], [1]) == {1}
    assert unique_elements([1, 2, 3], [1, 2, 3]) == {1, 2, 3}
    assert unique_elements([1, 2, 2, 3], [2, 1, 4]) == {1, 2, 3, 4}
    assert unique_elements([1, 2, 3], [4, 5, 6]) == {1, 2, 3, 4, 5, 6}
    assert unique_elements([1, 6, 7, 8], [2, 3, 4, 5]) == {
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
    }


def test_e44():
    assert sum_of_freq_tuples([]) == {}
    assert sum_of_freq_tuples([("a", 1), ("b", 2), ("a", 3)]) == {
        "a": 4,
        "b": 2,
    }
    assert sum_of_freq_tuples([("a", 1), ("b", 2), ("a", 3), ("b", 1)]) == {
        "a": 4,
        "b": 3,
    }
    assert sum_of_freq_tuples([("a", 1), ("b", 2), ("c", 3), ("d", 1)]) == {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 1,
    }
    assert sum_of_freq_tuples(
        [("a", 0), ("b", 2), ("b", 8), ("d", 5), ("d", 5), ("a", 10)]
    ) == {"a": 10, "b": 10, "d": 10}


def test_e45():
    assert count_words([]) == {}
    assert count_words(["hello", "world"]) == {"hello": 1, "world": 1}
    assert count_words(["hello", "world", "hello"]) == {"hello": 2, "world": 1}
    assert count_words(["a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]) == {"a": 10}
    assert count_words(
        ["learning", "python", "is", "fun", "python", "dynamic", "language"]
    ) == {
        "learning": 1,
        "python": 2,
        "is": 1,
        "fun": 1,
        "dynamic": 1,
        "language": 1,
    }


def test_e46():
    assert valid_parentheses("()") is True
    assert valid_parentheses("()[]{}") is True
    assert valid_parentheses("(]") is False
    assert valid_parentheses("([)]") is False
    assert valid_parentheses("{[]}") is True
    assert valid_parentheses("(([[{([({{}})])}]]))") is True
    assert valid_parentheses("(([[{([({{})])}]]))") is False


def test_e47():
    assert (
        record_x_in_matrix(
            [
                ["O", "O", "O", "O"],
                ["O", "O", "O", "O"],
                ["O", "O", "O", "O"],
                ["O", "O", "O", "O"],
            ]
        )
        == []
    )
    assert record_x_in_matrix(
        [
            ["O", "O", "O", "O"],
            ["O", "X", "O", "O"],
            ["O", "O", "O", "O"],
            ["O", "O", "O", "O"],
        ]
    ) == [(1, 1)]
    assert record_x_in_matrix(
        [
            ["X", "O", "O", "O"],
            ["O", "X", "O", "O"],
            ["O", "O", "X", "O"],
            ["O", "O", "O", "X"],
        ]
    ) == [(0, 0), (1, 1), (2, 2), (3, 3)]
    assert record_x_in_matrix(
        [
            ["X", "O", "O", "X"],
            ["O", "X", "X", "O"],
            ["O", "X", "X", "O"],
            ["X", "O", "O", "X"],
        ]
    ) == [(0, 0), (0, 3), (1, 1), (1, 2), (2, 1), (2, 2), (3, 0), (3, 3)]


def test_e48():
    assert is_target_duplicate_in_matrix([], "X") is False
    assert (
        is_target_duplicate_in_matrix(
            [
                ["O", "O", "O"],
                ["O", "O", "O"],
                ["O", "O", "O"],
            ],
            "X",
        )
        is False
    )
    assert (
        is_target_duplicate_in_matrix(
            [
                ["O", "O", "O"],
                ["O", "O", "O"],
                ["O", "O", "O"],
            ],
            "O",
        )
        is True
    )
    assert (
        is_target_duplicate_in_matrix(
            [
                ["O", "O", "O", "Y"],
                ["O", "Y", "O", "O"],
            ],
            "Y",
        )
        is True
    )
    assert (
        is_target_duplicate_in_matrix(
            [
                ["A", "B", "C", "D"],
                ["E", "F", "G", "H"],
            ],
            "A",
        )
        is False
    )


def test_e49():
    assert rolling_sum([], 2) == []
    assert rolling_sum([1, 2, 3, 4, 5], 1) == [1, 2, 3, 4, 5]
    assert rolling_sum([1, 2, 3, 4, 5], 2) == [3, 5, 7, 9]
    assert rolling_sum([1, 2, 3, 4, 5], 3) == [6, 9, 12]
    assert rolling_sum([1, 2, 3, 4, 5], 4) == [10, 14]
    assert rolling_sum([1, 2, 3, 4, 5], 5) == [15]
    assert rolling_sum([10, 20, 30, 40, 50, 60], 3) == [60, 90, 120, 150]
