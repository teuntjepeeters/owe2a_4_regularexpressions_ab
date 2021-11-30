import re


def voorbeeld_re(string):
    print(string)
    #print(match_stopcodon.)
    #print(match_stopcodon.start())
    match_startcodon = re.search("ATG[ATGC]*TAA", string)
    #match_stopcodon = re.search("TAA", string)

    #print(match_startcodon.start())
    #print(match_stopcodon.end())
    print(string[match_startcodon.start():match_startcodon.end()])


def main():
    string = "AAATTATCCATGCCAAATTTTAAATATTAA"
    voorbeeld_re(string)


main()