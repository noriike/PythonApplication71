import copy



x=[[1,2,3],4,5]
y=copy.copy(x)
y[0][0]=100
print('copy1',x,y)



xx=[[1,2,3],4,5]
yy=copy.deepcopy(xx)
yy[0][0]=100
print('copy2',xx,yy)

