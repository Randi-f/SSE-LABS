from app import process_query


def test_knows_about_dinosaurs():
    assert (
        process_query("dinosaurs") == "Dinosaurs ruled the Earth 200 million years ago"
    )


def test_does_not_know_about_asteroids():
    assert process_query("asteroids") == "Unknown"


def test_does_not_know_about_name():
    assert process_query("What is your name?") == "Aoligei"


def test_plus():
    assert process_query("What is 27 plus 75?") == "102"


def test_max():
    assert process_query("Which of the following numbers is the largest: 98, 59, 31?") == "98"


def test_multiplied():
    assert process_query("What is 5 multiplied by 9?") == "45"


def test_square_cube():
    assert process_query("Which of the following numbers is both a square and a cube: 8, 4, 64") == "64"
