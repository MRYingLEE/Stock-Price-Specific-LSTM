# Stock-Specific-LSTM
This is a basic LSTM application on stock (securities) market.

## What's LSTM (Long Short-Term Memory)?
A popular LSTM introcution can be found at http://colah.github.io/posts/2015-08-Understanding-LSTMs/. It said:
Long Short Term Memory networks – usually just called “LSTMs” – are a special kind of RNN, capable of learning long-term dependencies. They were introduced by Hochreiter & Schmidhuber (1997), and were refined and popularized by many people in following work.1 They work tremendously well on a large variety of problems, and are now widely used.

LSTMs are explicitly designed to avoid the long-term dependency problem. Remembering information for long periods of time is practically their default behavior, not something they struggle to learn!

The internal LSTM architecture is as the following:
![Architecture](https://cdn-images-1.medium.com/max/800/1*0f8r3Vd-i4ueYND1CUrhMA.png)

## How does LSTM work?
There is a good Illustrated Guide to LSTM (https://towardsdatascience.com/illustrated-guide-to-lstms-and-gru-s-a-step-by-step-explanation-44e9eb85bf21).

Forget gate
![Forget gate](https://cdn-images-1.medium.com/max/800/1*GjehOa513_BgpDDP6Vkw2Q.gif)

Input gate
![Input gate](https://cdn-images-1.medium.com/max/800/1*TTmYy7Sy8uUXxUXfzmoKbA.gif)

Cell State
![Cell State](https://cdn-images-1.medium.com/max/800/1*S0rXIeO_VoUVOyrYHckUWg.gif)

Output Gate
![Output gate](https://cdn-images-1.medium.com/max/800/1*VOXRGhOShoWWks6ouoDN3Q.gif)

If you are not familar to LSTM, I strongly suggest you to check this guide.

## Why LSTM?
By Wikipedia (https://en.wikipedia.org/wiki/Long_short-term_memory):
LSTM networks are well-suited to classifying, processing and making predictions based on time series data, since there can be lags of unknown duration between important events in a time series. LSTMs were developed to deal with the exploding and vanishing gradient problems that can be encountered when training traditional RNNs. Relative insensitivity to gap length is an advantage of LSTM over RNNs, hidden Markov models and other sequence learning methods in numerous applications.

In short, LSTM is suitable to deal with a time series with long term patterns.

## What's the specificity of stock market?
A lot of people, especially technical analysis supporters, think stock market price data is this kind of data. The technical analysis believes (https://en.wikipedia.org/wiki/Technical_analysis#Principles):
1. Market action discounts everything
2. Prices move in trends
3. History tends to repeat itself

Of course, a lot of people believes there is the price moves as random walking and no one can gain extra by taking advantange of the price data. A lot of research shows the return is very similar to a normal distribution with fat tail.

![Normal Distribution](https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Normal_Distribution_PDF.svg/700px-Normal_Distribution_PDF.svg.png)

## What's the unique ?
There are a few good LSTM projects on stock price data. But the code shows that most of them didn't use any knowledge of stock market. The code is general to any data.

As an investement professional and an AI learner, I believe a stock specific features are needed. 

So based on the code of https://github.com/jaungiers/LSTM-Neural-Network-for-Time-Series-Prediction, I demoed my ideas.

In short,
1. Stock specific preprocessing
  I use daily return instead of price directly. And I normalize the whole data set instead of windowed data. After my preprocessing, I don't need any normalization. For the daily return is normalized in a normal distribution already.
  
2. Stock specific post LSTM

3. More comments


## Is it practical?


## Credit
Most code is copied from . What I did is as the following:

