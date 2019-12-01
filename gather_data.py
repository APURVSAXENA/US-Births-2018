import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


with open("Nat2018PublicUS.c20190509.r20190717.txt") as myfile:
    df = [next(myfile) for x in range(3801534)]
    

# Birth details
DOB_YY, DOB_MM, DOB_TT, DOB_WK, BFACIL = [[] for _ in range(5)]   

# Mother's details
MAGE_IMPFLG, MAGER, MBSTATE_REC, RESTATUS = [[] for _ in range(4)]
MRACE31, MRAVE6, MRACE15, MRACEIMP, MHISPX = [[] for _ in range(5)]
DMAR, MAR_IMP = [[] for _ in range(2)]
MEDUC = []   

# Father's details
FAGECOMB = []
FRACE31, FRACE6, FRACE15, FHISPX = [[] for _ in range(4)]
FEDUC = []    

# Prior prenatal 
PRIORLIVE, PRIORDEAD, PRIORTERM = [[] for _ in range(3)]
ILLB_R, ILOP_R, ILP_R = [[] for _ in range(3)]    

# Prenatal care
PRECARE, PREVIS = [[] for _ in range(2)]

# WIC details
WIC, CIG_0, CIG_1, CIG_2, CIG_3 = [[] for _ in range(5)]   

# Mothers height and weight
M_Ht_In, BMI, PWgt_R, DWgt_R, WTGAIN = [[] for _ in range(5)]

# Risk Factors
RF_PDIAB, RF_GDIAB, RF_PHYPE, RF_GHYPE, RF_EHYPE, RF_PPTERM = [[] for _ in range(6)]
RF_INFTR, RF_FEDRG, RF_ARTEC = [[] for _ in range(3)] 
RF_CESAR, RF_CESARN = [[] for _ in range(2)]
NO_RISKS = []

# Infections present
IP_GON, IP_SYPH, IP_CHLAM, IP_HEPB, IP_HEPC, NO_INFEC = [[] for _ in range(6)]

# Obstetric Procedures details
OB_ECVS, OB_ECVF = [[] for _ in range(2)]

# Characteristics of Labor and Delivery
LD_INDL, LD_AUGM, LD_STER, LD_ANTB, LD_CHOR, LD_ANES = [[] for _ in range(6)]

# Method of Delivery
ME_PRES, ME_ROUT, ME_TRIAL, RDMETH_REC = [[] for _ in range(4)]

# Maternal Morbidity
MM_MTR, MM_PLAC, MM_RUPT, MM_UHYST, MM_AICU, NO_MMORB = [[] for _ in range(6)]

# Attendent
ATTEND, MTRAN, PAY, PAY_REC = [[] for _ in range(4)] 

APGAR5, APGAR10, DPLURAL, IMP_PLUR, SETORDER_R = [[] for _ in range(5)]

SEX, IMP_SEX, DLMP_MM, DLMP_YY = [[] for _ in range(4)]

# Baby's weight
DBWT = []    


for i in range(len(df)):
#for i in range(10**6):    
    #
    DOB_YY.append(int(df[i][8:12]))
    DOB_MM.append(int(df[i][12:14]))
    DOB_TT.append(int(df[i][18:22]))
    DOB_WK.append(int(df[i][22:23]))
    BFACIL.append(int(df[i][31:32]))
    #
    MAGE_IMPFLG.append(df[i][72:73])
    MAGER.append(int(df[i][74:76]))
    MBSTATE_REC.append(int(df[i][83:84]))
    RESTATUS.append(int(df[i][103:104]))
    MRACE31.append(int(df[i][104:106]))
    MRAVE6.append(int(df[i][106:107]))
    MRACE15.append(int(df[i][107:109]))
    MRACEIMP.append(df[i][110:111])
    MHISPX.append(int(df[i][111:112]))
    DMAR.append(df[i][119:120])
    MAR_IMP.append(df[i][120:121])
    MEDUC.append(int(df[i][123:124]))
    #
    FAGECOMB.append(int(df[i][146:148]))
    FRACE31.append(int(df[i][150:152]))
    FRACE6.append(int(df[i][152:153]))
    FRACE15.append(int(df[i][153:155]))
    FHISPX.append(int(df[i][158:159]))
    FEDUC.append(int(df[i][162:163]))
    #
    PRIORLIVE.append(int(df[i][170:172]))
    PRIORDEAD.append(int(df[i][172:174]))
    PRIORTERM.append(int(df[i][174:176]))
    #
    ILLB_R.append(int(df[i][197:200]))
    ILOP_R.append(int(df[i][205:208]))
    ILP_R.append(int(df[i][213:216]))
    #
    PRECARE.append(int(df[i][223:225]))
    PREVIS.append(int(df[i][237:239]))
    #
