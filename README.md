# doctor-model


## Description
This model was an attempt at improving patient/practitioner matching effectiveness for a virtual care provider. A user would type in the ideal review they would leave for a doctor and the model would take this phrase and match it to the doctor with the closest matching traits. This could optimize the matching system by using the best (closest matching) doctor available instead of using a basic first in, first out queue system.

## Process
- A webscraper was created to read data from a public doctor rating [site](https://www.ratemds.com/)
- Preprocessing data by manual labelling each data point
- Feature selection by finding most correlated words with each descriptor
- Text classification model selection by running a comparison of naive-bayes, svc, random forest, and a logistic regression.
- Accuracy test using a weighted averaged f1 score

## Results
- This tool struggled to gain much accuracy due to a small data set, though random forest solved with an accuracy of 23% in the testing data. Although low, this is a 23% improvement in fitment from before.
- For more information, there is a full report in the repo!

## Tools
- [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/) Parsing library
- [Selenium](https://www.selenium.dev/) Browser automation
- [SK-Learn](https://scikit-learn.org/stable/getting_started.html) Machine learning library

## Languages
- [Python](https://www.python.org/)
