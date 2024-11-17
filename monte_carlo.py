import statistics as stat
import matplotlib.pyplot as plt
import random as rnd

history_price = [68,69, 70, 73, 72, 70 ,69 ,69 ,68 ,67 ,70 ,75 ,76 ,76 ,80 ,89 ,88 ,90 ,87 ,91]

Ti_le_thay_doi = []
for i in range (len(history_price)):
 if i == 0:
  pass
 else: Ti_le_thay_doi.append((history_price[i] - history_price[i-1])/history_price[i-1])
Do_lech_chuan = stat.stdev(Ti_le_thay_doi)
print(Do_lech_chuan)

def du_doan(Do_lech_chuan, past_price):
   ngay_du_doan = [i for i in range(1,101)]
   gia_du_doan = []
   gia_tri = past_price[-1]
   for i in range(1,101):
     gia_tri = gia_tri + gia_tri*rnd.normalvariate(0,Do_lech_chuan)
     gia_du_doan.append(gia_tri)
   return([ngay_du_doan, gia_du_doan])

gia_du_doan = du_doan(Do_lech_chuan, history_price)


plt.plot(gia_du_doan[0],gia_du_doan[1])
plt.title("random price walk")
plt.xlabel("day")
plt.ylabel("stock price")

plt.figure()
for i in range(0,30):
    gia_du_doan = du_doan(Do_lech_chuan,history_price)
    plt.plot(gia_du_doan[0],gia_du_doan[1])
plt.title("monte-carlo simulation of stock price development")
plt.xlabel("day")
plt.ylabel("stock price")