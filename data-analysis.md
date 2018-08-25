# A Newspaper for Men
## A study on the gender distribution of writers at the New York Times

We all read news with implicit biases. From our own political views to those of the news source's and reporter's, attempting to escape political, social, or other frames is futile. Whether we’re watching a fifteen-second TV ad or reading a carefully laid-out newspaper, the frame imposed on the content dissuades us from thinking, or nudges us toward predetermined thought patterns. In news, the sum of our experiences preceding *what* we read determines *how* we read it. We know this, and many actively try to read political articles from both the left and right. This leads to my question: **Why don't we recognize these same frames in gender?**

We each view the world through our own set of internal frames, shaped by every experience we’ve had and every word we’ve heard and uttered. Men and women have biological disparities, affecting their outlooks and how they shape their news. More importantly, the social landscapes for men and women are vastly different: from how they're raised, how they're spoken to, and societal pressures placed on them, men and women view the world through divergent lenses. And if only one gender reports information, we only see one side of the truth.

My study reviews *The New York Times*, widely revered as the paragon of the news industry, to determine whether an equally distributed number of men and women write their articles.


## Data Collection

I cumulated every New York Times article written over the last 7 years, which totaled to be over 350,000 articles. From each article, I extracted the first name of the main author and the "section_type," a topic name that the New York Times attributed to the article.

Although I had a list of the authors' first names, the New York Times did not explicitly state their genders. To resolve this issue, I'm using an algorithm predicated on artificial intelligence that searches through the US Social Security name database to predict gender. For names like Tracy and Alex, which can fall into either category, the algorithm sees which gender is more popular for that name, and places it into that group. Currently, it appears to be about 82% accurate. 

## Analysis

![](figures/time-histogram-plotly.png)
A male dominated field

Analysis on figure one (only a paragraph)

> The largest gap between genders was in April, 2016, when *78% of all articles were written by men*

![](figures/bubble-chart-topics1.png)
Analysis on figure two (only a paragraph)

## Conclusion

## Citations

 - All data gathered using the New York Times Developer API
 - Miles McCain for answering some of my questions
 - Sephen Holiday [@sholiday](https://github.com/sholiday) for the framework for the Gender Predictor
 - Name database provided by the [US Social Security Administration](https://www.ssa.gov/oact/babynames/limits.html)
