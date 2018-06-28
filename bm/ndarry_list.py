import numpy as np
ndarry_list = [[-0.04394945,  0.11168578,  0.11446603,  0.01598915, -0.07099712,
       -0.00923932, -0.07804307, -0.0459201 ,  0.06476289, -0.04744239,
        0.11541356, -0.00088306, -0.16355418, -0.01036702,  0.04525531,
        0.11157607, -0.1545781 , -0.09439021, -0.08233855, -0.11549354,
       -0.0374289 ,  0.03927801, -0.0028579 ,  0.01179263, -0.14549425,
       -0.28355154, -0.06724866, -0.06585933,  0.11017239, -0.01333873,
       -0.05150978, -0.02668355, -0.16767377,  0.00538171,  0.05470857,
        0.08843984, -0.07352783, -0.02900586,  0.15592206, -0.03044806,
       -0.17156258,  0.07489391,  0.08151377,  0.22384171,  0.21890587,
        0.01849629,  0.04685329, -0.04175041,  0.08124159, -0.1798473 ,
        0.09855372,  0.1668451 ,  0.10313977,  0.10452038,  0.04122609,
       -0.11660485, -0.06852251,  0.14946502, -0.15165952,  0.0995129 ,
        0.0769681 , -0.02260226, -0.03677558, -0.06167378,  0.16955709,
        0.12051725, -0.14919902, -0.20576946,  0.09915499, -0.21391669,
       -0.03369395,  0.08774295, -0.08189957, -0.10871394, -0.27231055,
        0.07456289,  0.40259442,  0.11795079, -0.11588251, -0.01624947,
       -0.06493897, -0.08174223,  0.0113885 ,  0.08044887, -0.10851943,
       -0.02176684, -0.01264496,  0.09066909,  0.20053363,  0.00370402,
       -0.00782147,  0.13928738,  0.00832864,  0.01833988, -0.05595473,
        0.06449525, -0.1205658 , -0.02736579, -0.09206872, -0.04786462,
        0.00138056, -0.09433454,  0.05434254,  0.14135496, -0.16635156,
        0.19808754,  0.00225352,  0.00203428,  0.04647459,  0.13183065,
       -0.10787375, -0.05906459,  0.17682475, -0.22534271,  0.18522385,
        0.17708462,  0.04152733,  0.05278611,  0.06851013,  0.09259883,
        0.0055513 ,  0.00904205, -0.12914723, -0.05244024, -0.02459343,
       -0.05844498,  0.06251694,  0.05434564], [-0.04877899,  0.1308656 ,  0.0837459 ,  0.00859126, -0.08033846,
        0.00587106, -0.08045259, -0.04783835,  0.05847517, -0.03814692,
        0.11808434,  0.00217671, -0.16960464, -0.04103108,  0.03802131,
        0.14061338, -0.16209647, -0.08397658, -0.08654225, -0.12055577,
       -0.00195537,  0.02958921,  0.00166158,  0.01508614, -0.12934563,
       -0.2601141 , -0.04971312, -0.05415082,  0.11654394, -0.05066679,
       -0.04343724, -0.03367691, -0.18907103, -0.00184834,  0.03532129,
        0.05808071, -0.06376681, -0.03379511,  0.16604301, -0.01717184,
       -0.18214351,  0.11893691,  0.07839489,  0.21427885,  0.21648614,
        0.00786758,  0.03620221, -0.05898883,  0.08731534, -0.17419291,
        0.08602931,  0.16299458,  0.10632461,  0.08902128,  0.02599547,
       -0.10445929, -0.08371358,  0.1529922 , -0.15672901,  0.08239788,
        0.07102492, -0.01834128, -0.04608309, -0.08061088,  0.14461081,
        0.11791465, -0.13889575, -0.19641483,  0.10238914, -0.18212542,
       -0.03519419,  0.09841532, -0.06713741, -0.11229936, -0.27369532,
        0.07930957,  0.38032916,  0.1289472 , -0.13160683, -0.02222336,
       -0.06954007, -0.07075296,  0.01302558,  0.07903662, -0.09672134,
       -0.02145427,  0.01055376,  0.09958273,  0.18436539,  0.0014025 ,
       -0.00878625,  0.17053193,  0.04338928,  0.01856331, -0.06794323,
        0.06612846, -0.10087752, -0.0430835 , -0.10112548, -0.06317586,
       -0.00812685, -0.08761881,  0.06335609,  0.13632587, -0.16826598,
        0.18642637,  0.01972187, -0.00060321,  0.02927373,  0.13939607,
       -0.08454397, -0.04046897,  0.145218  , -0.22754531,  0.19536796,
        0.18637796,  0.03918184,  0.03848521,  0.07692496,  0.08836521,
        0.00654487, -0.02004872, -0.11406749, -0.05725687,  0.00428705,
       -0.04324342,  0.07267085,  0.05261748]]

