import itertools
import random

def generate_possible_digits(length):
    """
    Membuat list semua kemungkinan kombinasi digit dengan panjang tertentu.

    Args:
        length: Panjang deretan digit.

    Returns:
        List of strings representing all possible digit combinations.
    """
    digits = "0123456789"
    possibilities = ["".join(combination) for combination in itertools.product(digits, repeat=length)]
    return possibilities

def check_guess(guess, answer):
    """
    Membandingkan tebakan dengan jawaban dan memberikan umpan balik.

    Args:
        guess: Tebakan pengguna.
        answer: Jawaban yang benar.

    Returns:
        String yang menunjukkan hasil perbandingan (misalnya, "GGYBB").
    """
    result = ""
    for i in range(len(guess)):
        if guess[i] == answer[i]:
            result += "G"
        elif guess[i] in answer:
            result += "Y"
        else:
            result += "B"
    return result

def update_possibilities(possibilities, guess, feedback):
    """
    Memperbarui list kemungkinan digit berdasarkan umpan balik.

    Args:
        possibilities: List kemungkinan digit.
        guess: Tebakan pengguna.
        feedback: Umpan balik dari perbandingan.
    """
    new_possibilities = []
    for possibility in possibilities:
        if check_guess(guess, possibility) == feedback:
            new_possibilities.append(possibility)
    return new_possibilities

def wordle_digit(length, max_guesses):
    """
    Permainan Wordle dengan inputan string digit.

    Args:
        length: Panjang deretan digit.
        max_guesses: Jumlah maksimum tebakan.
    """
    answer = random.choice(generate_possible_digits(length))
    possibilities = generate_possible_digits(length)

    for _ in range(max_guesses):
        guess = random.choice(possibilities)
        feedback = check_guess(guess, answer)
        print(f"Tebakan: {guess}, Hasil: {feedback}")

        if feedback == "G" * length:
            print("Selamat, Anda menang!")
            return

        possibilities = update_possibilities(possibilities, guess, feedback)

    print("Anda kalah.")

panjang_digit = int(input('Masukkan Angka'))
tebakan = int(input('Masukkan tebakan'))
wordle_digit(panjang_digit, tebakan)  # Menebak deretan 4 digit dengan maksimal 6 tebakan