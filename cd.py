import re


def voorbeeld_regex(sequence):
    print(sequence)
    match_start = re.search("ATG", sequence)
    print(match_start.start())
    print(match_start.group())

    for match in re.finditer("ATG", sequence):
        print(match.start())

    # match_stop = re.search("TAA", sequence)
    # print(match_stop.end())
    # print(match_stop.group())

    # print(sequence[match_start.start(): match_stop.end()])


def main():
    sequence = "AAATTTATGGAATATGGGCCCCATTAACAT"
    # voorbeeld_regex(sequence)
    print("Goedemorgen!\nHoe gaat het met je?\tHier alles goed!")
    print(r"Goedemorgen!\nHoe gaat het met je?\tHier alles goed!")


main()
