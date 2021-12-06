import re


def voorbeeld_re(string):
    print(string)
    #print(match_stopcodon.)
    #print(match_stopcodon.start())
    match_startcodon = re.search("ATG", string)
    for match in re.finditer("ATG", string):
        print(match.start())

    #match_stopcodon = re.search("TAA", string)

    #print(match_startcodon.start())
    #print(match_stopcodon.end())
    print(match_startcodon.start())


def main():
    string = "AATGAATTATCCATGCCAAATTTTAAATATTAA"
    voorbeeld_re(string)


main()