x=[1,2,3]
y=[20,40,60]
n=len(x)
mean_x=sum(x)/n
mean_y=sum(y)/n
num=0
den=0
for i in range(n):
    num+=(x[i]-mean_x)*(y[i]-mean_y)
    den+=(x[i]-mean_x)**2
m=num/den
b=mean_y-m * mean_x 
x_new=6
y_pred=m*x_new+b
print("slope(m):",m)
print("Intercept(b):",b)
print("Predicted Marks for 6 hours:",y_pred) 