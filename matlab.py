import numpy as np
import matplotlib.pyplot as plt
import math
t1=np.array([0,0.0175,0.0350,0.0525,0.0699,0.0874,0.1049,0.1224,0.1399,0.1574,0.1749
    ,0.1923,0.2098,0.2273,0.2448,0.2623,0.2798,0.2973,0.3148,0.3322,0.3497,0.3672,0.3847,0.4022
    ,0.4197,0.4372,0.4546,0.4721,0.4896,0.5071,0.5246,0.5421,0.5596,0.5770,0.5945,0.6120,0.6295,0.6470,0.6645,0.6820
    ,0.6994,0.7169,0.7344,0.7519,0.7694,0.7869,0.8044,0.8219,0.8393,0.8568,0.8743,0.8918,0.9093
    ,0.9268,0.9443,0.9617,0.9792,0.9967,1.0142,1.0317,1.0492,1.0667,1.0841,1.1016,1.1191
    ,1.1366,1.1541,1.1716,1.1891,1.2065,1.2240,1.2415,1.2590,1.2765,1.2940,1.3115,1.3290,1.3464,1.3639,1.3814
    ,1.3989,1.4164,1.4339,1.4514,1.4688,1.4863,1.5038,1.5213,1.5388,1.5563,1.5738,1.5912,1.6087,1.6262,1.6437,1.6612,1.6787,1.6962,1.7136,1.7311,1.7486,1.7661])
y1=np.array([
    0.0006,0.0117,0.0353,0.0347,0.0133,0.0163,0.0047
    ,0.0021,0.0380,0.0162,0.0261,0.0476,0.0334,0.0237,0.0325,0.0333,0.0115,0.0402,0.0251,0.0217,0.0355,0.0278,0.0128,0.0038,0.0295,0.0337,0.0294,0.0267,0.0236,0.0162
    ,0.0215,0.0382,0.0498,0.0133,0.0396,0.0067,0.0018,0.0227,0.0281,0.0115,0.0072,0.0339,0.0177,0.0255,0.0347
    ,0.0298,0.0253,0.0388,0.0343,0.0160,0.0416,0.0330,0.0294,0.0010,0.0418,0.0057,0.0420,0.0169,0.1049,0.2210
    ,0.2814,0.3929,0.4927,0.5574,0.6033,0.7074,0.7531,0.8392,0.8839,0.9508,0.9898,1.0762,1.0991,1.1314
    ,1.1736,1.2457,1.3014,1.3086,1.3660,1.3775,1.4018,1.4522,1.4752,1.5326,1.5246,1.5647,1.5874,1.6122,1.6308
    ,1.6371,1.6499,1.6973,1.6799,1.7345,1.7303,1.7663,1.7875,1.7734,1.7676,1.8163,1.8198,1.8246])
y=np.array([
    0.0034,0.0415,0.1369,0.2850,0.4710,0.6692,0.8680,1.0585,1.2299,1.3568,1.4457,1.4892,1.4911,1.4637,1.3937,1.3073,1.2026,1.0949,0.9900,0.8903,0.8046,0.7419,0.6999,0.6842,0.6951,0.7136,0.7626,0.8096,0.8645,0.9294,0.9892,1.0349,1.0802,1.1088,1.1245,1.1268,1.1198,1.1032,1.0784,1.0465,1.0169,0.9800
    ,0.9553,0.9245,0.9128,0.8992,0.8874,0.8938,0.8997,0.9110,0.9174,0.9327,0.9529,0.9711,0.9855,1.0036,1.0078
    ,1.0159,1.0162,1.0158,1.0170,1.0012,0.9939,0.9870,0.9819,0.9666,0.9659,0.9599,0.9495,0.9531,0.9441,0.9518,0.9530,0.9575,0.9610
    ,0.9636,0.9680,0.9776,0.9833,0.9850,0.9851,0.9907,0.9870,0.9823,0.9850,0.9789,0.9805,0.9801,0.9701
    ,0.9743,0.9699,0.9625,0.9631,0.9697,0.9655,0.9702,0.9703,0.9641,0.9732,0.9739,0.9771,0.9755,0.9769,0.9725
])
t=np.array([
         0,0.0350,0.0699,0.1049,0.1399,0.1749,0.2098,0.2448,0.2798,0.3148
    ,0.3497,0.3847,0.4197,0.4546,0.4896,0.5246,0.5596,0.5945,0.6295,0.6645,0.6994,0.7344,0.7694
    ,0.8044,0.8393,0.8743,0.9093,0.9443,0.9792,1.0142,1.0492,1.0841,1.1191,1.1541,1.1891,1.2240,1.2590,1.2940,1.3290,1.3639,1.3989
    ,1.4339,1.4688,1.5038,1.5388,1.5738,1.6087,1.6437,1.6787,1.7136,1.7486,1.7836,1.8186,1.8535,1.8885,1.9235,1.9585,1.9934,2.0284,2.0634,2.0983,2.1333,2.1683,2.2033,2.2382,2.2732,2.3082,2.3432,2.3781,2.4131,2.4481,2.4830,2.5180,2.5530,2.5880,2.6229,2.6579,2.6929,2.7278,2.7628,2.7978,2.8328,2.8677,2.9027,2.9377,2.9727,3.0076,3.0426,3.0776,3.1125,3.1475,3.1825,3.2175,3.2524,3.2874,3.3224,3.3573,3.3923,3.4273,3.4623,3.4972,3.5322,3.5672,3.6022])

y2=[math.log((2-i)/2) for i in y1]
plt.subplot(2,1,1)
plt.plot(t1,y1)
plt.plot(t1,y2)
plt.subplot(2,1,2)
plt.plot(t,y)
plt.show()
def Pid(T,ta,K):
    Zn=[1.2,1,2,1,.5,1]
    Iae=[1.43,.92,1.14,.75,.48,1.14]
    Ise=[1.5,.95,.92,.77,.56,1]
    Itae=[1.46,.95,1.18,.74,.38,1]
    Teta=ta/T
    #Zn
    K2=1/K*Zn[0]*Teta**(-1*Zn[1])
    Ti=T*Zn[2]*Teta**Zn[3]
    Td=T*Zn[4]*Teta**Zn[5]
    print(f"K(s) for ZN:{K2}(1+{Td}s+1/({Ti}s)")
    #Iae
    K2=1/K*Iae[0]*Teta**(-1*Iae[1])
    Ti=T*Iae[2]*Teta**Iae[3]
    Td=T*Iae[4]*Teta**Iae[5]
    print(f"K(s) for Iae:{K2}(1+{Td}s+1/({Ti}s)")
    #Ise
    K2=1/K*Ise[0]*Teta**(-1*Ise[1])
    Ti=T*Ise[2]*Teta**Ise[3]
    Td=T*Ise[4]*Teta**Ise[5]
    print(f"K(s) for Ise:{K2}(1+{Td}s+1/({Ti}s)")
    #Itae
    K2=1/K*Itae[0]*Teta**(-1*Itae[1])
    Ti=T*Itae[2]*Teta**Itae[3]
    Td=T*Itae[4]*Teta**Itae[5]
    print(f"K(s) for Itae:{K2}(1+{Td}s+1/({Ti}s)")

Pid(.31,1,2)
#K(s) for ZN:0.186(1+0.5s+1/(2.0s)
#K(s) for Iae:0.2434214248059087(1+0.5655234267503483s+1/(0.8506389695948509s)
#K(s) for Ise:0.24652154026387113(1+0.56s+1/(0.7027502631874911s)
#K(s) for Itae:0.2399476325235012(1+0.38000000000000006s+1/(0.8702340011032949s)
