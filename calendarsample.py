import calendar

#�����̕\��
print(calendar.monthrange(2018,1)[1])
print(calendar.monthrange(2018,2)[1])

#�N�����w�肵�ăJ�����_�[��\��
calendar.prmonth(2018,1)

#�N�_����j�ɂ����J�����_�[��\��
c=calendar.TextCalendar(calendar.SUNDAY)
c.prmonth(2018,1)

#���邤�N���ǂ���
print(calendar.isleap(2018))
print(calendar.isleap(2020))
