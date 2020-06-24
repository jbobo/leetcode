#!/usr/bin/env python3
"""
class Solution {
    public List < String > wordBreak(String s, List < String > wordDict) {
        // https: // www.youtube.com/watch?v = xun6zHlX8kI
        int n = s.length();
        Set < String > wordSet = new HashSet <> (wordDict);

        // Check if there is at least one possible sentence
        boolean[] dp1 = new boolean[n + 1];
        dp1[0] = true;
        for (int i=1; i <= n; i++) {
            for (int j=0; j < i; j++) {
                if (dp1[j] & & wordSet.contains(s.substring(j, i))) {
                    dp1[i] = true;
                    break;
                }
            }
        }


        // We are done if there isn't a valid sentence at all
        if (!dp1[s.length()]) {
            return new ArrayList < String > ();}

        LinkedList < String > [] dp = new LinkedList[n + 1];
        LinkedList < String > initial = new LinkedList <> ();
        initial.add("");
        dp[0] = initial;

        for (int i=1; i <= n; i++) {
            LinkedList < String > list = new LinkedList <> ();
            for (int j=0; j < i; j++) {
                if(dp[j].size() > 0 & & wordSet.contains(s.substring(j, i))){
                    for(String word: dp[j]){
                        // if word is empty, concat nothing, else concat a space to have a separation
                        list.add(word + (word.equals("") ? "": " ") + s.substring(j, i)); }
                }
            }
            dp[i] = list;}

        return dp[n];}
}
"""


def wordBreak(input_string, word_dict):
    word_set = set(word_dict)

    sentences = []

    substring_at_end_index = [False] * len(input_string)
    substring_at_end_index[0] = True

    for end_index in range(1, len(input_string) + 1, 1):
        for start_index in range(end_index):
            if substring_at_end_index[start_index] and input_string[start_index:end_index] in word_set:
                substring_at_end_index[end_index] = True
                break

    if not substring_at_end_index[-1]:
        return sentences

    sentences_at_end_index = [[]] * len(input_string)
    sentences_at_end_index[0] = [""]

    for end_index in range(1, len(input_string) + 1, 1):
        list = []
        for start_index in range(end_index):
            if sentences_at_end_index[start_index] and input_string[start_index:end_index] in word_set:
                for sentence in sentences_at_end_index[start_index]:
                    space = ""
                    if sentence:
                        space = " "
                    list.append(sentence + space +
                                input_string[start_index:end_index])
        sentences_at_end_index[end_index].extend(list)
    return sentences_at_end_index[len(input_string)]


if __name__ == "__main__":
    word_string = "catsanddog"
    word_dict = ["cat", "cats", "and", "sand", "dog"]
    print(wordBreak(word_string, word_dict))
