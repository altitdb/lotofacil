def print_games(writer):
    for number01 in range(1, 26):
        for number02 in range(number01 + 1, 26):
            for number03 in range(number02 + 1, 26):
                for number04 in range(number03 + 1, 26):
                    for number05 in range(number04 + 1, 26):
                        for number06 in range(number05 + 1, 26):
                            for number07 in range(number06 + 1, 26):
                                for number08 in range(number07 + 1, 26):
                                    for number09 in range(number08 + 1, 26):
                                        for number10 in range(number09 + 1, 26):
                                            for number11 in range(number10 + 1, 26):
                                                for number12 in range(number11 + 1, 26):
                                                    for number13 in range(number12 + 1, 26):
                                                        for number14 in range(number13 + 1, 26):
                                                            for number15 in range(number14 + 1, 26):
                                                                line = f'{number01},{number02},{number03},{number04},{number05},{number06},{number07},{number08},{number09},{number10},{number11},{number12},{number13},{number14},{number15}'
                                                                writer.write(f'{line}\n')


if __name__ == '__main__':
    with open("games.md", "w") as writer:
        print_games(writer)