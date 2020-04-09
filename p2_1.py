from flashtext import KeywordProcessor

# determine the position of the New York
keyword_processor = KeywordProcessor()
keyword_processor.add_keyword('New York', 'New York')
keywords_found = keyword_processor.extract_keywords('New York City (NYC), often called the City of New York or simply New York (NY), is the most populous city in the United States. With an estimated 2018 population of 8,398,748 distributed over about 302.6 square miles (784 km2), New York is also the most densely populated major city in the United States.[10] Located at the southern tip of the U.S. state of New York, the city is the center of the New York metropolitan area, the largest metropolitan area in the world by urban landmass.[11] With almost 20 million people in its metropolitan statistical area and approximately 23 million in its combined statistical area, it is one of the worlds most populous megacities. New York City has been described as the cultural, financial, and media capital of the world, significantly influencing commerce,[12] entertainment, research, technology, education, politics, tourism, art, fashion, and sports. Home to the headquarters of the United Nations,[13] New York is an important center for international diplomacy.[14][15]', span_info=True)
print(keywords_found)

# change the keyword 'New York City' to 'NYC' and 'New York' to 'NY'
keyword_processor.add_keyword('New York City', 'NYC')
keyword_processor.add_keyword('New York', 'NY')
new_sentence = keyword_processor.replace_keywords('New York City, often called the City of New York or simply New York (NY), is the most populous city in the United States. With an estimated 2018 population of 8,398,748 distributed over about 302.6 square miles (784 km2), New York is also the most densely populated major city in the United States.[10] Located at the southern tip of the U.S. state of New York, the city is the center of the New York metropolitan area, the largest metropolitan area in the world by urban landmass.[11] With almost 20 million people in its metropolitan statistical area and approximately 23 million in its combined statistical area, it is one of the worlds most populous megacities. New York City has been described as the cultural, financial, and media capital of the world, significantly influencing commerce,[12] entertainment, research, technology, education, politics, tourism, art, fashion, and sports. Home to the headquarters of the United Nations,[13] New York is an important center for international diplomacy.[14][15]')
print(new_sentence)

