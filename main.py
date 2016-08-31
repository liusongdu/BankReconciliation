# -*- coding: utf-8 -*-

qi_shou = []
qi_fu = []
i = 0
qi_qi_mo_yu_er = 0
for line in open("BankReconciliation/a.csv"):

    if i == 0:
        i += 1
        continue

    c = line.split(',')
    if not line:
        break
    elif c[3]:
        # print(c[3])
        qi_shou.append(float(c[3].replace('"', '')))
        qi_qi_mo_yu_er = float(c[6].replace('"', ''))
    elif c[4]:
        # print(c[4])
        qi_fu.append(float(c[4].replace('"', '')))
        qi_qi_mo_yu_er = float(c[6].replace('"', ''))
    else:
        pass

yin_shou = []
yin_fu = []
j = 0
yin_qi_mo_yu_er = 0
for line in open("BankReconciliation/b.csv"):

    if j == 0:
        j += 1
        continue

    c = line.split(',')
    if not line:
        break
    elif c[3]:
        # print(c[3])
        yin_fu.append(float(c[3].replace('"', '')))
        yin_qi_mo_yu_er = float(c[6].replace('"', ''))
    elif c[4]:
        # print(c[4])
        yin_shou.append(float(c[4].replace('"', '')))
        yin_qi_mo_yu_er = float(c[6].replace('"', ''))
    else:
        pass

qi_yshou_yin_nshou = []
for qs in qi_shou:
    if qs not in yin_shou:
        qi_yshou_yin_nshou.append(qs)
print("企收银未收: %s" % qi_yshou_yin_nshou)

yin_shou_qi_nshou = []
for ys in yin_shou:
    if ys not in qi_shou:
        yin_shou_qi_nshou.append(ys)
print("银收企未收: %s" % yin_shou_qi_nshou)

qi_yfu_yin_nfu = []
for count in range(len(qi_fu)):
    for qf in qi_fu:
        if qf in yin_fu:
            qi_fu.remove(qf)
            yin_fu.remove(qf)
        elif qf not in yin_fu:
            qi_yfu_yin_nfu.append(qf)
            qi_fu.remove(qf)
        else:
            pass
# for eacha in qi_fu:
#     if eacha in yin_fu:
#         qi_fu.remove(eacha)
#         yin_fu.remove(eacha)
#     else:
#         qi_yfu_yin_nfu.append(eacha)
#         qi_fu.remove(eacha)
# for eacha1 in qi_fu:
#     if eacha1 in yin_fu:
#         qi_fu.remove(eacha1)
#         yin_fu.remove(eacha1)
#     else:
#         qi_yfu_yin_nfu.append(eacha1)
#         qi_fu.remove(eacha1)
print("企付银未付: %s" % qi_yfu_yin_nfu)

yin_yfu_qi_nfu = []
for count in range(len(yin_fu)):
    for yf in yin_fu:
        if yf in qi_fu:
            qi_fu.remove(yf)
            yin_fu.remove(yf)
        elif yf not in qi_fu:
            yin_yfu_qi_nfu.append(yf)
            yin_fu.remove(yf)
        else:
            pass
print("银付企未付: %s" % yin_yfu_qi_nfu)

# bank reconciliation
import codecs
f = open('c.csv', 'w')
f.write(codecs.BOM_UTF8)
f.write('银行存款余额调节表,,,\n')
f.write(',,,\n')
f.write('开户行及账号：,,,金额单位：元\n')
f.write('项目,金额,项目,金额\n')

line1 = ''
f.write('企业银行存款日记账余额,'); f.write(str(qi_qi_mo_yu_er))
f.write(',银行对账单余额,'); f.write(str(yin_qi_mo_yu_er))
f.write('\n')

yin_shou_qi_nshou_sum = sum(yin_shou_qi_nshou)
qi_yshou_yin_nshou_sum = sum(qi_yshou_yin_nshou)
line2 = '加：银行已收、企业未收款,' + str(yin_shou_qi_nshou_sum) + ',加：企业已收、银行未收款,' +\
        str(qi_yshou_yin_nshou_sum) + '\n'
f.write(line2)

yin_yfu_qi_nfu_sum = sum(yin_yfu_qi_nfu)
qi_yfu_yin_nfu_sum = sum(qi_yfu_yin_nfu)
line3 = '减：银行已付、企业未付款,' + str(yin_yfu_qi_nfu_sum) + ',减：企业已付、银行未付款,' + \
        str(qi_yfu_yin_nfu_sum) + '\n'
f.write(line3)

tiao_jie_hou_yu_er_1 = qi_qi_mo_yu_er + yin_shou_qi_nshou_sum - yin_yfu_qi_nfu_sum
tiao_jie_hou_yu_er_2 = yin_qi_mo_yu_er + qi_yshou_yin_nshou_sum - qi_yfu_yin_nfu_sum
line4 = '调节后的存款余额,' + str(tiao_jie_hou_yu_er_1) + ',调节后的存款余额,' + str(tiao_jie_hou_yu_er_2) + '\n'
f.write(line4)

f.write('主管：,会计：,,出纳：\n')
f.write(',,编制单位：,\n')
f.close()

# import csv
# f = csv.writer(file('d.csv', 'wb'))
# f.write(codecs.BOM_UTF8)
# f.writerow(['Column1', 'Column2', 'Column3', 'Column4'])
# f.writerow([u'银行存款余额调节表'.encode('utf-8'), '', '', ''])
# f.writerow(['', '', '', ''])
# f.writerow([u'开户行及账号：'.encode('gb2312'), '', '', '金额单位：元'])
# f.writerow(['项目', '金额', '项目', '金额'])
# line1 = ''
# f.writerow(['企业银行存款日记账余额', '40000', '银行对账单余额', '10000'])
# line2 = ['加：银行已收、企业未收款', str(sum(yin_shou_qi_nshou)), '加：企业已收、银行未收款',
#          str(sum(qi_yshou_yin_nshou))]
# f.writerow(line2)
# line3 = ['减：银行已付、企业未付款', str(sum(yin_yfu_qi_nfu)), '减：企业已付、银行未付款',
#          str(sum(qi_yfu_yin_nfu))]
# f.writerow(line3)
# line4 = ['调节后的存款余额', '50000', '调节后的存款余额', '50000']
# f.writerow(line4)
# f.writerow(['主管：', '会计：', '', '出纳：'])
# f.writerow(['', '', '编制单位：', ''])
# # f.close()  # AttributeError: '_csv.writer' object has no attribute 'close'

# >>>for i in range(0,10):f.write(str(random.randint(0,9)))
# >>>f.write('\n')