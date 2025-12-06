stopwords = {"the", "a", "an", "and", "or", "is", "are", "at", "on", "in"}

def etl_pipeline(texts):
    all_words = []
    for text in texts:
      words = text.lower().split()
      for word in words:
        if word not in stopwords:
                all_words.append(word)

      freq_dict = {}
    for word in all_words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
    
    return freq_dict
