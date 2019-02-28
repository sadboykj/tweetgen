import sys

# 1. Let's Get Started
# Bonus challenges: cowsay

def cowsay():

    cowsays = sys.argv[1:]
    speech = " ".join(cowsays)
    bubble = ""

    for char in speech:
        bubble += "_"



    cowtalk = """
         \   ^__^
          \  (oo)\_______
             (__)\       )\/\\
                 ||----w |
                 ||     ||
    """

    drawing = bubble + "\n" + speech + "\n" + bubble + cowtalk
        
    return drawing


if __name__ == '__main__':
    print(cowsay())