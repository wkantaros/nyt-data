# A Newspaper for Men
## A study on the gender distribution of writers at the New York Times

We all read news with implicit biases. From our own political views to those of the news source's and reporter's, attempting to escape political, social, or other frames is futile. Whether we’re watching a fifteen-second TV ad or reading a carefully laid-out newspaper, the frame imposed on the content dissuades us from thinking, or nudges us toward predetermined thought patterns. In news, the sum of our experiences preceding *what* we read determines *how* we read it. We know this, and many actively try to read political articles from both the left and right. This leads to my question: **Why don't we recognize these same frames in gender?**

We each view the world through our own set of internal frames, shaped by every experience we’ve had and every word we’ve heard and uttered. Men and women have biological disparities, affecting their outlooks and how they shape their news. More importantly, the social landscapes for men and women are vastly different: from how they're raised, how they're spoken to, and societal pressures placed on them, men and women view the world through divergent lenses. And if only one gender reports information, we only see one side of the truth.

My study reviews *The New York Times*, widely revered as the paragon of the news industry, to determine whether an equally distributed number of men and women write their articles.


## Data Collection

I cumulated every New York Times article written over the last 7 years, which totaled to be over 350,000 articles. From each article, I extracted the first name of the main author and the "section_type," a topic name that the New York Times attributed to the article.

Although I had a list of the authors' first names, the New York Times did not explicitly state their genders. To resolve this issue, I created an algorithm that searches through the US Social Security name database to predict gender. For names like Tracy and Alex, which can fall into either category, the algorithm checks which gender is more popular for that name, and places it into that group. If the name cannot be placed into a gender with a 60% certainty or higher, or if the name isn't in the database at all, the algorithm omits the name to insure accurate data. Roughly 5% of the data was not included in my analysis for these reasons.

## Analysis

In order to determine whether there is an imbalance between articles written by men and women, we need to look at the number of articles written by each gender. Seeing how this data looks over a five year span ensures reliability and eliminates the possibility of an outlier month as the cause for an inbalance.

![](figures/histogram-2011-to-2018.png)
As we can see from the histogram above, writing at the New York Times is heavily male dominated. Men consistently double or nearly double women in total articles every month. Men wrote 7,290 articles - the greatest number of articles written by a single gender in a month - in January 2012. For comparison, during that same month women wrote a measly 3,554 articles, or a little over 32% of the total articles. Eight years later, there doesn't appear to be any progress concerning the amelioration of gender discrepancies at The Times.

It is also worth noting the drastic reduction in total articles over the last seven yers. In that time span, The Times released 12,069 articles at its peak in January, 2012. Over the ensuing years, that number has plummeted. In December, 2017, the newspaper published a mere 991 articles, or 8% of what was produced nearly seven years earlier.

Within The Times, gender distributions fluctuate between topic sections. This is shown in the figure below.

![](figures/bubble-chart-topics1.png)

Although some topic sections have a relatively equal gender distribution, a far greater number do not. Several sections contain more female writers, including Real Estate, Travel, and Fashion, but these sections publish fewer articles per month in comparison to the other Times' sections. In fact, primarily men write the top seven topic sections, which include US, World, Arts, Business, and Opinion.

In December, 2016, women wrote only 24.9% of the articles in the Opinion Section. The Opinion section covers authors views on a variety of topics, from politics, to food, to life decisions. Simply put, readers hear the voices and views of the authors in this section. Why, then, does The Times mainly present the voices of only 50% of the population?

## Conclusion

Over the last seven years, the amount of news distributed to the American people from The Times has diminished, and the company and continues to select voices from a skewed demographic. When people consume information from a homogeneous source, they develop blindspots; they are deprived of fresh ideas, new cultures, and diverging opinions as a consequence. As the New York Times continues to release fewer articles, the potency of each becomes greater. Not to be confused, The Times has a great reputation for a reason: for over a hundred years they've released an ample amount of quality content to the public. However, we must be cognizant of their blindspots. Much like the rise of suburban America in the 1950s, where provincial ideas resonated off one other like a soundboard for white America, the concentrated male-dominated news perpetrated by the New York Times leaves Americans in uniform thought, and leaves women without representation. And when the distributors of information are only a few, homogeneous voices, democracy and the progress of this nation halts. Although the absence of free news can cripple a nation, a trusted newsource with concealed biases, like The New York Times, can trigger pernicious and equally damaging consequences.


## Citations

 - All data gathered using the New York Times Developer API
 - Miles McCain for answering some of my questions
 - Sephen Holiday [@sholiday](https://github.com/sholiday) for the framework for the Gender Predictor
 - Name database provided by the [US Social Security Administration](https://www.ssa.gov/oact/babynames/limits.html)
