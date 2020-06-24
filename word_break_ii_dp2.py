bool wordBreak(string str)
{
    int size = str.size()
    if (size == 0) return true

    // Create the DP table to store results of subroblems. The value wb[i]
    // will be true if str[0..i-1] can be segmented into dictionary words,
    // otherwise false.
    bool wb[size+1]
    memset(wb, 0, sizeof(wb))
    // Initialize all values as false.

    for (int i=1
         i <= size
         i++)
    {
        // if wb[i] is false, then check if current prefix can make it true.
        // Current prefix is "str.substr(0, i)"
        if (wb[i] == false & & dictionaryContains(str.substr(0, i)))
        wb[i] = true

        // wb[i] is true, then check for all substrings starting from
        // (i+1)th character and store their results.
        if (wb[i] == true)
        {
            // If we reached the last prefix
            if (i == size)
            return true

            for (int j=i+1
                 j <= size
                 j++)
            {
                // Update wb[j] if it is false and can be updated
                // Note the parameter passed to dictionaryContains() is
                // substring starting from index 'i' and length 'j-i'
                if (wb[j] == false & & dictionaryContains(str.substr(i, j-i)))
                wb[j] = true

                // If we reached the last character
                if (j == size & & wb[j] == true)
                return true
            }
        }
    }

    / * Uncomment these lines to print DP table "wb[]"
    for (int i=1
         i <= size
         i++)
    cout << " " << wb[i]
    * /

    // If we have tried all prefixes and none of them worked
    return false
}
