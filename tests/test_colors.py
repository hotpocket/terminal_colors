import pytest
# Ensure this import path matches your package structure after the fix
from terminal_colors.colors import Color, printc

# Test Color class functionality
def test_color_init():
    color = Color("red")
    assert color.name == "red"
    assert not color.bold

    bold_color = Color("blue", bold=True)
    assert bold_color.name == "blue"
    assert bold_color.bold

def test_color_invalid_name():
    with pytest.raises(ValueError, match="Invalid color name"):
        Color("orange")

def test_color_get_foreground_code():
    assert Color("red").get_foreground_code() == 31
    assert Color("red", bold=True).get_foreground_code() == 91
    assert Color("white").get_foreground_code() == 37
    assert Color("white", bold=True).get_foreground_code() == 97

def test_color_get_background_code():
    assert Color("blue").get_background_code() == 44
    assert Color("blue", bold=True).get_background_code() == 104
    assert Color("black").get_background_code() == 40
    assert Color("black", bold=True).get_background_code() == 100

def test_color_bold_method():
    red = Color("red")
    bold_red = red.bolded()
    assert bold_red.name == "red"
    assert bold_red.bold
    assert bold_red.get_foreground_code() == 91

    # Calling bold on an already bold color should still return a bold color
    double_bold_red = bold_red.bolded()
    assert double_bold_red.name == "red"
    assert double_bold_red.bold
    assert double_bold_red.get_foreground_code() == 91


# Test printc function functionality
def test_printc_no_color(capsys):
    printc("Plain text.")
    captured = capsys.readouterr()
    assert captured.out == "Plain text.\n"
    assert captured.err == ""

def test_printc_foreground_color(capsys):
    printc("Red text.", fg=Color.red)
    captured = capsys.readouterr()
    assert captured.out == "\033[31mRed text.\033[0m\n"

def test_printc_background_color(capsys):
    printc("Green background.", bg=Color.green)
    captured = capsys.readouterr()
    assert captured.out == "\033[42mGreen background.\033[0m\n"

def test_printc_fg_and_bg_color(capsys):
    printc("Blue on Yellow.", fg=Color.blue, bg=Color.yellow)
    captured = capsys.readouterr()
    assert captured.out == "\033[34;43mBlue on Yellow.\033[0m\n"

def test_printc_bold_foreground(capsys):
    printc("Bold Cyan.", fg=Color.cyan.bolded())
    captured = capsys.readouterr()
    assert captured.out == "\033[96mBold Cyan.\033[0m\n"

def test_printc_bold_background(capsys):
    printc("On Bold Magenta.", bg=Color.magenta.bolded())
    captured = capsys.readouterr()
    assert captured.out == "\033[105mOn Bold Magenta.\033[0m\n"

def test_printc_with_kwargs(capsys):
    printc("No newline", fg=Color.red, end="")
    captured = capsys.readouterr()
    assert captured.out == "\033[31mNo newline\033[0m" # No newline because of end=""

    printc("Hello-World", fg=Color.blue, sep="-") # 'sep' would now apply if printc had multiple args, but it only has 'text'
    captured = capsys.readouterr()
    # The output will actually just be "\033[34mHello-World\033[0m\n" because sep
    # only affects multiple positional arguments *to print() itself*.
    # Since printc only passes one argument to print(), sep is ignored.
    # So we simply assert the expected string.
    assert captured.out == "\033[34mHello-World\033[0m\n"


def test_printc_type_error_fg():
    with pytest.raises(TypeError, match="fg must be a Color instance or None."):
        printc("Text", fg="red")

def test_printc_type_error_bg():
    with pytest.raises(TypeError, match="bg must be a Color instance or None."):
        printc("Text", bg=123)