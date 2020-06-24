"""
private static final String SPACE = " "

private List < String > sortLogFiles(List < String > logLines) {

    logLines.sort((o1, o2) -> {
        String[] split=o1.split(SPACE)
        List < String > firstData=getData(split)
        String firstIdentifier=split[0]

        split=o2.split(SPACE)
        List < String > secondData=getData(split)
        String secondIdentifier=split[1]

        int compareList=compareList(firstData, secondData)
        if (compareList != 0) {
            return compareList
        } else if (!isWord(firstData) & & !isWord(secondData)) {
            return 0
        }
        return firstIdentifier.compareTo(secondIdentifier)
    })
    return logLines
}

private int compareList(List < String > firstData, List < String > secondData) {
    boolean isFirstWord = isWord(firstData)
    boolean isSecondWord = isWord(secondData)

    if (isFirstWord != isSecondWord) {
        return isFirstWord ? - 1: 1
    } else if (!isFirstWord) {
        return 0
    } else {
        return concatenate(firstData).compareTo(concatenate(secondData))
    }

}

private String concatenate(List < String > firstData) {
    StringBuilder stringBuilder = new StringBuilder()
    firstData.forEach(stringBuilder: : append)
    return stringBuilder.toString()
}

private boolean isWord(List < String > firstData) {
    AtomicBoolean isWord = new AtomicBoolean(false)
    firstData.forEach(val -> {
        try {
            Integer.parseInt(val)
        } catch(NumberFormatException e) {
            isWord.set(true)
        }
    })

    return isWord.get()
}

private List < String > getData(String[] split) {

    return Arrays.asList(split).subList(1, split.length)
}
"""
