# This programe is to analize the results when we deal with window-normalised price data directly.

# Say, for the corresponding config.json,
# 	"data": {
# 		"filename": "sp500-new.csv",
# 		"columns": [
# 			"Close",
# 			"Volume"
# 		],
#     ....
#

import numpy as np
import matplotlib.pyplot as plt
import math

predictions=np.loadtxt('predictions.csv')
cum_predictions =np.cumprod(np.power(1 + predictions, 1/49)) #To convert a 49 days return to daily return, then cumulate

test=np.loadtxt('test.csv',delimiter=',', usecols=range(2))[:,0]
effective_test=test[:-50]

y_test=np.loadtxt('y_test.csv')

cum_y_test=np.multiply(effective_test,y_test+1)
daily_test=np.diff(test) / test[1:]


f, (ax1, ax2) = plt.subplots(2, sharex=False, sharey=False)
ax1.plot(test[50:], label='True Data')
ax1.plot(cum_y_test,label='Predicted Price')
ax1.set_title('True Data vs Step Prediction')

ax2.plot(test[50:], label='True Data')
ax2.plot(cum_predictions*test[50],label='Cumulative Prediction')

ax2.set_title('True Data vs Cumulative Prediction')

f.suptitle('Visualize Price and Prediction\n'+"Avg(delta Y_Test)="+str(np.average(daily_test))+"\n"+"Avg(delta predictions)="+str(np.average(predictions)))
plt.show()

#Conclusion: The model is much optimistic in an typical uptread. 