#    WIC.append(df[i][250:251])
    CIG_0.append(int(df[i][252:254]))
#     CIG_1.append(int(df[i][254:256]))
#     CIG_2.append(int(df[i][256:258]))
#     CIG_3.append(int(df[i][258:260]))
    #
    M_Ht_In.append(int(df[i][279:281]))
    BMI.append(float(df[i][282:286]))
    PWgt_R.append(int(df[i][291:294]))
    DWgt_R.append(int(df[i][298:301]))
    WTGAIN.append(int(df[i][303:305]))
    #
#     RF_PDIAB.append(df[i][312:313])
#     RF_GDIAB.append(df[i][313:314])
#     RF_PHYPE.append(df[i][314:315])
#     RF_GHYPE.append(df[i][315:316])
#     RF_EHYPE.append(df[i][316:317])
#     RF_PPTERM.append(df[i][317:318])
#     RF_INFTR.append(df[i][324:325])
#     RF_FEDRG.append(df[i][325:326])
#     RF_ARTEC.append(df[i][326:327])
    RF_CESAR.append(df[i][330:331])
    RF_CESARN.append(df[i][331:333])
    NO_RISKS.append(df[i][336:337])
    #
    IP_GON.append(df[i][342:343])
#     IP_SYPH.append(df[i][343:344])
#     IP_CHLAM.append(df[i][344:345])
#     IP_HEPB.append(df[i][345:346])
#     IP_HEPC.append(df[i][346:347])
    NO_INFEC.append(df[i][352:353])
    #
    LD_INDL.append(df[i][382:383])
#     LD_AUGM.append(df[i][383:384])
#     LD_STER.append(df[i][384:385])
#     LD_ANTB.append(df[i][385:386])
#     LD_CHOR.append(df[i][386:387])
#     LD_ANES.append(df[i][387:388])
#     #
#     ME_PRES.append(int(df[i][400:401]))
#     ME_ROUT.append(df[i][402:403])
#     ME_TRIAL.append(int(df[i][403:404]))
    RDMETH_REC.append(int(df[i][406:407]))
    #
#     MM_MTR.append(df[i][414:415])
#     MM_PLAC.append(df[i][415:416])
#     MM_RUPT.append(df[i][416:417])
#     MM_UHYST.append(df[i][417:418])
    MM_AICU.append(df[i][418:419])
    NO_MMORB.append(int(df[i][426:427]))
    #
    ATTEND.append(int(df[i][432:433]))
    MTRAN.append(df[i][433:434])
    PAY.append(int(df[i][434:435]))
    PAY_REC.append(int(df[i][435:436]))
    #
#     APGAR5.append(int(df[i][443:445]))
#     APGAR10.append(int(df[i][447:449]))
#     DPLURAL.append(int(df[i][453:454]))
#     IMP_PLUR.append(df[i][455:456])
#     SETORDER_R.append(int(df[i][458:459]))
    #
    SEX.append(df[i][474:475])
    IMP_SEX.append(df[i][475:476])
    DLMP_MM.append(int(df[i][476:478]))
    DLMP_YY.append(int(df[i][480:484]))
    #
    DBWT.append(int(df[i][503:507]))
    
    
