// 3. Input a one page long file and process the text into words. Also get rid of "stop words".
// I'm not really familar with how to read in text files, so I did this one in JS which I am a bit more familiar with

// 1. Take in a text file
function process(data) {
  let words = split_and_clean(data);
  words = clear_stop_words(words);
  return words;
}

//2. Split and clear out special characters
function split_and_clean(str) {
  //1. Split
  let words = str.split(" ");
  //2. Iterate and clean
  for (let i = 0; i < words.length; i++) {
    words[i] = words[i].replaceAll(/[^a-zA-Z0-9\s]/g, ""); // Use regEx to get rid of all non-alphanumeric characters
  }
  return words;
}

//3. clear out stop words
function clear_stop_words(words) {
  const stopWords = [
    "i",
    "me",
    "my",
    "myself",
    "we",
    "our",
    "ours",
    "ourselves",
    "you",
    "your",
    "yours",
    "yourself",
    "yourselves",
    "he",
    "him",
    "his",
    "himself",
    "she",
    "her",
    "hers",
    "herself",
    "it",
    "its",
    "itself",
    "they",
    "them",
    "their",
    "theirs",
    "themselves",
    "what",
    "which",
    "who",
    "whom",
    "this",
    "that",
    "these",
    "those",
    "am",
    "is",
    "are",
    "was",
    "were",
    "be",
    "been",
    "being",
    "have",
    "has",
    "had",
    "having",
    "do",
    "does",
    "did",
    "doing",
    "a",
    "an",
    "the",
    "and",
    "but",
    "if",
    "or",
    "because",
    "as",
    "until",
    "while",
    "of",
    "at",
    "by",
    "for",
    "with",
    "about",
    "against",
    "between",
    "into",
    "through",
    "during",
    "before",
    "after",
    "above",
    "below",
    "to",
    "from",
    "up",
    "down",
    "in",
    "out",
    "on",
    "off",
    "over",
    "under",
    "again",
    "further",
    "then",
    "once",
    "here",
    "there",
    "when",
    "where",
    "why",
    "how",
    "all",
    "any",
    "both",
    "each",
    "few",
    "more",
    "most",
    "other",
    "some",
    "such",
    "no",
    "nor",
    "not",
    "only",
    "own",
    "same",
    "so",
    "than",
    "too",
    "very",
    "s",
    "t",
    "can",
    "will",
    "just",
    "don",
    "should",
    "now",
  ];

  let newWords = [];
  let i = 0;
  let j = 0;

  for (i = 0; i < words.length; i++) {
    if (!stopWords.includes(words[i].toLowercase)) {
      newWords[j] = words[i];
      j++;
    }
    // Else its a stop word don't add
  }
  return newWords;
}

// Read in the text file
const fs = require("fs");
fs.readFile("lordOfTheFliesSelection.txt", (err, data) => {
  if (err) throw err;

  console.log(process(data.toString())); // Process the data
});
