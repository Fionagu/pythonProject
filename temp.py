s="4.0154.1003.8083.8373.8543.48112.85612.81612.46612.86912.49512.5253.7283.3373.3013.3083.6213.2903.6623.8043.4433.4243.3563.6746.7996.7346.8036.6886.4026.71542.01546.10841.94841.61441.62341.7733.3163.3393.6973.3273.7303.7013.6773.3433.7153.3123.3873.6983.3243.6953.6693.3283.6453.306"

times = []

i = s.find('.')
while (i>0):
    times.append(s[0:i+4])
    s = s[i+4:]
    i = s.find('.')

for t in times:
    print(t)