dfFinal = pd.DataFrame({'DOB_YY':DOB_YY,
 'DOB_MM':DOB_MM,
 'DOB_TT':DOB_TT,
 'DOB_WK':DOB_WK,
 'BFACIL':BFACIL,
 'MAGE_IMPFLG':MAGE_IMPFLG,
 'MAGER':MAGER,
 'MBSTATE_REC':MBSTATE_REC,
 'RESTATUS':RESTATUS,
 'MRACE31':MRACE31,
 'MRAVE6':MRAVE6,
 'MRACE15':MRACE15,
 'MRACEIMP':MRACEIMP,
 'MHISPX':MHISPX,
 'DMAR':DMAR,
 'MAR_IMP':MAR_IMP,
 'MEDUC':MEDUC,
 'FAGECOMB':FAGECOMB,
 'FRACE31':FRACE31,
 'FRACE6':FRACE6,
 'FRACE15':FRACE15,
 'FHISPX':FHISPX,
 'FEDUC':FEDUC,
 'PRIORLIVE':PRIORLIVE,
 'PRIORDEAD':PRIORDEAD,
 'PRIORTERM':PRIORTERM,
 'ILLB_R':ILLB_R,
 'ILOP_R':ILOP_R,
 'ILP_R':ILP_R,
 'PRECARE':PRECARE,
 'PREVIS':PREVIS,
# 'WIC':WIC,
 'CIG_0':CIG_0,
#  'CIG_1':CIG_1,
#  'CIG_2':CIG_2,
#  'CIG_3':CIG_3,
 'M_Ht_In':M_Ht_In,
 'BMI':BMI,
 'PWgt_R':PWgt_R,
 'DWgt_R':DWgt_R,
 'WTGAIN':WTGAIN,
#  'RF_PDIAB':RF_PDIAB,
#  'RF_GDIAB':RF_GDIAB,
#  'RF_PHYPE':RF_PHYPE,
#  'RF_GHYPE':RF_GHYPE,
#  'RF_EHYPE':RF_EHYPE,
#  'RF_PPTERM':RF_PPTERM,
#  'RF_INFTR':RF_INFTR,
#  'RF_FEDRG':RF_FEDRG,
#  'RF_ARTEC':RF_ARTEC,
 'RF_CESAR':RF_CESAR,
 'RF_CESARN':RF_CESARN,
 'NO_RISKS':NO_RISKS,
 'IP_GON':IP_GON,
#  'IP_SYPH':IP_SYPH,
#  'IP_CHLAM':IP_CHLAM,
#  'IP_HEPB':IP_HEPB,
#  'IP_HEPC':IP_HEPC,
 'NO_INFEC':NO_INFEC,
 'LD_INDL':LD_INDL,
#  'LD_AUGM':LD_AUGM,
#  'LD_STER':LD_STER,
#  'LD_ANTB':LD_ANTB,
#  'LD_CHOR':LD_CHOR,
#  'LD_ANES':LD_ANES,
#  'ME_PRES':ME_PRES,
#  'ME_ROUT':ME_ROUT,
#  'ME_TRIAL':ME_TRIAL,
 'RDMETH_REC':RDMETH_REC,
#  'MM_MTR':MM_MTR,
#  'MM_PLAC':MM_PLAC,
#  'MM_RUPT':MM_RUPT,
#  'MM_UHYST':MM_UHYST,
 'MM_AICU':MM_AICU,
 'NO_MMORB':NO_MMORB,
 'ATTEND':ATTEND,
 'MTRAN':MTRAN,
 'PAY':PAY,
 'PAY_REC':PAY_REC,
#  'APGAR5':APGAR5,
#  'APGAR10':APGAR10,
#  'DPLURAL':DPLURAL,
#  'IMP_PLUR':IMP_PLUR,
#  'SETORDER_R':SETORDER_R,
 'SEX':SEX,
 'IMP_SEX':IMP_SEX,
 'DLMP_MM':DLMP_MM,
 'DLMP_YY':DLMP_YY,
 'DBWT':DBWT
})

dfFinal.to_csv('data.csv', index=False)
