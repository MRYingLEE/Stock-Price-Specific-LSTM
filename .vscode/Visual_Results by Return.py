# This programe is to analize the results when we deal with window-normalised price data directly.

# Say, for the corresponding config.json,
# 	"data": {
# 		"filename": "sp500-new.csv",
# 		"columns": [
# 			"Return",
# 			"Volume"
# 		],
#     ....
#

import numpy as np
import matplotlib.pyplot as plt

predictions=np.loadtxt('rate_predictions.csv')
y_test=np.loadtxt('rate_y_test.csv')

# To convert return to cumulative return
cum_predictions =np.cumprod(1 + predictions)
cum_test=np.cumprod(1+y_test)
cum_predictions =np.multiply(1 +np.asarray(predictions),cum_test) # use only 1 step prediction based on each real return
np.delete(cum_test,0)
cum_predictions2=np.cumprod(1+predictions) # cumulative predicted return, no real return is used

# To visualize
f, (ax1, ax2) = plt.subplots(2, sharex=False, sharey=False)
ax1.plot(cum_test, label='True Data')
ax1.plot(cum_predictions,label='Step by Step Prediction')
ax1.set_title('True Data vs Step Prediction')

ax2.plot(cum_test, label='True Data')
ax2.plot(cum_predictions2,label='Cumulative Prediction')

ax2.set_title('True Data vs Cumulative Prediction')

f.suptitle('Visualize Cumulative Return\n'+"Avg(Y_Test)="+str(np.average(y_test))+"\n"+"Avg(predictions)="+str(np.average(predictions)))

plt.show()

#Conclusion: The model is much optimistic in an typical uptread. 
