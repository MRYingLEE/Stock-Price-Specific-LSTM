# Stock-Price-Specific-LSTM
This is a basic LSTM application on stock (securities) price.

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
A lot of people, especially technical analysis supporters, believe (https://en.wikipedia.org/wiki/Technical_analysis#Principles):
1. Market action discounts everything
2. Prices move in trends
3. History tends to repeat itself

Of course, some other people believe the price moves as random walking and no one can gain extra by taking advantange of the price data. 

Anyway, a lot of research shows the return is very similar to a normal distribution with fat tail.
![Normal Distribution](https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Normal_Distribution_PDF.svg/700px-Normal_Distribution_PDF.svg.png)

## What's the unique ?
There are a few good LSTM projects on stock price data. But the code shows that most of them didn't use any knowledge of stock market. The code is general to any data.

As an investement professional and an AI learner, I believe stock specific features are needed for stock price prediction. 

So based on the code of https://github.com/jaungiers/LSTM-Neural-Network-for-Time-Series-Prediction, I demoed my ideas.

I still use the original model define:

![Model Architecture](https://github.com/MRYingLEE/Stock-Price-Specific-LSTM/blob/master/model.png)


1. Stock specific preprocessing.
  I use daily return instead of price directly. After my preprocessing, I don't need any normalization. For the daily return is normalized in a normal distribution already. You may think I normalized the whole data set instead of windowed data at the beginning. 
  The original data is visualized as the following:
  ![Original Data](https://github.com/MRYingLEE/Stock-Price-Specific-LSTM/blob/master/Visual%20Data.png)
  
2. Stock specific post LSTM.
  In order to visualize the prediction, the predicted return is converted into price.
  
  The model using window-normalised price data has the following prediction:
  ![Based on Price Data](https://github.com/MRYingLEE/Stock-Price-Specific-LSTM/blob/master/Visual_Results%20by%20Normalised%20Price.png)
  The model using daily return data has the following prediction:
  ![Based on Return Data](https://github.com/MRYingLEE/Stock-Price-Specific-LSTM/blob/master/Visual%20Results%20by%20Return.png)
  
By the way, I added a lot of comments.

## Is it practical to use LSTM to make money?
The results is better than I expected.

There is a good discussion on this topic:
https://medium.com/@mikeharrisNY/machine-learning-often-a-complicated-way-of-replicating-simple-forecasting-methods-in-financial-25c38db2f624.

I agree that the algo is not so important and feature engineering is the key to success. In short, in order to make a successful mechine learning application on stock market, you should put your attension on your data. You cannot have complete stock market data. You have to balance your time, budget with the data universe, frenquency, delay and accuracy. Besides price data, you may need fundamental data, such as financial statements data.

## Credit
Most code is modified from  https://github.com/jaungiers/LSTM-Neural-Network-for-Time-Series-Prediction. So I didn't put my name in the source code.

## I am working on a reinforcement learning project on stock market.
Please follow it at https://github.com/MRYingLEE/Stock.AI
